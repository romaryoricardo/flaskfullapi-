# -*- coding: utf-8 -*-

# Python
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or '84012jd83081230d18'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}