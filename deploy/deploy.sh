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


# MTA variables
MTA_DIR=/opt/mta
LOG_DIR=$MTA_DIR/logs
DIST_DIR=$MTA_DIR/dist
DIST_TMP_DIR=$DIST_DIR/tmp

# Github variables
# GITHUB_TOKEN= loaded from .env
OWNER=macolby14
REPO=mta-py


# load env variables from $MTA_DIR/.env
set -o allexport
source $MTA_DIR/.env
set +o allexport




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


# frontend
function deploy_frontend() {

  # remove and recreate any old folders
  rm -r $DIST_DIR/frontend-dist
  mkdir $DIST_DIR/frontend-dist

  FRONTEND_WORKFLOW_FILE=$DIST_TMP_DIR/frontend-workflow-data.json

  log "saving frontend workflow info" curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/$OWNER/$REPO/actions/workflows/build-frontend.yml/runs?per_page=1&branch=main&event=push&status=success" \
    > $FRONTEND_WORKFLOW_FILE

  ARTIFACT_URL=$(jq .workflow_runs[0].artifacts_url $FRONTEND_WORKFLOW_FILE | tr -d '"')

  ARCHIVE_DOWNLOAD_URL=$(log "getting frontend archive url" curl -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" ${ARTIFACT_URL} \
    | jq .artifacts[0].archive_download_url \
    | tr -d '"')

  log "downloading frontend archive" curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    $ARCHIVE_DOWNLOAD_URL > $DIST_TMP_DIR/frontend-dist.zip

  log "unzipping fe artifact" unzip -d $DIST_DIR/frontend-dist $DIST_TMP_DIR/frontend-dist.zip
}

# backend
function deploy_backend() {
  BACKEND_WORKFLOW_FILE=$DIST_TMP_DIR/backend-workflow-data.json


  # remove and recreate any old folders
  rm -r $DIST_DIR/backend-dist
  mkdir $DIST_DIR/backend-dist


  log "cleaning up python from previous runs" pkill python3

  log "saving backend workflow info" curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/$OWNER/$REPO/actions/workflows/build-backend.yml/runs?per_page=1&branch=main&event=push&status=success" \
    > $BACKEND_WORKFLOW_FILE


  ARTIFACT_URL=$(jq .workflow_runs[0].artifacts_url $BACKEND_WORKFLOW_FILE | tr -d '"')

  ARCHIVE_DOWNLOAD_URL=$(log "getting archive url" curl -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" ${ARTIFACT_URL} \
    | jq .artifacts[0].archive_download_url \
    | tr -d '"')



  log "downloading archive" curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    $ARCHIVE_DOWNLOAD_URL > $DIST_TMP_DIR/backend-dist.zip

  log "unzipping artifact" unzip -d $DIST_DIR/backend-dist $DIST_TMP_DIR/backend-dist.zip

  log "deactivating existing env" deactivate



  log "creating python venv" python3 -m venv backend-dist/venv
  log  "activating venv" source backend-dist/venv/bin/activate

  log "installing flask app" python3 -m pip install backend-dist/mta_flask*.whl

  echo $(date) >> ${LOG_DIR}/be.log
  log "starting flask app" python3 -m flask --app mta_flask run &>> ${LOG_DIR}/be.log &
  echo "process: $!" >> ${LOG_DIR}/be.log

  log "deactivating existing env" deactivate
}


deploy_frontend
deploy_backend

log "removing tmp dir" rm -r $DIST_DIR/tmp
