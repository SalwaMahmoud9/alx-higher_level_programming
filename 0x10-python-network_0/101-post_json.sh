#!/bin/bash
# post json
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
