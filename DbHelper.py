#!/usr/bin/env python3
# coding=utf-8

import sqlite3
import threading
from Global import *
import datetime

class DbHelper:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(DbHelper, "_instance"):
            with DbHelper._instance_lock:
                if not hasattr(DbHelper, "_instance"):
                    DbHelper._instance = object.__new__(cls)
                    DbHelper._instance.__connect_database()
        return DbHelper._instance

    def __connect_database(self):
        self.db_path = TARGET_DATABASE_PATH
        self.__connection = sqlite3.connect(self.db_path)
        self.__cursor = self.__connection.cursor()

    def insert(self, table, data_list):
        '''
        :param table: table name
        :param data_list: [{col1:val1, col2:val2, ...}, ...]
        :return:
        '''
        if not data_list or not len(data_list):
            return False

        sql_template = '''INSERT INTO %s(%s) VALUES (%s)'''

        try:
            for data in data_list:
                column = tuple(data.keys())
                sql = sql_template % (table, ', '.join(column), ', '.join(['?']*len(column)))

                task = [data[key] for key in column]
                # print(sql)
                # print(task)
                self.__cursor.execute(sql, task)
            self.__connection.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def update(self, table, data_list):
        '''
        :param table:
        :param data_list: [[{(update)col1:val1, col2:val2, ...},{(condition)col1:val1, col2:val2, ...}], ...]
        :return:
        '''
        if not data_list or not len(data_list):
            return False

        sql_template = '''UPDATE %s SET %s WHERE %s'''
        try:
            for data in data_list:
                update_column = tuple(data[0].keys())
                condition_column = tuple(data[1].keys())

                sql = sql_template % (table, ', '.join(['%s = ?' % col for col in update_column]), ' and '.join(['%s = ?' % col for col in condition_column]))
                task = ([data[0][key] for key in update_column] + [data[1][key] for key in condition_column])
                self.__cursor.execute(sql, task)
            self.__connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, sql):
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except Exception as e:
            print(e)
            return None

    def close_db(self):
        if not self.__cursor:
            self.__cursor.close()
            self.__cursor = None
        if not self.__connection:
            self.__connection.close()
            self.__connection = None

    def __del__(self):
        if not self.__connection or not self.__cursor:
            self.close_db()


if __name__ == "__main__":
    db = DbHelper()

    # print(db.insert('member', [Member('1', '2', '3').get_model()]));
    data = db.select("SELECT FileID, AliasTarget, AliasTarget_L from files")
    update_list = []
    for row in data:
        update_list.append([{"AliasTarget": row[1].replace("G:", "D:", 1), "AliasTarget_L": row[2].replace("g:", "d:", 1)}, {"FileID": row[0]}])
        break

    print(db.update("files", update_list))
    print(update_list)