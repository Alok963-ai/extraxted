#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "c")
    API_ID = int(os.environ.get("API_ID", "296"))
    API_HASH = os.environ.get("API_HASH", "67a684286baa34cb")
    AUTH_USERS = "7903596276"

