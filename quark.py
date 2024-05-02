#coding: utf-8
from flask import Flask
from service.detect import Detect

if __name__ == "__main__":
    Detect.train()