from fabric.api import *


def make():
    local('make html')
    
def deploy():
    local('rm -rf _s*')
    local('mv -f html/* .')
    local('git commit -a')
    local('git push')
    