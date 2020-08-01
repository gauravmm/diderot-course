FROM ubuntu:18.04
ARG notebook
ENV NOTEBOOK ${notebook}
WORKDIR /app

# git
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN apt update
RUN apt upgrade -yq
RUN apt install -yq python3 python3-pip python3-numpy python3-scipy python3-matplotlib git
RUN pip3 install --upgrade pip
RUN pip3 install torch==1.3.1+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./* /app/
# Grader requirements
RUN pip3 install -r grader-requirements.txt

# Disable inline tests:
ENV DISABLE_TESTING=1
CMD sh -c "(cd /app; make)"
