#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843532886:AAEKhbnb-61xATKee49vLVop8dJB4uVGsHc")
    API_ID = int(os.environ.get("API_ID", "26572696"))
    API_HASH = os.environ.get("API_HASH", "67a8947a3e1b15f9ef9684286baa34cb")
    AUTH_USERS = "7903596276"

