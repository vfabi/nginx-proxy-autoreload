#!/bin/bash


while true
do
 inotifywait --exclude .swp -e create -e modify -e delete -e move /etc/nginx/conf.d
 echo "[CONFIG-RELOADER] Checking Nginx configuration."
 nginx -t
 if [ $? -eq 0 ]
 then
  echo "[CONFIG-RELOADER] Detected Nginx configuration change."
  echo "[CONFIG-RELOADER] Executing: nginx -s reload."
  nginx -s reload
 fi
done
