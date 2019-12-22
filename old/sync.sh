#!/usr/bin/env bash

DESTINATION="pi@192.168.1.3:/home/pi/apps"

rsync -avzH  --partial /home/tomek/workspace/my/loremote_sensors $DESTINATION/
