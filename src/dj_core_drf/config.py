from __future__ import absolute_import, print_function, unicode_literals

from os import path

from dj_core.config import Config as BaseConfig


class Config(BaseConfig):
    def get_installed_apps(self, settings):
        return super(Config, self).get_installed_apps(settings) + [
            'rest_framework',
            'rest_framework.authtoken',
            'rest_framework_swagger',
            'rest_auth',
            'allauth',
            'allauth.account',
            'rest_auth.registration',
            'corsheaders',
            'revproxy',
            'django_filters',
        ]
