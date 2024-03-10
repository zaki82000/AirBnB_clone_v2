#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of my AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from fabric import Connection
import os
from os.path import exists
from fabric import env
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static directory.

    Returns:
        str: Path to the generated archive file if successful, None otherwise.
    """
    # Create the folder versions if not exists
    local("mkdir -p versions")
    # Create the file with date format
    date = datetime.now()
    date_format = date.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_format)
    # Compress file
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Args:
        archive_path (str): The path to the archive file to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    env.hosts = ['35.153.67.162', '34.239.254.62']

    if not exists(archive_path):
        return False

    c = Connection('ubuntu@35.153.67.162')
    local_path = archive_path
    remote_path = '/tmp/'
    c.put(local=local_path, remote=remote_path)
    remote_filename = os.path.splitext(os.path.basename(archive_path))[0]

    c.run(f'tar -xvf {remote_path}{remote_filename}.tgz '
          f'-C /data/web_static/releases/{remote_filename}')
    c.run(f'rm {remote_path}{remote_filename}.tgz')
    c.run("rm -f /data/web_static/current")
    c.run(f'ln -s /data/web_static/releases/{remote_filename} '
          f'/data/web_static/current')

    return True
