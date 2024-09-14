import os

stream = os.popen('uname')
output = stream.read()

if output.strip() == "Linux":
    os.system("df -h && lscpu && whoami && free -h && pwd")
    os.system("apt update")
    os.system("mkdir -p ~/bin")
    os.system("curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && chmod a+x ~/bin/repo")
    os.system("PATH='$HOME/bin:$PATH'")
