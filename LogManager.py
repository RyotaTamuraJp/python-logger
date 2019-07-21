#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:15:34 2019

@author: ryota_tamura
"""

from logging import getLogger, StreamHandler, Formatter, DEBUG, FileHandler


class LogManager:
    def __init__(self, parent_name='Log', output_path=None):
        self.logger = getLogger(parent_name)
        self.logger.setLevel(DEBUG)
        self.stream_handler = StreamHandler()
        self.stream_handler.setLevel(DEBUG)
        self.handler_format = Formatter(
            '%(asctime)s / %(name)s / %(levelname)s / %(message)s'
        )
        self.stream_handler.setFormatter(self.handler_format)
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        self.logger.addHandler(self.stream_handler)
        if output_path:
            self.file_handler = FileHandler(filename=output_path)
            self.file_handler.setLevel(DEBUG)
            self.file_handler.setFormatter(self.handler_format)
            self.logger.addHandler(self.file_handler)

    def get_child_logger(self, child_name):
        return self.logger.getChild(child_name)
