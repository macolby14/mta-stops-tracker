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
    return 1
  fi
  }

function log_fail(){
  log "$@";
  if [[ $? -eq 1 ]]
  then
    exit 1
  fi
}

set -o allexport
if [[ ! -f ../.env ]]
then
  echo "no .env variable"
  exit 1
fi
source ../.env
set +o allexport

# MTA variables
MTA_DIR=/opt/mta
LOG_DIR=$MTA_DIR/logs
DIST_DIR=$MTA_DIR/dist
DIST_TMP_DIR=$DIST_DIR/tmp

# Github variables
# GITHUB_TOKEN= loaded from .env
OWNER=macolby14
REPO=mta-stops-tracker

if [[ ! -d $LOG_DIR ]]
then
  log_fail "making $LOG_DIR" mkdir $LOG_DIR
fi

if [[ ! -d $DIST_TMP_DIR ]]
then
  log_fail "making $DIST_TMP_DIR" mkdir -p $DIST_TMP_DIR
else
  echo "$DIST_TMP_DIR already exists but should have been cleaned up" 1>&2
fi

cd $DIST_DIR


# frontend
function upgrade_frontend() {
  # Produces upgraded frontend static files by pulling latest from Github workflow
  # Frontend does not run. It is 100% static, so this is upgrading the frontend

  # remove and recreate any old folders
  rm -r $DIST_DIR/frontend-dist
  mkdir $DIST_DIR/frontend-dist

  FRONTEND_WORKFLOW_FILE=$DIST_TMP_DIR/frontend-workflow-data.json
  echo "Token is ${GITHUB_TOKEN}"
  log_fail "saving frontend workflow info" curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/$OWNER/$REPO/actions/workflows/build-frontend.yml/runs?per_page=1&branch=main&event=push&status=success" \
    > $FRONTEND_WORKFLOW_FILE

  ARTIFACT_URL=$(jq .workflow_runs[0].artifacts_url $FRONTEND_WORKFLOW_FILE | tr -d '"')

  ARCHIVE_DOWNLOAD_URL=$(log_fail "getting frontend archive url" curl -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" ${ARTIFACT_URL} \
    | jq .artifacts[0].archive_download_url \
    | tr -d '"')

  echo "curl -H 'Accept: application/vnd.github+json' -H 'Authorization: Bearer ${GITHUB_TOKEN}' -H 'X-GitHub-Api-Version: 2022-11-28' ${ARTIFACT_URL}"
  echo "Frontend ARCHIVE_DOWNLOAD_URL: ${ARCHIVE_DOWNLOAD_URL}"

  log_fail "downloading frontend archive" curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    $ARCHIVE_DOWNLOAD_URL > $DIST_TMP_DIR/frontend-dist.zip

  log_fail "unzipping fe artifact" unzip -d $DIST_DIR/frontend-dist $DIST_TMP_DIR/frontend-dist.zip
}

# backend
function upgrade_backend() {
  # Produces upgraded backend files by pulling latest from Github workflow

  BACKEND_WORKFLOW_FILE=$DIST_TMP_DIR/backend-workflow-data.json


  # remove and recreate any old folders
  rm -r $DIST_DIR/backend-dist
  mkdir $DIST_DIR/backend-dist



  log_fail "saving backend workflow info" curl \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/$OWNER/$REPO/actions/workflows/build-backend.yml/runs?per_page=1&branch=main&event=push&status=success" \
    > $BACKEND_WORKFLOW_FILE


  ARTIFACT_URL=$(jq .workflow_runs[0].artifacts_url $BACKEND_WORKFLOW_FILE | tr -d '"')

  ARCHIVE_DOWNLOAD_URL=$(log "getting archive url" curl -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $GITHUB_TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" ${ARTIFACT_URL} \
    | jq .artifacts[0].archive_download_url \
    | tr -d '"')



  log_fail "downloading archive" curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $GITHUB_TOKEN"\
    -H "X-GitHub-Api-Version: 2022-11-28" \
    $ARCHIVE_DOWNLOAD_URL > $DIST_TMP_DIR/backend-dist.zip

  log_fail "unzipping artifact" unzip -d $DIST_DIR/backend-dist $DIST_TMP_DIR/backend-dist.zip

  
}

upgrade_frontend
upgrade_backend

log "removing tmp dir" rm -r $DIST_DIR/tmp
