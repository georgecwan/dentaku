from util import github
import time
import subprocess
import yaml

github.pull_repo()
config = yaml.load(open("autodeploy.conf"))

p = subprocess.Popen("exec " + "python " + config['run'], stdout=subprocess.PIPE, shell=True)


def restart_app():
    global p
    p.kill()
    p = subprocess.Popen("exec " + "python " + config['run'], stdout=subprocess.PIPE, shell=True)


while True:
    if github.pull_repo():
        print("New commit found. Repository updated.")
        print("Restarting app...")
        restart_app()
    time.sleep(300)
