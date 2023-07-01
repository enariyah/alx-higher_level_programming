#!/bin/bash
# This program takes in a URL, sends a request to that URL, and shows the size.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
