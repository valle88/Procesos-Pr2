import subprocess

p = subprocess.getoutput(['ping -c 5 www.google.es'])
print(p)