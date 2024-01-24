#!/bin/bash

epoch_to_human_readable() {
    epoch_time=$1
    if [[ $epoch_time =~ ^[0-9]+$ ]]; then
        # Convert epoch time to human-readable format in UTC
        utc_time=$(date -u -d @"$epoch_time" '+%Y-%m-%d %H:%M:%S UTC')

        # Convert epoch time to human-readable format in EST
        est_time=$(TZ="America/New_York" date -d @"$epoch_time" '+%Y-%m-%d %H:%M:%S %Z')

        echo "UTC time: $utc_time"
        echo "EST time: $est_time"
    else
        echo "Error: Invalid epoch time format."
    fi
}

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <epoch_time>"
else
    epoch_to_human_readable "$1"
fi
