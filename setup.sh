#!/bin/sh

git config core.hooksPath .githooks

pip install --upgrade pip && \
( pip install --no-cache-dir -r requirements.txt  || \
  pip3 install --no-cache-dir -r requirements.txt || \
  python -m pip install --no-cache-dir -r requirements.txt  || \
  python3 -m pip install --no-cache-dir -r requirements.txt )

wget -c -i dataset.txt -P ./data