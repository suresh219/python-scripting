import subprocess
i=1
while i<=10:
    subprocess.call("docker run -P -d --name t%d tomcat"%i,shell=True)
    i=i+1

