# keras-yolo3

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A Keras implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).

This (ckhung's) repo is forked from [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).
I added yolo_image.py to process image files in batch.
```
python3 yolo_image.py --outdir /some/dir *.jpg
```
My test env is built on the docker image gw000/keras:2.1.4-py3-tf-cpu
running on a cpu-only machine.
See the Dockerfile for dependencies.

For more complete doc, see the original repo.

