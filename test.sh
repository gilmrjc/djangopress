#!/bin/bash
coverage erase
tox --skip-missing
coverage combine
coverage report
