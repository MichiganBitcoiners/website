"""
Tools for deploying the michiganbitcoiners website.
"""

from fabric.api import local, sudo, env, settings
import fabfile_env

env.hosts = fabfile_env.HOSTS

def commit_changes():
    with settings(warn_only=True):
        local('git commit')
        local('git push')

def pull_changes_to_server():
    sudo('cd %s && git pull -u' % fabfile_env.DIRECTORY, user=fabfile_env.USER)
    sudo('cd %s && lessc css/style.less css/style.css' % fabfile_env.DIRECTORY,
         user=fabfile_env.USER)
    sudo('cd %s && python productionize_html.py < index.dev.html > index.html' %
         fabfile_env.DIRECTORY, user=fabfile_env.USER)

def deploy():
    commit_changes()
    pull_changes_to_server()
