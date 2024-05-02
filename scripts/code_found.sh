#!/bin/bash

if command -v code &> /dev/null
then
    code .
else
    echo "vscode could not be found."
fi
