#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response.... "$1" gets the first afrg, -s means silent mode, wc for getting len and -c for chars
curl -s "$1" | wc -c
