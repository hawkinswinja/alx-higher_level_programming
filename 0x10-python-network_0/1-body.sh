#!/usr/bin/env bash
#Display body of status 200 ok
status=$(curl -sLw "%{http_code}" -o >(cat >/tmp/curlbody) "$1")
if [ "$status" == 200 ]
then
  cat /tmp/curlbody
fi
