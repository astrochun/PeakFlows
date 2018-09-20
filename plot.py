"""
plot
====

Provide description for code here.
"""

import sys, os

from chun_codes import systime

from os.path import exists

import numpy as np

import matplotlib.pyplot as plt

from astropy import log

from pandas import read_excel, to_datetime

def main(silent=False, verbose=True):

    '''
    Main function to plot trends of peak flows

    Parameters
    ----------

    silent : boolean
      Turns off stdout messages. Default: False

    verbose : boolean
      Turns on additional stdout messages. Default: True

    Returns
    -------

    Notes
    -----
    Created by Chun Ly, 2 August 2018
    '''
    
    if silent == False: log.info('### Begin main : '+systime())

    main_file = '/Users/cly/Dropbox/Documents/Personals/Peak_Flows.xls'

    data = read_excel(main_file)

    dates = data['Date'].values
    v1    = data['PF #1'].values
    v2    = data['PF #2'].values
    v3    = data['PF #3'].values

    val = [v1, v2, v3]
    avg_pf = np.average(val, axis=0)

    # data.Date = to_datetime(data['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    # data.set_index(['Date'],inplace=True)

    plt.scatter(dates, avg_pf, edgecolor='none', facecolor='b', alpha=0.5)
    #data['Date'], data['PF #1'])
    #data.plot('Date', 'PF #1') #, xlim=[2016,2019])
    
    if silent == False: log.info('### End main : '+systime())
#enddef
