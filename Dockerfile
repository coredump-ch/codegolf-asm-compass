# ASM Codegolf Dockerfile
#
# Version: 1

FROM ubuntu:14.04
MAINTAINER Danilo Bargen <mail@dbrgn.ch>

# Install dependencies
RUN apt-get update
RUN apt-get install -y build-essential make nasm python git

# Create non-privileged user
RUN useradd -b /home -m -s /bin/bash compass
USER compass

# Clone repository
WORKDIR /home/compass
RUN git clone https://github.com/dbrgn/asm-codegolf codegolf

# Create volume for code
VOLUME /code
