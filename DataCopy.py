#!/usr/bin/env python3
# coding=utf-8

import os
import shutil
from Global import *

def CopyDatabase():
    # check path
    if not os.path.exists(SOURCE_DATABASE_PATH):
        raise Exception("The source database path '%s' is not there" % SOURCE_DATABASE_PATH)

    if os.path.exists(TARGET_DATABASE_PATH):
        raise Exception("The target database path '%s' has already been created" % TARGET_DATABASE_PATH)

    # create target dir if not exists
    if not os.path.exists(TARGET_DATABASE_DIR):
        os.makedirs(TARGET_DATABASE_DIR)

    #copy db
    shutil.copyfile(SOURCE_DATABASE_PATH, TARGET_DATABASE_PATH)

def CopyAliasFiles():
    # check path
    if not os.path.exists(SOURCE_FILE_DIR):
        raise Exception("The source file dir '%s' is not there" % SOURCE_FILE_DIR)

    if os.path.exists(TARGET_FILE_DIR):
        if len(os.listdir(TARGET_FILE_DIR)) > 0:
            raise Exception("The target file dir '%s' have already had some files" % SOURCE_FILE_DIR)
    else:
        os.makedirs(TARGET_FILE_DIR)

    # copy files
    for file_name in os.listdir(SOURCE_FILE_DIR):
        shutil.copyfile(os.path.join(SOURCE_FILE_DIR, file_name), os.path.join(TARGET_FILE_DIR, file_name))


if __name__ == "__main__":
    CopyAliasFiles()
