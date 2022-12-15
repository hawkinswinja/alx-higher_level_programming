#!/bin/bash
#Post a json file
curl -s --request POST -H"Content-Type: application/json" -d"@$2" "$1"
