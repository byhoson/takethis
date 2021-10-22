#!/usr/bin/env bash
PROJECT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd ../ && pwd)"
rm $PROJECT_HOME/.cache/*
