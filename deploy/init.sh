#!/bin/bash

MTA_DIR=/opt/mta
DEPLOY_DIR=$MTA_DIR/deploy

$DEPLOY_DIR/upgrade.sh

if [[ $? -ne 0 ]]
then
  echo "upgrade.sh failed. Exiting"
  exit 1
fi

$DEPLOY_DIR/run.sh
