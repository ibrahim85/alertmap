#!/usr/bin/env python

import numpy as np
from scipy import interpolate

class TravelTimeCalculator(object):
    def __init__(self):
        homedir = os.path.dirname(os.path.abspath(__file__)) #where is this script?
        ttimefile = os.path.join(homedir,'ttimes.csv')
        data = np.loadtxt(ttimefile,delimiter=',',skiprows=1)
        self.fp = interpolate.interp1d(data[:,0],data[:,1])
        self.fs = interpolate.interp1d(data[:,0],data[:,2])

    def getTravelTimes(distance):
        ptime = fp(distance)
        stime = fs(distance)
        return (ptime,stime)

    