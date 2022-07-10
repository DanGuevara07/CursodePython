# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:30:49 2022

@author: LENOVO
"""
from math import pi

def areatriangulo(base, altura):
    return (base*altura)/2

def areacirculo(radio):
    return pi * (radio**2)

print(areatriangulo(10, 5))
print(areacirculo(6))