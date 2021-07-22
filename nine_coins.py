#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
class Nine_Coins:
    def __init__(self,num):
        self.num = num
    def toss(self):
        self.num = random.randint(0,511)
    def __repr__(self):
        binary_num = "{:09b}".format(self.num)     # 把數字轉成9bits的2進位數字存起來
        binary_str = str(binary_num)               # 把2進位數字轉成字串存起來
        binary_str = binary_str.replace("0","H")   # 把字串中的"0"都替換成"H"
        binary_str = binary_str.replace("1","T")
        return 'Nine_Coins: '+binary_str+''
    def __str__(self):
        return f'binary: {"{:09b}".format(self.num)} and decimal: {self.num}'

