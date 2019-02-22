import subprocess

cmd = subprocess.run('ipconfig',shell=True,stdout=subprocess.PIPE)
print(cmd)