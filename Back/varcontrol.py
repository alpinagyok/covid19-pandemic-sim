# this is a script that helps keep track of the variables in the model

import pandas as pd
from pathlib import Path
from pysd.py_backend.functions import Model

age_groups = ['80','70']

# Time list is fix and won't change
time_lst = ['INITIAL TIME', 'FINAL TIME', 'SAVEPER']

#init list needs to be updated and copied into the the model.py script
init_lst = ['init Critical Cases', 'init Diseased',
            'init Infected asymptomatic', 'init Infected symptomatic',
            'init Isolated', 'init Recovered', 'init Susceptible', 'init accumulated cases']

def agify_init():
    out_lst = []
    for el in init_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

#model list needs to be updated and copied into the the model.py script
model_lst = ['asymptomatic duration', 'contacts per person normal self',
             'duration of treatment', 'fraction of asymptomatic case development', 'fraction of critical cases',
             'fraction of death', 'immunity time', 'infectivity per contact', 'isolation duration',
             'isolation effectiveness', 'symptomatic duration', 'test fraction', 'symptomatic contact fraction']

def agify_model():
    out_lst = []
    for el in model_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

#stock list needs to be updated and copied into the the model.py script
#stocks are sinks that accumulate over time
stock_lst = ['Infected asymptomatic', 'Infected symptomatic', 'Critical Cases', 'Diseased',
             'Susceptible', 'Isolated', 'Recovered', 'total infected', 'accumulated cases']

def agify_stock():
    out_lst = []
    for el in stock_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

#flow list needs to be updated and copied into the the model.py script
#flows are the rates at which persons flow between the stocks
flow_lst = ['critical cases recovery rate', 'death rate', 'deimmunization rate',
            'infected asymptomatic recovery rate', 'infected critical case rate',
            'infected symptomatic recovery rate',
            'infection rate', 'infection rate asymptomatic self',
            'infection rate quarantined self', 'infection rate symptomatic self',
            'isolated recovery rate', 'isolation rate asymptomatic', 'isolation rate symptomatic',
            'isolated critical case rate', 'symptomatic rate', 'new cases']

def agify_flow():
    out_lst = []
    for el in flow_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

#endo list needs to be updated and copied into the the model.py script
endo_lst = ['contact infectivity asymptomatic self', 'contact infectivity quarantine self', 'contact infectivity symptomatic self',
            'fraction of symptomatic', 'non controlled population', 'incidence per 100000', 'case fatality rate', 'total infection rate', 'contacts per person symptomatic self',
            'init total population']
def agify_endo():
    out_lst = []
    for el in endo_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

#ignore params are varaibles that are currently not looked at but are in the model for further work
ignore_param_lst = ['available test kits', 'available test kits for testing asymptomatic',
                    'available test kits for testing symptomatic',
                    'effect of kits availability on effectiveness of testing',
                    'kits per person', 'kits population ratio', 'max kits population ratio',
                    'produced test kits',
                    'production phase1', 'production phase2', 'production phase3',
                    'production start phase1', 'production start phase2', 'production start phase3',
                    'production volume phase1', 'production volume phase2', 'production volume phase3',
                    'testing duration', 'tests for symptomatic', 'used test kits', 'sum infection rate',
                    'init available test kits']

#policy param variables are handled differently in the script and don't have to be copied
policy_param_lst = ['self quarantine effectiveness', 'self quarantine policy',
                    'self quarantine policy SWITCH self', 'self quarantine start',
                    'social distancing effectiveness', 'social distancing policy',
                    'social distancing policy SWITCH self', 'social distancing start']

def agify_policy():
    out_lst = []
    for el in policy_param_lst:
        # this needs to be added for the moment because we have both models mixed
        out_lst.append(el)
        for group in age_groups:
            item = '%s %s' % (el,group)
            out_lst.append(item)
    return out_lst

ignore_lst = ['TIME', 'TIME STEP']



def run_varcontrol():
    model = Model('corona_base_hackathon_treated.py')
    var_df = model.run()
    var_lst = var_df.columns.tolist()
    print('Total number of variables:', len(var_lst))

    var_lst = [v for v in var_lst if v not in time_lst]
    var_lst = [v for v in var_lst if v not in init_lst]
    var_lst = [v for v in var_lst if v not in model_lst]
    var_lst = [v for v in var_lst if v not in stock_lst]
    var_lst = [v for v in var_lst if v not in flow_lst]
    var_lst = [v for v in var_lst if v not in endo_lst]
    var_lst = [v for v in var_lst if v not in ignore_param_lst]
    var_lst = [v for v in var_lst if v not in policy_param_lst]
    var_lst = [v for v in var_lst if v not in ignore_lst]

    print('Variables that are not sorted yet:', var_lst)
    print('Number of not sorted variables:', len(var_lst))

def run_varcontrol_age():
    model = Model('corona_base_hackathon_agegroups_treated.py')
    var_df = model.run()
    var_lst = var_df.columns.tolist()
    print('Total number of variables:', len(var_lst))

    #no need to agifiy
    var_lst = [v for v in var_lst if v not in time_lst]
    var_lst = [v for v in var_lst if v not in ignore_lst]
    var_lst = [v for v in var_lst if v not in ignore_param_lst]
    lst = agify_init()
    var_lst = [v for v in var_lst if v not in lst]
    lst = agify_model()
    var_lst = [v for v in var_lst if v not in lst]
    lst = agify_stock()
    var_lst = [v for v in var_lst if v not in lst]
    lst = agify_flow()
    var_lst = [v for v in var_lst if v not in lst]
    lst = agify_endo()
    var_lst = [v for v in var_lst if v not in lst]
    lst = agify_policy()
    var_lst = [v for v in var_lst if v not in lst]

    combo_lst = ['70x80', '80x70']

    var_lst = [v for v in var_lst if v[-5:] not in combo_lst]


    print('Variables that are not sorted yet:', var_lst)
    print('Number of not sorted variables:', len(var_lst))

if __name__ == '__main__':
    #run_varcontrol()
    run_varcontrol_age()



