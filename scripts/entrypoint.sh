#!/bin/bash
set -e

# rm -rf /usr/src/mytonctrl
# mv /usr/src/mytonctrl_fixes /usr/src/mytonctrl

echo "Starting validator and mytoncore"
systemctl start validator
systemctl start mytoncore

echo "Check logs, wait for Accept"
cat /var/ton-work/log

while [ 1 ]
do
    echo "Running!"
    sleep 60
done
