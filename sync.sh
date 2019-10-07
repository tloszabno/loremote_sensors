#!/usr/bin/env bash


DESTINATION="pi@192.168.1.8:/home/pi/apps"

rsync -avzH  --partial /home/tomek/workspace/private/loremote_sensors $DESTINATION/
