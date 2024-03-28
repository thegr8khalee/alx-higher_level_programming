#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response... -s for silent, X for method
curl -sX DELETE "$1"
