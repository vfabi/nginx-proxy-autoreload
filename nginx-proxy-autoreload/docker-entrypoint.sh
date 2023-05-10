#!/bin/bash


sh -c "configReloader.sh &"
exec "$@"