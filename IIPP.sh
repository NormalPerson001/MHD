#!/bin/bash


# Check if an argument (IP address) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <IP address>"
    exit 1
fi

# Perform the ping command silently
ping -c 1 -q "$1" > /dev/null 2>&1

# Check the exit status of the ping command
if [ $? -eq 0 ]; then
    exit 0  # Exit with code 0 if host is alive
else
    exit 1  # Exit with code 1 if host is unreachable or offline
fi
whois $IP
