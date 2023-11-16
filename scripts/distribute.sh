#!/bin/bash
# * Shell script to distribute latest wheel file

clear

file=$(ls dist/*.whl -Art | tail -n 1)
echo "Distributing: $file to..."

# Example
# cp "$file" ~/_JT/jt-mdm/redist
# echo ~/_JT/jt-mdm/redist
