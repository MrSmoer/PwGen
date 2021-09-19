#!/bin/bash
cd `dirname $0`
SCRIPTDIR=`pwd`
cd -
python3 $SCRIPTDIR/PwGen.py $*
