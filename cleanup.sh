#!/bin/bash

# enable dry run unless -f is passed

DRY_RUN=1

while getopts "f" opt; do
    case $opt in
        f)
            DRY_RUN=0
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac
done

# If dry run, print what would be done

if [ $DRY_RUN -eq 1 ]; then
    echo "Dry run: would delete README files"
    echo "find . -name "README" -exec rm {} \;"

    echo "Dry run: would move python files"
    echo "find python -name "*.py" -exec mv {} . \;"

    echo "Dry run: would move script files"
    echo "find scripts -name "*.sh" -exec mv {} . \;"

    echo "Dry run: would remove python and scripts directories"
    echo "rm -r python scripts"

    echo "Dry run: would remove .git directory"
    echo "rm -r .git"

    echo "Dry run: would remove .gitignore file"
    echo "rm .gitignore"
fi

# If not dry run, actually do it
if [ $DRY_RUN -eq 0 ]; then
    # Remove all README files from the current directory
    echo "Deleting README files"
    find . -name "README.md" -exec rm {} \;

    # Move all python files in the "python" directory to the current directory
    echo "Moving python files"
    find python -name "*.py" -exec mv {} . \;

    # Move all scripts in the "shell" directory to the current directory
    echo "Moving script files"
    find shell -name "*.sh" -exec mv {} . \;

    # Remove the "python" and "scripts" directories
    echo "Removing python and scripts directories"
    rm -r python shell

    # Remove .git directory
    echo "Removing .git directory"
    rm -r .git -y

    # Remove .gitignore file
    echo "Removing .gitignore file"
    rm .gitignore
fi

