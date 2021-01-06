# srt.py
# Some functions for making dealing with SRT data a little easier.

import re
import numpy as np
from astropy.time import Time
from astropy.coordinates import SkyCoord, ICRS
import astropy.units as u

def extract_metadata(filename):
    """
    Extract all of the meta data contained within the name of a data file.
    
    Parameters
    ----------
    filename : str
        The name of the file, can optionally include the full path, 
        in which case the name is taken to be everything after the final
        slash.
        
    Returns
    -------
    position : `astropy.skycoord`
        The sky position at which the file starts
    time : `astropy.Time`
        The time at which the file starts.
    """
    
    a = re.compile("ra(.*)dec(.*)time(.*).dat")
    filepath = filename.split('/')

    s_ra = float(a.search(filepath[-1]).group(1))
    s_dec = float(a.search(filepath[-1]).group(2))
    s_time = a.search(filepath[-1]).group(3)
    
    
    time = Time(s_time, format='isot', scale='utc')
    position = SkyCoord(s_ra*u.deg, s_dec*u.deg, frame=ICRS, obstime = time)
    return position, time
    
def read_data(filename, spec_len=256):
    """
    Read-in the data from an SRT data file.
    
    Parameters
    ----------
    filename : str
        The name of the file, can optionally include the full path, 
        in which case the name is taken to be everything after the final
        slash.
    spec_len  : int
        The length of each spectrum. Defaults to 256.
        
    Returns
    -------
    data : `numpy.ndarray`
        A 2D numpy array of spectral data.
    position : `astropy.coordinates.SkyCoord`
        The position of the first spectrum on the celestial sphere.
    time : `astropy.time.Time`
        The start time of the first spectrum in the data set.
    """
    
    data = np.fromfile(filename, dtype=np.float32)
    data = np.reshape(data, [-1,spec_len])
    position, time = extract_metadata(filename)
    
    return data, position, time