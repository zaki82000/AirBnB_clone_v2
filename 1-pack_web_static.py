#!/usr/bin/python3
"""
generates a .tgz archive from web_static dir
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from web_static dir
    """
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(date)
    if local(
        'mkdir -p versions && tar -czvf {} web_static/'.format(path)
    ).succeeded:
        return path
    else:
        return None
