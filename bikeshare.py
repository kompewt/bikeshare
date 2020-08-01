# -*- coding: utf-8 -*-
# import functions from the modsim library
from matplotlib import *
from modsim import *

def run_simulation(p1, p2, num_steps):
    '''
    Takes the values p1 and p2 as probabilities
    a bike will be taken from a station and returned to the alternate station
    over a time period of minutes defined by num_steps
    '''
    timeO = TimeSeries()
    timeW = TimeSeries()
    unhappy = TimeSeries()

    # Step through minutes testing and recording bike movements
    for i in range(num_steps):
        wes = flip(p1)
        oli = flip(p2)
        if wes == oli:
            timeO[i] = bikeshare.olin
            timeW[i] = bikeshare.wellesley
            continue
        if wes: # if bike from olin to wellesley
            if bikeshare.olin == 0: # catch -1 bikes = unhappy customer
                bikeshare.olin_empty += 1 # count lost sales
                unhappy[i] = 0 # record time series of unhappy moments
                if bikeshare.clock == 0: # if first unhappy customer
                    bikeshare.clock = i # record first unhappy moment
                timeO[i] = bikeshare.olin
                timeW[i] = bikeshare.wellesley
                continue
            bikeshare.olin -= 1
            bikeshare.wellesley += 1
        if oli: # if bike from wellesley to olin
            if bikeshare.wellesley == 0: # catch -1 bikes = unhappy customer
                bikeshare.wellesley_empty += 1 # count lost sales
                unhappy[i] = 0 # record time series of unhappy moments
                if bikeshare.clock == 0: # if first unhappy customer
                    bikeshare.clock = i # record first unhappy moment
                timeO[i] = bikeshare.olin
                timeW[i] = bikeshare.wellesley
                continue
            bikeshare.olin += 1
            bikeshare.wellesley -= 1
        # Write bike states
        timeO[i] = bikeshare.olin
        timeW[i] = bikeshare.wellesley

    # plot bike values and unhappy customers over time
    plt.figure()
    plt.plot(timeO, label='Olin')
    plt.plot(timeW, label='Wellesley')
    plt.scatter(unhappy.index, unhappy, color='red', label='Unhappy customer')
    decorate(title='Olin-Wellesley Bikeshare',
             xlabel='Time step (min)',
             ylabel='Number of bikes')
    plt.show()
    # unhappy customer info
    print(bikeshare.olin_empty)
    print('unhappy customers')
    print(bikeshare.clock)
    print('minutes until the first unhappy customer')

bikeshare = State(olin=10, wellesley=10, olin_empty=0, wellesley_empty=0, clock=0)
run_simulation(0.6, 0.4, 60)

