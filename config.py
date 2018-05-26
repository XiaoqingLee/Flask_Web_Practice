#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "A string you can never guess right"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky] '
    FLASKY_MAIL_SENDER = 'Flasky Admin <xiaoqinglee@foxmail.com>'
    FLASKY_ADMIN = "xiaoqinglee@foxmail.com"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_STL = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "xiaoqinglee@foxmail.com"
    with open('./mail_password.txt', 'r', encoding='utf8') as pw_file:
        MAIL_PASSWORD = pw_file.read()
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
