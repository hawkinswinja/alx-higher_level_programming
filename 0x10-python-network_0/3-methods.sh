#!/usr/bin/env bash
#Display allowed verbs
curl -sI "$@" | grep -i allow | sed -e "s/Allow: //"
