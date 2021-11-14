#! /bin/sh

set -e -x

if [ X"${1}" = X"/bin/sh" ]; then
    exec python -m ssh_uptime
else
    exec "${@}"
fi
