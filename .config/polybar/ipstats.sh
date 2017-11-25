#!/bin/bash

ip -s -h -c -4 addr show enp3s0 | grep --o '[[0-9]\{1,3\}]\?\.\?[0-9]\{1,3\}[k|M|G]' | head -1
