#Anastasia Douka
#260768503

import doctest
import datetime
import numpy as np
import matplotlib.pyplot as plt

def date_diff(date1, date2):
    '''
    (str, str)-> int
    Input two strings representing dates in ISO format
    and returns how many days apart the two dates are as an int.
    >>> date_diff('2019-10-31', '2019-11-2')
    2
    >>> date_diff('2019-04-16', '2019-03-17')
    -30
    '''
    date1_list = date1.split('\t')#create a list of the date so we can access the index correctly
    date2_list = date2.split('\t')
    year1 = int(date1_list[0])
    month1 = int(date1_list[1])
    day1 = int(date1_list[2])
    year2 = int(date2_list[0])
    month2 = int(date2_list[1])
    day2 = int(date2_list[2])
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    diff = date2 - date1

    return diff.days

def get_age(date1, date2):
    '''
    (str, str)-> int
    This function takes as input two strings represeting dates in ISO format
    and returns how many complete years apart the two dates are.
    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    '''
    one_year = 365.2425 #one year in days(given)
    days_apart = date_diff(date1, date2)
    years_apart = int(days_apart/one_year)#use int to round down, as complete years are requested
    return (years_apart)

def stage_three(input_filename, output_filename):
    '''
    (file, file)-> dict
    Input two files.
    Return: a dictionary. The keys are each day of the pandemic (integer). The values are a dictionary, with how many people are in each state on that day. Example:
    >>> stage_three('stage2.tsv', 'stage3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}
    '''
    inFile = open(input_filename, 'r') 
    outFile = open(output_filename, 'w', encoding = 'utf-8')
    records = inFile.readlines()
    line = records[0]
    columns = line.split('\t')
    index_date = columns[2]
    days_of_pandemic_dict = {}#dict to store days of pandemic

    for line in records:
        state_dict = {'I':0, 'R':0, 'D':0} #dict with health state of each person
        days_admitted = date_diff(columns[2], index_date)
        age_admitted = get_age(columns[3], index_date)

        columns[2] = days_admitted
        columns[3] = age_admitted
        
        if 'I' in columns[6]:
            columns[6] = 'I'
            state_dict['I'] += 1

        elif 'DEA' or 'M' in columns[6]:
            columns[6] = 'D'
            state_dict['D'] += 1

        elif 'REC' in columns[6]:
            columns[6] = 'R'
            state_dict['R'] += 1

        if days_admitted not in days_of_pandemic_dict:
           days_of_pandemic_dict[days_admitted] = state_dict
        else:
            for key in state_dict:
                days_of_pandemic_dict[days_admitted][key] += state_dict[key]

        line = '\t'.join(columns)
        outFile.write(line)

        return days_of_pandemic_dict

def plot_time_series(days_dict):
    '''
    (dict) ->  list
    Input: a dictionary of dictionaries, formatted as the return value of Stage Three.
    Return: a list of lists, where each sublist represents each day of the pandemic.
    Each sublist [how many people infected, how many people recovered, how many people dead]
    >>> d = stage_three(’stage2.tsv’, ’stage3.tsv’)
    >>> plot_time_series(d)
    [[1, 0, 0], [2, 0, 1]]
    '''
    days_list = []

    while len(days_dict) != 0:
        #create the inner list to store the data in dict_min_day
        dict_min_day = days_dict[min(days_dict)]
        # delete min key
        del days_dict[min(days_dict)]

        #create the inner list to store the data in dict_min_day
        inner_list_each_day = []
        for key in dict_min_day:
            inner_list_each_day.append(dict_min_day[key])

        # now inner list is filled, we append it to days_list
        days_list.append(inner_list_each_day)
    
    sum_inf = 0 #sum of infected
    sum_rec = 0 #sum of recovered
    sum_dead = 0 #sum of dead
    list_inf = []
    list_rec = []
    list_dead = []
    for sublist in days_list:
        sum_inf += sublist[0]
        list_inf.append(sum_inf)

        sum_rec += sublist[1]
        list_rec.append(sum_rec)

        sum_dead += sublist[2]
        list_dead.append(sum_dead)

    plt.title('Time series of early pandemic, by Anastasia Douka', fontsize = 20)
    plt.xlabel('Days into Pandemic', fontsize = 14)
    plt.ylabel('Number of People', fontsize = 14)    
    plt.plot(list_inf, '-g')
    plt.plot(list_rec, '_.r')
    plt.plot(list_dead, 'k')
    plt.legend(['Infected', 'Recovered', 'Dead'])
    plt.savefig(time_series.png)        
            
    return days_list        
    
    
if __name__=='__main__':
    doctest.testmod()
    date_diff(date1, date2)
    get_age(date1, date2)
    stage_three('output_filename','stage_three.tsv')
    plot_time_series(stage_three('output_filename','stage_three.tsv')) 
