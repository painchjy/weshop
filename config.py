#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

WECHAT_TOKEN = os.environ.get('WECHAT_TOKEN') or 'hard to guess string'
WECHAT_ENCODING_AES_KEY = os.environ.get('WECHAT_ENCODING_AES_KEY') or 'hard to guess string'
WECHAT_APPID = os.environ.get('WECHAT_APPID') or 'hard to guess string'
WECHAT_SECRET = os.environ.get('WECHAT_SECRET') or 'hard to guess string'
WECHAT_MENU_FILE = os.path.join(basedir, 'weapp/static/wechat_menu.json')

TULING_APIKEY = os.environ.get('TULING_APIKEY') or '123'

WECHAT_WELCOME_MSG = '''
     能聊天，能识别图片人物年龄，
     能解析语音，能讲笑话
     上知天文下知地理，学富五车才高八斗
     --------------------------
     来来来，帮你排忧解难。。。
     http://www.baidu.com
    '''


class Config(object):
    SECRET_KEY = os.urandom(24)
    BOOTSTRAP_SERVE_LOCAL = True

    WTF_CSRF_SECRET_KEY = os.urandom(24)

    @classmethod
    def init_app(cls, app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class PrdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-prd.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'default': DevConfig
}
