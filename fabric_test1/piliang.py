from fabric.api import run,env,sudo,execute

env.hosts=['root@192.168.1.144:22']
env.password='123456'

def host_type(comm):
    return run(comm)