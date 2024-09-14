#!/bin/bash
source /root/CustomerSupportBor/myenv/bin/activate
nohup python3 /root/CustomerSupportBor/main.py > /dev/null 2>&1 &
