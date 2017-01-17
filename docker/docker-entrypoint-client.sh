#!/bin/bash
cd ../client && npm install
cd ../client && bower install --allow-root
exec "$@"