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


# Start
MTA_DIR=/opt/mta
LOG_DIR=$MTA_DIR/logs
DIST_DIR=$MTA_DIR/dist
cd $DIST_DIR

log "cleaning up python from previous runs" pkill python3

# Start the backend 
log "deactivating existing env" deactivate
log "creating python venv" python3 -m venv backend-dist/venv
log  "activating venv" source backend-dist/venv/bin/activate

log_fail "installing flask app" python3 -m pip install backend-dist/mta_flask*.whl

echo $(date) >> ${LOG_DIR}/be.log
log_fail "starting flask app" python3 -m flask --app mta_flask run &>> ${LOG_DIR}/be.log &
echo "process: $!" >> ${LOG_DIR}/be.log

log "deactivating existing env" deactivate


# Start the browser
echo "Killing previous chromium-browser"
pkill chromium-browse
echo "Finished killing previous processes"

echo "starting browser"
export DISPLAY=":0.0"
chromium-browser --kiosk --app http://127.0.0.1
echo "brower started"

echo "${0} completed"
