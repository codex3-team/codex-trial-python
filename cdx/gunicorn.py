import multiprocessing
from os import environ

bind = '0.0.0.0:' + environ.get('PORT', '80')
workers = multiprocessing.cpu_count()
