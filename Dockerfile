# ASM Codegolf Dockerfile

FROM alpine:3.4
MAINTAINER Danilo Bargen <mail@dbrgn.ch>

# Install dependencies
RUN apk add --no-cache nasm make python3 git

# Clone repository
RUN git clone https://github.com/coredump-ch/codegolf-asm-compass /root/codegolf

# Create non-privileged user
RUN adduser -D -h /home/codegolf -u 9987 codegolf

# Copy necessary verification files to user home
RUN cp /root/codegolf/Makefile /root/codegolf/test.py /home/codegolf && \
    chown root:codegolf /home/codegolf/* && \
    chmod 440 /home/codegolf/Makefile && \
    chmod 440 /home/codegolf/test.py

# Delete other files
RUN rm -r /root/codegolf

# Change user and workdir
USER compass
WORKDIR /home/compass

# Create volume for code
VOLUME /code
