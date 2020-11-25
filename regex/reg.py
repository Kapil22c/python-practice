# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:19:24 2020

@author: Kapil
"""


import re
handle = open('regex_sum.txt')
count = list()
summ = 0
for line in handle:
    stuff = re.findall('[0-9]+',line)
    
    for number in stuff:
        summ = int(summ)+int(number)
print(summ)