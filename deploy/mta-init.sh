#!/bin/bash

MTA_DIR=/opt/mta-py


# Cleaning up previous runs
echo "Killing previous python, node, chromium-browser"
pkill python
pkill node
pkill chromium-browser
echo "Finished killing previous processes"

echo "Activating python environment"
source $MTA_DIR/env/bin/activate
echo "Done activating py env."

echo "Starting be app"
echo $(date) >> be.log
python -m flask --app ${MTA_DIR}/server.py run &>> be.log &
echo "process: $!" >> be.log
echo "Be App started"

echo "Starting frontend app"
export BROWSER=none
echo $(date) >> fe.log
npm --prefix ${MTA_DIR}/mta-fe run start &>> fe.log &
echo "$!" >> fe.log
echo "Fe app started"

echo "sleeping to ensure browser starts after react-app"
sleep 10
echo "done sleeping"

echo "starting browser"
chromium-browser --kiosk --app http://localhost:3000
echo "brower started"

echo "${0} completed"
