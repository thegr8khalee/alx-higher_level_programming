#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.... -sI for silent anf fetch spaecified headers without downloading the actual content, grep filters lines with allow, then cut with delim of space , -f 2- extracts everything from the second field to the end of the line
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
