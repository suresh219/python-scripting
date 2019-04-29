import subprocess
subprocess.call('docker container ls | grep catalina.sh | cut -d " " -f 1 >file4',shell=True)
container=open("/root/file4",'r').readlines()
i=0
while i<len(container):
    cont_id=container[i]
    subprocess.call("docker rm -f %s"%cont_id,shell=True)
    i=i+1
