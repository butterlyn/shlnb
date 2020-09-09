"""
This module is aimed at signal analysis and beamforming of data (.wav format) from microphones in a ULA configuration.

This package contains the following functions :
    find_extrema(wavform_data, maxima_or_minima) : 
        Finds the values of the maximas or the minimas (and their index locations) of a given sinusoidal waveform passed as a 1D numpy array.
    
And the following classes :
    Nil
"""

from pyargus.antennaArrayPattern import array_rad_pattern_plot
import pyargus.beamform as bf
import pyargus.tests.beamformTest as bft
from pyargus.tests.patternPlotTest import demo_ULA_plot, demo_UCA_plot
import matplotlib.pyplot as plt
import numpy as np

def find_extrema(waveform_data : '1D numpy array', maxima_or_minima = 'maxima' : 'str'):
    """
    Finds the values of the maximas or the minimas (and their index locations) of a given sinusoidal waveform passed as a 1D numpy array.

    Parameters
    ----------
    waveform_data : 1D numpy array
        Sinusoidal waveform to be analysed
    maxima_or_minima : {'maxima', 'minima'}
        Specify (as a string) whether to find the maximas or minimas of the sinusoidal waveform. (default: 'maxima')

    Returns
    -------
    extrema : 2D numpy array
        Numpy array of extrema index locations and corresponding values

    Examples
    --------
    >>> waveform = np.sin(np.linspace(0,10*np.pi,1000))
    >>> extrema = find_extrema(waveform, 'minima')
    >>> plt.plot(waveform, '-D', markevery = extrema[0])
    """
    # Check if sample is greater than or equal to 2 samples to the left and two samples to the right. Store in bool array
    
    if maxima_or_minima = 'maxima':
        extrema_map = np.r_[data[2:] <= data[:-2],False,False] &\
                    np.r_[data[1:] <= data[:-1],False] &\
                    np.r_[False,data[:-1] <= data[1:]] &\
                    np.r_[False,False,data[:-2] <= data[2:]]
    elif maxima_or_minima = 'minima':
        extrema_map = np.r_[data[2:] >= data[:-2],False,False] &\
            np.r_[data[1:] >= data[:-1],False] &\
            np.r_[False,data[:-1] >= data[1:]] &\
            np.r_[False,False,data[:-2] >= data[2:]]
    else:
        raise ValueError("maxima_or_minima arument must be the string 'maxima' or 'minima'")

    # When a local maxima occurs twice consecutively, only count the first one
    extrema_map = extrema_map & np.diff(np.r_[False,extrema_map])

    # Identify when an extrema has been counted twice and remove duplicates
    extrema_index = np.where(extrema_map)[0]
    extrema_spacing = np.diff(extrema_index) # Find the spacing between extremas
    outliers_map = np.r_[True ,abs(extrema_spacing - np.mean(extrema_spacing)) < 3 * np.std(extrema_spacing)] # filter out outliers outside three standard deviations
    extrema_index = extrema_index[outliers_map] # Remove outliers

    # Find values of extrema
    extrema_values = data[extrema_index]
    
    # Store results in a 2D numpy array
    extrema = np.array([extrema_index, extrema_values])
    return extrema


