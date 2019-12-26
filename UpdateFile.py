#!/usr/bin/env python3
# coding=utf-8

import os
import shutil
from Global import *
import fileinput

def UpdateFiles():
    for file_name in os.listdir(TARGET_FILE_DIR):
        file_path = os.path.join(TARGET_FILE_DIR, file_name)
        lines = []
        with open(file_path, 'r', encoding='utf16') as read_file:
            for line in read_file:
                lines.append(line)
        if len(lines) > 0:
            lines[0] = lines[0].replace('Target=G', 'Target=D')

        with open(file_path, 'w', encoding='utf16') as write_file:
            for line in lines:
                write_file.write(line)

