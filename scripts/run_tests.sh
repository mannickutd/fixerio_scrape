#!/bin/bash
#
# Run project unit tests
#
# NOTE: This script expects to be run from the project root with
# ./scripts/run_tests.sh

set -o pipefail

source environment_for_test.sh

function display_result {
  RESULT=$1
  EXIT_STATUS=$2
  TEST=$3

  if [ $RESULT -ne 0 ]; then
    echo -e "\033[31m$TEST failed\033[0m"
    exit $EXIT_STATUS
  else
    echo -e "\033[32m$TEST passed\033[0m"
  fi
}

pylint fixerio_scrape
display_result $? 1 "Python code style check"

alias py.test3='python3 -m pytest'

py.test --cov=fixerio_scrape --cov-report=term-missing tests/ scripts/
display_result $? 2 "Python unit tests"