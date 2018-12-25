import sys
sys.path.append('../../software/models/')
from dftModel import dftAnal, dftSynth
from scipy.signal import get_window
import matplotlib.pyplot as plt
import numpy as np
import copy
"""
A3-Part-4: Suppressing frequency components using DFT model

"""
def suppressFreqDFTmodel(x, fs, N):
    """
    Inputs:
        x (numpy array) = input signal of length M (odd)
        fs (float) = sampling frequency (Hz)
        N (positive integer) = FFT size
    Outputs:
        The function should return a tuple (y, yfilt)
        y (numpy array) = Output of the dftSynth() without filtering (M samples long)
        yfilt (numpy array) = Output of the dftSynth() with filtering (M samples long)
    The first few lines of the code have been written for you, do not modify it. 
    """
    M = len(x)
    w = get_window('hamming', M)
    outputScaleFactor = sum(w)

    (mX, pX) = dftAnal(x, w, N)
    mXnew = mX.copy()
    index = int(np.ceil((70.0 * N)/ float(fs)))
    for i in range(index):
        if i < N:
            mXnew[i] = -120
    y = dftSynth(mX, pX, M)
    yFilt = dftSynth(mXnew, pX, M)

    return outputScaleFactor * y, outputScaleFactor * yFilt
    
    ## Your code here
