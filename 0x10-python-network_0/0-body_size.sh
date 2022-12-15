#!/usr/bin/bash
#returns the content size of a request in bytes
curl -sI "$@" | grep -i content-length | awk '{print $2}'
