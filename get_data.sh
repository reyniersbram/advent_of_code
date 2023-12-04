#! /usr/bin/env sh

day=$(date +%-e)
year=$(date +%Y)

panic ()
{
    echo "Usage: get_data [-d day] [-y year]"
    exit 1
}

while getopts ":y:d:" opt; do
    case $opt in
        d)
            day=${OPTARG}
            ;;
        y)
            year=${OPTARG}
            ;;
        *)
            panic
            ;;
    esac
done
shift $((OPTIND - 1))

mkdir -v -p "${year}/day${day}"
curl "https://adventofcode.com/${year}/day/${day}/input" -H "Cookie: session=$(pass show adventofcode.com)" > "${year}/day${day}/input.txt"
