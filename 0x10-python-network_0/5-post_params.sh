#!/bin/bash
#Post params to url using POST
curl -s --request POST "$@" -d'email=test@gmail.com' -d'subject=I will always be here for PLD'
