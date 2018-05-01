# @Author: 陈长富 <ccf>
# @Date:   2018-04-10T20:25:54+08:00
# @Email:  ccfwwm@gmail.com
# @Filename: const.py
# @Last modified by:   ccf
# @Last modified time: 2018-04-10T22:26:57+08:00
# @License: MIT



# encoding: UTF-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import os


class Constant(object):
    conf_dir = os.path.join(os.path.expanduser('~'), '.netease-musicbox')
    download_dir = os.path.join(conf_dir, 'cached')
    config_path = os.path.join(conf_dir, 'config.json')
    storage_path = os.path.join(conf_dir, 'database.json')
    cookie_path = os.path.join(conf_dir, 'cookie')
    log_path = os.path.join(conf_dir, 'musicbox.log')
