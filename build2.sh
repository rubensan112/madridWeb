#!/bin/bash

echo "Eliminate old images"

docker rmi $(docker images -f "dangling=true" -q) --force

echo "Finish"