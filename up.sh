#!/bin/bash
apt update && apt full-upgrade -y && apt install --fix-missing -y  && apt install --fix-broken -y && apt autoremove -y &&  updatedb

