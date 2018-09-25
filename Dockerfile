FROM gw000/keras:2.1.4-py3-tf-cpu

RUN pip3 install pillow matplotlib opencv-python
RUN apt -y update
RUN apt install -y feh
RUN ln -s /usr/bin/feh /usr/bin/display

