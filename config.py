#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TamilFusion1


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2085963018:AAELvrbWMfeJWk-r7lG91E0bc2sKspMaGqw")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "3264079"))
    API_HASH = os.environ.get("API_HASH", "41d88a8a4319ad19f451a8ca47d2e37f")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "926195542").split())
    
