import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_strong_key_for_dev'
