#!/bin/bash
# Alta3 Research | RZFeeser
# SOLUTION 01 - How quickly can we get to 50 requests (per hour) to be rate limited
# by FlaskLimiter? Run the script to get results.

URI="http://localhost:2224/"
start_time=$(date +%s)
end_time=0

# start an infinite loop
while true; do
    response_code=$(curl -s -o /dev/null -w "%{http_code}" "${URI}fast")  # this URI is limited by 50 lookups per hour
    if [[ $response_code != 200 ]]; then
        end_time=$(date +%s)
        break  # stop looping, as we have hit the limit
    fi
done

# display the total time it took to perform the lookups
echo "To reach the limit of /fast, it took $((end_time - start_time)) seconds"
