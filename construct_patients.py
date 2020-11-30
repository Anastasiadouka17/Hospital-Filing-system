#Anastasia Douka
#260768503

import doctest
import datetime
import numpy as np
import matplotlib.pyplot as plt


class Patient:
    """ Represents a patient"""
    # starting from the second column
    def __init__(self,num,day_diagnosed,age,sex_gender,postal,state,temps,days_symptomatic):
        self.num = num
        self.day_diagnosed = day_diagnosed
        self.age = age
        self.sex_gender = Patient.gender(sex_gender)
        self.postal = Patient.postal_code(postal)
        self.state = state
        self.temps = Patient.temperature(temps)
        self.days_symptomatic = days_symptomatic

    def gender(sex_gender):
        if 'GIRL' in sex_gender or 'FEMMES' in sex_gender or 'F' in sex_gender or 'WOMAN' in sex_gender:
            return 'F'
        elif 'MALE' in sex_gender or 'M' in sex_gender or 'HOMME' in sex_gender or 'BOY' in sex_gender:
            return 'M'
        else:
            return 'X'
    def postal_code(postal):
            

            if postal[0]== 'H' and type(postal[1])== int and type(postal[2])== str:
                return postal[0:3]
            else:
                return '000'
              
    def temperature(temps):
        try:
            if '-' in temps :
                temps = temps.replace('-', '.')
            if '°' in temps:
                temps = temps.replace('°', '')
            if temps[-1]== 'C' or temps[-1] == 'F':
                temps = temps[:-1]
            if float(temps) > 45:
                temps = ((float(temps) - 32) * (5/9))
                temps = round(temps, 2)
            return str(temps)    
        except ValueError:
            return '0'
    def __str__(p):

        a = [p.num, p.age, p.sex_gender, p.postal, p.day_diagnosed, p.state, p.days_symptomatic]
        str_result = '\t'.join(a)
        return str_result

    def update(self, p1):
        if self.num == p1.num and self.sex_gender == p1.sex_gender and self.postal== p1.postal:
            self.days_symptomatic = p1.days_symptomatic
            self.state = p1.state
            a = [self.temps, p1.temps]
            self.temps = ';'.join(a)
        else:
            raise AssertionError
def stage_four(input_filename, output_filename):
    inFile = open(input_filename, 'r', encoding = 'utf-8') 
    outFile = open(output_filename, 'w', encoding = 'utf-8')
    records = inFile.readlines()
    patients_dict = {}
    for line in records:
        attributes = line.split('\t')
        p = Patient(attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6], attributes[7], attributes[8])
        if p.num not in patients_dict:
            patients_dict[p.num] = p
        else:
            try:
                patients_dict[p.num].update(p)
            except AssertionError:
                continue
    copy_patients_dict = patients_dict.copy()        
    while len(copy_patients_dict)!= 0:
        patient = copy_patients_dict.pop(min(copy_patients_dict))
        line = str(patient)
        outFile.write(line)

    return patients_dict    

if __name__ == '__main__':
    doctest.testmod()
    stage_four('stage3.tsv', 'stage4.tsv')
            
        
