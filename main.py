#!/usr/bin/env -S poetry run python

from openrgb import OpenRGBClient
import sys

client = OpenRGBClient()

# set the profile to whatever the input is
client.load_profile(sys.argv[1])