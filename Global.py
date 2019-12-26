#!/usr/bin/env python3
# coding=utf-8

import os

# PATH
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SOURCE_PATH="F:\code\FenrirFSEveryWhere\comic.profile"
'''
./db/FenrirFS.db
./files
'''
TARGET_PATH=os.path.join(BASE_PATH, "target")
SOURCE_DATABASE_PATH = os.path.join(SOURCE_PATH, "db/FenrirFS.db")
SOURCE_FILE_DIR = os.path.join(SOURCE_PATH, "files")
TARGET_DATABASE_DIR = os.path.join(TARGET_PATH, "db")
TARGET_DATABASE_PATH = os.path.join(TARGET_DATABASE_DIR, "FenrirFS.db")
TARGET_FILE_DIR = os.path.join(TARGET_PATH, "files")


if __name__ == "__main__":
    print(TARGET_PATH)
    print(SOURCE_DATABASE_PATH)
    print(TARGET_DATABASE_DIR)
    print(TARGET_DATABASE_PATH)
    print(TARGET_DATABASE_DIR)
