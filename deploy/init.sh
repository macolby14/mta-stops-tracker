#!/bin/bash

MTA_DIR=/opt/mta-py
LOG_DIR=$MTA_DIR/deploy

# Cleaning up previous runs
echo "Killing previous chromium-browser"
pkill chromium-browse
echo "Finished killing previous processes"

echo "starting browser"
export DISPLAY=":0.0"
chromium-browser --kiosk --app http://localhost
echo "brower started"

echo "${0} completed"
