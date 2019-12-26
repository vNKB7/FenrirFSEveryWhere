#!/usr/bin/env python3
# coding=utf-8

import os
import shutil
from Global import *
from DbHelper import *

def UpdateDatabase():
    db = DbHelper()
    Update_table_files(db)


def Update_table_files(db):
    data = db.select("SELECT FileID, AliasTarget, AliasTarget_L from files")
    update_list = []
    for row in data:
        update_list.append([{"AliasTarget": row[1].replace("G:", "D:", 1), "AliasTarget_L": row[2].replace("g:", "d:", 1)}, {"FileID": row[0]}])

    db.update("files", update_list)

if __name__ == "__main__":
    UpdateDatabase()