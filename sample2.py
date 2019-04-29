import subprocess
subprocess.call('docker images | cut -d " " -f 1 > file2',shell=True)
images = open("/root/file2",'r').readlines()
i=3
while i<len(images):
    image_name=images[i]
    subprocess.call("docker rmi %s"%image_name,shell=True)
    i=i+1

