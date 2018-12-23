#!/bin/sh

gunicorn manage:app -b 0.0.0.0:5000 -w 4