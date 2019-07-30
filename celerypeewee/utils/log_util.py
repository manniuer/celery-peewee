#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :Copyright: 2018, BBD Tech. Co.,Ltd.
    :File Name: log_util.py
    :Description: 
    :Author: liulongjun@bbdservice.com
    :Date: 19-1-5
    :Version: v.1.0
"""
import sys
import logging
from loguru import logger


es_logger = logging.getLogger('elasticsearch')
es_logger.setLevel(logging.CRITICAL)


def get_logger(*args):
    logger.remove()
    logger.add(sys.stdout, format="{time}|{level}|{file}|{function}:{line}|{message}|", level="INFO")
    return logger

