#!/usr/bin/env python3

import yaml
import os
import sys

if os.path.exists("snapcraft.yaml"):
    filename = "snapcraft.yaml"
elif os.path.exists("snap/snapcraft.yaml"):
    filename = "snap/snapcraft.yaml"
else:
    print("Can't find snapcraft.yaml file")
    sys.exit(1)

with open(filename,"r") as f:
    data = yaml.load(f, Loader=yaml.Loader)

parts = ""
for part in data["parts"]:
    parts += f" {part}"

os.system(f"snapcraft clean {parts}")
