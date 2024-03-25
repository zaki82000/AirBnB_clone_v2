#!/usr/bin/python3
"""
distributes an archive to your web server
"""
from os.path import exists
from fabric.api import *
from datetime import datetime

env.user = 'ubuntu'
env.hosts = [
    '54.237.72.179',
    '52.23.245.31'
]


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


def do_deploy(archive_path):
    """
    distributes an archive to your web server
    """
    path = archive_path.split('/')[-1].split('.')[0]

    if not exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    run('mkdir -p /data/web_static/releases/{}'.format(path))
    run(
        'tar -xzvf /tmp/{}.tgz -C /data/web_static/releases/{}'
        .format(path, path)
    )
    run('rm -f /tmp/{}.tgz'.format(path))
    run(
        'mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}'.format(path, path)
    )
    run('rm -f /data/web_static/current')
    run(
        'ln -s /data/web_static/releases/{} \
        /data/web_static/current'.format(path)
    )

    return True
