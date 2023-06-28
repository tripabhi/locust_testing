#!/bin/bash

source venv/bin/activate

pip install -r requirements.txt

locust --config master.conf