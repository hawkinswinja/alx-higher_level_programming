#!/bin/bash
#Dsiplay the status code without redirections
curl -sw "%{http_code}" -o /dev/null "$@"
