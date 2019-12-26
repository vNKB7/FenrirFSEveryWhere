#!/usr/bin/env python3
# coding=utf-8

from DataCopy import *
from UpdateDatabase import *
from UpdateFile import *

CopyDatabase()
CopyAliasFiles()
UpdateFiles()
UpdateDatabase()
