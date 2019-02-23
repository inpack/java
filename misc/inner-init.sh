#!/bin/bash

set -e

SCRIPT_PATH=$(readlink -f $0)

export JAVA_HOME=`dirname $SCRIPT_PATH`

if [ ! -d $GOPATH ]; then
  mkdir -p $GOPATH
fi

/home/action/.sysinner/inagent confrender --in ${JAVA_HOME}/misc/profile.d_java.sh --out /home/action/local/profile.d/java.sh --var__inpack_prefix_java ${JAVA_HOME}

