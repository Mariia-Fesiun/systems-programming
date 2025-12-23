FROM jenkins/ssh-agent:latest

RUN apt-get update && apt-get install -y \
    git \
    bash \
    rpm \
    dpkg-dev \
    fakeroot \
    alien \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/jenkins/.ssh

COPY agent_key.pub /home/jenkins/.ssh/authorized_keys

RUN chown -R jenkins:jenkins /home/jenkins/.ssh && \
    chmod 700 /home/jenkins/.ssh && \
    chmod 600 /home/jenkins/.ssh/authorized_keys