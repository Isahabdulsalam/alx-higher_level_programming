#!/bin/bash
# Takes URL, display status code only
curl -o /dev/null -w '%{http_code}' -sLI "$1"
