#!/usr/bin/python3
"""Fabric script that generates a.tgz archive with contents
 from webstatic folder"""

from fabric.api import local
from time import strftime


def do_pack():
    """generates .tgz file"""
    time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None
