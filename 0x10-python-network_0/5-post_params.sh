#!/usr/bin/env bash
#Post params to url using POST
curl -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$@"
