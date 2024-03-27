#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response... -s forsilent mode, -L for redirect
curl -sL "$1"
