#!/usr/bin/env python
# coding: utf-8

import os
import io
import re
import sys
import json
from os.path import dirname



def load_json(path):
    with open(path, "r") as file:
        text = file.read()
        out = json.loads(text)
        if out:
            return out
        else:
            sys.stdout.write("Error in reading transriptions from file.")
            return None
