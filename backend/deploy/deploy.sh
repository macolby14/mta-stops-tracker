#!/bin/bash


function log() {
  PRINT=$1
  shift 1;
  echo "started $PRINT" > /dev/tty;
  "$@";
  if [[ $? -eq 0 ]]
  then
    echo "finished $PRINT" > /dev/tty;
  else
    echo "failed $PRINT" > /dev/tty;
    echo > /dev/tty
  fi
  }

set -o allexport
source ../.env
set +o allexport


# Github variables
# GITHUB_TOKEN= loaded from .env
OWNER=macolby14
REPO=mta-py
WORKFLOW_ID=build-backend.yml

# MTA variables
MTA_DIR=/opt/mta
LOG_DIR=$MTA_DIR/logs
DIST_DIR=$MTA_DIR/dist
DIST_TMP_DIR=$DIST_DIR/tmp

if [[ ! -d $LOG_DIR ]]
then
  log "making $LOG_DIR" mkdir $LOG_DIR
fi

if [[ ! -d $DIST_TMP_DIR ]]
then
  log "Making $DIST_TMP_DIR" mkdir -p $DIST_TMP_DIR
else
  echo "$DIST_TMP_DIR already exists but should have been cleaned up" 1>&2
fi

cd $DIST_DIR


log "cleaning up python from previous runs" pkill python3
log "cleaning chromium-browser from previous runs" pkill chromium-browser

log "saving workflow info" curl \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/$OWNER/$REPO/actions/workflows/build-backend.yml/runs?per_page=1&branch=main&event=push&status=success" \
   > $DIST_TMP_DIR/workflow-data.json


WORKFLOW_ID=$(jq .workflow_runs[0].id $DIST_TMP_DIR/workflow-data.json)
ARTIFACT_URL=$(jq .workflow_runs[0].artifacts_url $DIST_TMP_DIR/workflow-data.json | tr -d '"')

ARCHIVE_DOWNLOAD_URL=$(log "getting archive url" curl -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" ${ARTIFACT_URL} \
  | jq .artifacts[0].archive_download_url \
  | tr -d '"')


log "downloading archive" curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  $ARCHIVE_DOWNLOAD_URL > $DIST_TMP_DIR/out.zip

log "unzipping artifact" unzip -d $DIST_DIR $DIST_TMP_DIR/out.zip

log "deactivating existing env" deactivate

log "creating python venv" python3 -m venv venv
log  "activating venv" source venv/bin/activate

log "installing flask app" python3 -m pip install mta_flask*.whl

echo $(date) >> ${LOG_DIR}/be.log
log "starting flask app" python3 -m flask --app mta_flask run &>> ${LOG_DIR}/be.log
echo "process: $!" >> ${LOG_DIR}/be.log

log "removing tmp dir" rm -r $DIST_DIR/tmp

log "deactivating existing env" deactivate
