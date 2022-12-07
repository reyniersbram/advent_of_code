#! /bin/bash

syntaxError() {
	echo "Syntax Error: ./setup.sh [-y <directory>]" 1>&2
	exit 1
}

argumentError () {
	echo "Argument Error: Expected an argument, but none was given" 1>&2
	exit 2
}

year=$(date -u +"%Y")
while getopts ":y:" opt
do
	case $opt in
		y )	year=$OPTARG
			;;
		\?)	syntaxError
			;;
		\:)	argumentError
	esac
done
shift $((OPTIND - 1))

# Create directories
mkdir $year
mkdir -v "$year/Day_"{1..24}

# Create input files
touch "$year/Day_"{1..24}/input.txt
for i in {1..24}
do
	echo "created file $year/Day_$i/input.txt"
done

# Copy formats
echo "$year/Day_"{1..24}/solution.py | xargs -n 1 cp -v template.py 

