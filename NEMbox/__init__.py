# @Author: 陈长富 <ccf>
# @Date:   2018-04-10T20:25:54+08:00
# @Email:  ccfwwm@gmail.com
# @Filename: __init__.py
# @Last modified by:   ccf
# @Last modified time: 2018-04-11T22:22:42+08:00
# @License: MIT



#!/usr/bin/env python
# encoding: UTF-8
'''
网易云音乐 Entry
'''
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()

import curses
import traceback
import argparse
import sys

from .menu import Menu
version = "0.2.4.0"


def start():
    nembox_menu = Menu()
    try:
        nembox_menu.start_fork(version)
    except (OSError, TypeError, ValueError, KeyError):
        # clean up terminal while failed
        nembox_menu.screen.keypad(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()


if __name__ == '__main__':
    start()

parser = argparse.ArgumentParser()
parser.add_argument("-v",
                    "--version",
                    help="show this version and exit",
                    action="store_true")
args = parser.parse_args()
if args.version:
    latest = Menu().check_version()
    curses.endwin()
    print('NetEase-MusicBox installed version:' + version)
    if latest != version:
        print('NetEase-MusicBox latest version:' + str(latest))
    sys.exit()
