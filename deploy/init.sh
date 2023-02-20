#!/bin/bash

MTA_DIR=/opt/mta
DEPLOY_DIR=$MTA_DIR/deploy

$DEPLOY_DIR/deploy.sh

if [[ $? -ne 0 ]]
then
  echo "deploy.sh failed. Exiting"
  exit 1
fi



# Cleaning up previous runs
echo "Killing previous chromium-browser"
pkill chromium-browse
echo "Finished killing previous processes"

echo "starting browser"
export DISPLAY=":0.0"
chromium-browser --kiosk --app http://localhost
echo "brower started"

echo "${0} completed"
