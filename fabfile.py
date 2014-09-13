"""
Tools for deploying the michiganbitcoiners website.
"""

from fabric.api import local, sudo, env, settings

env.hosts = ['goldmoth.com']

def makecss():
    local('lessc css/style.less css/style.css')

def productionize():
    local('python productionize_html.py < index.dev.html > index.html')

def commit_changes():
    with settings(warn_only=True):
        local('hg commit')
        local('hg push')

def deploy():
    makecss()
    productionize()
    commit_changes()
