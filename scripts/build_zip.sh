#!/bin/bash
#
# Build the zip file to upload to lambda
#
# NOTE: This script expects to be run from the project root with
# ./scripts/build_zip.sh
mkdir -p build

docker build -t python-lambda .

rm build/fixerio_scrape.zip || true

id=$(docker create python-lambda)
docker cp $id:/fixerio_scrape/fixerio_scrape.zip ./build/fixerio_scrape.zip
docker rm -v $id
