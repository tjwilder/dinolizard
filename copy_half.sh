#!/bin/bash

i=0
for x in trex/*; do
  if [ "$i" -lt 495 ]; then continue; fi
  mv -- "$x" trex_half2/
  i=$((i+1))
done
