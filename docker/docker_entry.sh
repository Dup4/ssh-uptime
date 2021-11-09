#! /bin/bash

set -e -x

if [ X"${1}" = X"/bin/bash" ]; then
    exec python -m ssh_uptime
else
    exec "${@}"
fi
