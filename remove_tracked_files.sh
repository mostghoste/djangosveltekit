#!/bin/bash

# Remove files from git tracking but keep them locally
git rm -r --cached .
git add .
git commit -m "Remove files that should be ignored"
