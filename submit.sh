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

if [ $# -lt 2 ]; then
    echo "Usage: submit <level> <answer>"
    exit 1
fi

curl "https://adventofcode.com/${year}/day/${day}/answer" -H "Cookie: session=$(pass show adventofcode)" --data-raw "level=$1&answer=$2"
