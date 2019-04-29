FROM ubuntu
MAINTAINER suresh
USER root
RUN apt-get update
RUN apt-get install -y git maven sudo
RUN apt-get install -y openjdk-8-jdk
ADD http://mirrors.jenkins.io/war-stable/latest/jenkins.war /
ENTRYPOINT ["java","-jar","jenkins.war"]


