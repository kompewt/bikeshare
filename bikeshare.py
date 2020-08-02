# -*- coding: utf-8 -*-
# import functions from the modsim library
from matplotlib import *
from modsim import *

def sweep_p2(p1, p2_array, num_steps):
    global bikeshare
    sweep_series = SweepSeries()
    init_state = bikeshare
    for p2 in p2_array:
        for i in range(num_steps):
            wes = flip(p1)
            oli = flip(p2)
            if wes: # if bike from olin to wellesley
                if bikeshare.olin == 0: # catch unhappy customer
                    bikeshare.olin_empty += 1 # count lost sales
                    continue
                bikeshare.olin -= 1
                bikeshare.wellesley += 1
            if oli: # if bike from wellesley to olin
                if bikeshare.wellesley == 0: # catch unhappy customer
                    bikeshare.wellesley_empty += 1 # count lost sales
                    continue
                bikeshare.olin += 1
                bikeshare.wellesley -= 1
        sweep_series[p2] = bikeshare.wellesley_empty
        bikeshare = init_state

    plot(sweep_series, label='Olin')
    decorate(title='Olin-Wellesley Bikeshare',
             xlabel='Arrival rate at Olin (p1 in customers/min)', 
             ylabel='Number of unhappy customers')
    
bikeshare = State(olin=10, wellesley=10, olin_empty=0, wellesley_empty=0)
p2_array = linspace(0, 1, 10)
p1 = 0.5
num_steps = 60

sweep_p2(p1, p2_array, num_steps)