#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   class_intro.py
@Time    :   2023/03/02 13:58:01
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Introduction to classes a simple example of a Robot class
'''

class Robot:
    def __init__(self, name=None, model=None, version=None):
        self.name = name
        self.model = model
        self.version = version

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name.")

x = Robot()
y = Robot("Marvin", "UB42", "1.0")
x.say_hi()
y.say_hi()
