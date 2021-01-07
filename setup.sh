#!/bin/sh

( pip install --upgrade pip                                   || \
  pip3 install --upgrade pip                                  || \
  python -m pip install --upgrade pip                         || \
  python3 -m pip install --upgrade pip )                      && \
( pip install --no-cache-dir -r requirements.txt              || \
  pip3 install --no-cache-dir -r requirements.txt             || \
  python -m pip install --no-cache-dir -r requirements.txt    || \
  python3 -m pip install --no-cache-dir -r requirements.txt ) && \
( pip install --no-cache-dir -e HTML                          || \
  pip3 install --no-cache-dir -e HTML                         || \
  python -m pip install --no-cache-dir -e HTML                || \
  python3 -m pip install --no-cache-dir -e HTML )

nbstripout --install --attributes .gitattributes

mkdir data
mkdir outputs

wget -c -i dataset.txt -P ./data
