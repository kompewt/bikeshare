# -*- coding: utf-8 -*-
# import functions from the modsim library
from matplotlib import *
from modsim import *
    
bikeshare = State(olin=10, wellesley=10, olin_empty=0, wellesley_empty=0)
p2_array = linspace(0, 1, 20)
p3_array = linrange(0, 20, 1)
p1 = 0.5
num_steps = 60

plot(sweep_series, label='Olin')
decorate(title='Olin-Wellesley Bikeshare',
         xlabel='Arrival rate at Olin (p1 in customers/min)', 
         ylabel='Number of unhappy customers')

def empty_avg(p1, p2_array, p3_array, num_steps):
    for p3 in p3_array:
        sweep_series3[p3] = sweep_empty(p1, p2_array, num_steps)
    for p2 in p2_array:
        temp = sweep_series3[p3]
        for l in range(len(sweep_series2)):
            
            sweep_series2[l] = sweep_series[k]

def sweep_empty(p1, p2_array, num_steps):
    global bikeshare
    init_state = bikeshare
    sweep_series = list()
    for p2 in p2_array:
        run_sim(p1, p2, num_steps)
        sweep_series[p2] = bikeshare.wellesley_empty
        bikeshare = init_state
    return sweep_series

def run_sim(p1, p2, num_steps):
    global bikeshare
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