#! /bin/bash

# Create directories
mkdir -v "$1/Day_"{1..24}

# Create input files
touch "$1/Day_"{1..24}/input.txt
for i in {1..24}
do
	echo "created file $1/Day_$i/input.txt"
done

# Copy formats
echo "$1/Day_"{1..24} | xargs -n 1 cp -v solution.py 

