
#Created by Deepak Sharma (emaildeepaksharma@gmail.com)
#Version 1 created on Jul, 5, 2017

import numpy as np
import os, xlrd, csv
from math import radians, cos, sin, asin, sqrt
from collections import Counter
import string
import json
from datetime import datetime as dt
from datetime import timedelta
import pandas as pd
import sys

#import logging
#import matplotlib.pyplot as plt

def factors(n): # generator that computes factors
    k=1
    tempK = []
    while k*k < n: # while k < sqrt(n)
        if n % k == 0:
            tempK.append(k)
            yield k
            #yield n // k
        k += 1
        if k*k == n: # special case if n is perfect square
            yield k

    for k in tempK[::-1] :
        yield n//k




if __name__ == "__main__" :

    a = factors(100)

    for i in a :

        print i


