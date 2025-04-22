#!/bin/bash
# Usage: ./new_day.sh DAY_NUMBER
if [ -z "$1" ]; then
  echo "Usage: $0 DAY_NUMBER"
  exit 1
fi

DAY=$(printf "%02d" "$1")
DIR="Day${DAY}"
if [ -d "$DIR" ]; then
  echo "Directory $DIR already exists."
  exit 1
fi

mkdir "$DIR"
sed "s/DD/$DAY/g" template.md > "$DIR/README.md"
echo "Created $DIR/README.md"
