#!/bin/sh

/var/health-checker --listener 0.0.0.0:${HC_LISTEN_PORT} --singleflight --script /var/health.sh