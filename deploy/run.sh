#!/bin/bash

# Cleaning up previous runs
echo "Killing previous chromium-browser"
pkill chromium-browse
echo "Finished killing previous processes"

echo "starting browser"
export DISPLAY=":0.0"
chromium-browser --kiosk --app http://127.0.0.1
echo "brower started"

echo "${0} completed"
