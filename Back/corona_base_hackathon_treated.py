"""
Python model "corona_base_hackathon_v3_treated.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

import sys
import warnings

warnings.filterwarnings('ignore')

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'contacts per person symptomatic self': 'contacts_per_person_symptomatic_self',
    'infection rate': 'infection_rate',
    'total infection rate': 'total_infection_rate',
    'symptomatic contact fraction': 'symptomatic_contact_fraction',
    'accumulated cases': 'accumulated_cases',
    'init total population': 'init_total_population',
    'incidence per 100000': 'incidence_per_100000',
    'new cases': 'new_cases',
    'init accumulated cases': 'init_accumulated_cases',
    'case fatality rate': 'case_fatality_rate',
    'test fraction': 'test_fraction',
    'isolation rate asymptomatic': 'isolation_rate_asymptomatic',
    'fraction of symptomatic': 'fraction_of_symptomatic',
    'total infected': 'total_infected',
    'infected symptomatic recovery rate': 'infected_symptomatic_recovery_rate',
    'infected asymptomatic recovery rate': 'infected_asymptomatic_recovery_rate',
    'asymptomatic duration': 'asymptomatic_duration',
    'available test kits': 'available_test_kits',
    'available test kits for testing asymptomatic': 'available_test_kits_for_testing_asymptomatic',
    'available test kits for testing symptomatic': 'available_test_kits_for_testing_symptomatic',
    'contact infectivity asymptomatic self': 'contact_infectivity_asymptomatic_self',
    'contact infectivity quarantine self': 'contact_infectivity_quarantine_self',
    'contact infectivity symptomatic self': 'contact_infectivity_symptomatic_self',
    'contacts per person normal self': 'contacts_per_person_normal_self',
    'Critical Cases': 'critical_cases',
    'critical cases recovery rate': 'critical_cases_recovery_rate',
    'death rate': 'death_rate',
    'deimmunization rate': 'deimmunization_rate',
    'Diseased': 'diseased',
    'duration of treatment': 'duration_of_treatment',
    'effect of kits availability on effectiveness of testing':
    'effect_of_kits_availability_on_effectiveness_of_testing',
    'fraction of asymptomatic case development': 'fraction_of_asymptomatic_case_development',
    'fraction of critical cases': 'fraction_of_critical_cases',
    'fraction of death': 'fraction_of_death',
    'immunity time': 'immunity_time',
    'Infected asymptomatic': 'infected_asymptomatic',
    'Infected symptomatic': 'infected_symptomatic',
    'infected critical case rate': 'infected_critical_case_rate',
    'infection rate asymptomatic self': 'infection_rate_asymptomatic_self',
    'infection rate quarantined self': 'infection_rate_quarantined_self',
    'infection rate symptomatic self': 'infection_rate_symptomatic_self',
    'infectivity per contact': 'infectivity_per_contact',
    'init available test kits': 'init_available_test_kits',
    'init Critical Cases': 'init_critical_cases',
    'init Diseased': 'init_diseased',
    'init Infected asymptomatic': 'init_infected_asymptomatic',
    'init Infected symptomatic': 'init_infected_symptomatic',
    'init Isolated': 'init_isolated',
    'init Recovered': 'init_recovered',
    'init Susceptible': 'init_susceptible',
    'Isolated': 'isolated',
    'isolated recovery rate': 'isolated_recovery_rate',
    'isolation rate symptomatic': 'isolation_rate_symptomatic',
    'kits availability for testing table': 'kits_availability_for_testing_table',
    'kits per person': 'kits_per_person',
    'kits population ratio': 'kits_population_ratio',
    'max kits population ratio': 'max_kits_population_ratio',
    'non controlled population': 'non_controlled_population',
    'produced test kits': 'produced_test_kits',
    'production phase1': 'production_phase1',
    'production phase2': 'production_phase2',
    'production phase3': 'production_phase3',
    'production start phase1': 'production_start_phase1',
    'production start phase2': 'production_start_phase2',
    'production start phase3': 'production_start_phase3',
    'production volume phase1': 'production_volume_phase1',
    'production volume phase2': 'production_volume_phase2',
    'production volume phase3': 'production_volume_phase3',
    'isolation duration': 'isolation_duration',
    'isolated critical case rate': 'isolated_critical_case_rate',
    'isolation effectiveness': 'isolation_effectiveness',
    'Recovered': 'recovered',
    'self quarantine effectiveness': 'self_quarantine_effectiveness',
    'self quarantine policy': 'self_quarantine_policy',
    'self quarantine policy SWITCH self': 'self_quarantine_policy_switch_self',
    'self quarantine start': 'self_quarantine_start',
    'social distancing effectiveness': 'social_distancing_effectiveness',
    'social distancing policy': 'social_distancing_policy',
    'social distancing policy SWITCH self': 'social_distancing_policy_switch_self',
    'social distancing start': 'social_distancing_start',
    'Susceptible': 'susceptible',
    'symptomatic duration': 'symptomatic_duration',
    'symptomatic rate': 'symptomatic_rate',
    'testing duration': 'testing_duration',
    'tests for symptomatic': 'tests_for_symptomatic',
    'used test kits': 'used_test_kits',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def contacts_per_person_symptomatic_self():
    """
    Real Name: b'contacts per person symptomatic self'
    Original Eqn: b'contacts per person normal self*symptomatic contact fraction'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self() * symptomatic_contact_fraction()


@cache('step')
def infection_rate():
    """
    Real Name: b'infection rate'
    Original Eqn: b'total infection rate'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return total_infection_rate()


@cache('step')
def total_infection_rate():
    """
    Real Name: b'total infection rate'
    Original Eqn: b'infection rate asymptomatic self+infection rate quarantined self+infection rate symptomatic self'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infection_rate_asymptomatic_self() + infection_rate_quarantined_self(
    ) + infection_rate_symptomatic_self()


@cache('run')
def symptomatic_contact_fraction():
    """
    Real Name: b'symptomatic contact fraction'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def accumulated_cases():
    """
    Real Name: b'accumulated cases'
    Original Eqn: b'INTEG ( new cases, init accumulated cases)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_accumulated_cases()


@cache('step')
def init_total_population():
    """
    Real Name: b'init total population'
    Original Eqn: b'init Infected asymptomatic+init Susceptible'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return init_infected_asymptomatic() + init_susceptible()


@cache('step')
def incidence_per_100000():
    """
    Real Name: b'incidence per 100000'
    Original Eqn: b'accumulated cases/init total population*100000'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return accumulated_cases() / init_total_population() * 100000


@cache('step')
def new_cases():
    """
    Real Name: b'new cases'
    Original Eqn: b'symptomatic rate*test fraction'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_rate() * test_fraction()


@cache('run')
def init_accumulated_cases():
    """
    Real Name: b'init accumulated cases'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def case_fatality_rate():
    """
    Real Name: b'case fatality rate'
    Original Eqn: b'ZIDZ( Diseased, accumulated cases)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(diseased(), accumulated_cases())


@cache('run')
def test_fraction():
    """
    Real Name: b'test fraction'
    Original Eqn: b'1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def isolation_rate_asymptomatic():
    """
    Real Name: b'isolation rate asymptomatic'
    Original Eqn: b'MIN(available test kits for testing asymptomatic*effect of kits availability on effectiveness of testing\\\\ /kits per person, Infected asymptomatic )/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(
        available_test_kits_for_testing_asymptomatic() *
        effect_of_kits_availability_on_effectiveness_of_testing() / kits_per_person(),
        infected_asymptomatic()) / testing_duration()


@cache('step')
def fraction_of_symptomatic():
    """
    Real Name: b'fraction of symptomatic'
    Original Eqn: b'ZIDZ(Infected symptomatic, total infected)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.zidz(infected_symptomatic(), total_infected())


@cache('step')
def total_infected():
    """
    Real Name: b'total infected'
    Original Eqn: b'Infected asymptomatic+Infected symptomatic'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() + infected_symptomatic()


@cache('step')
def infected_symptomatic_recovery_rate():
    """
    Real Name: b'infected symptomatic recovery rate'
    Original Eqn: b'Infected symptomatic*(1-fraction of critical cases)/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * (1 - fraction_of_critical_cases()) / symptomatic_duration()


@cache('step')
def infected_asymptomatic_recovery_rate():
    """
    Real Name: b'infected asymptomatic recovery rate'
    Original Eqn: b'fraction of asymptomatic case development*Infected asymptomatic/(asymptomatic duration\\\\ +symptomatic duration)'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_of_asymptomatic_case_development() * infected_asymptomatic() / (
        asymptomatic_duration() + symptomatic_duration())


@cache('run')
def asymptomatic_duration():
    """
    Real Name: b'asymptomatic duration'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def available_test_kits():
    """
    Real Name: b'available test kits'
    Original Eqn: b'INTEG ( produced test kits-used test kits, init available test kits)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_available_test_kits()


@cache('step')
def available_test_kits_for_testing_asymptomatic():
    """
    Real Name: b'available test kits for testing asymptomatic'
    Original Eqn: b'MAX(available test kits for testing symptomatic-tests for symptomatic, 0)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(available_test_kits_for_testing_symptomatic() - tests_for_symptomatic(), 0)


@cache('step')
def available_test_kits_for_testing_symptomatic():
    """
    Real Name: b'available test kits for testing symptomatic'
    Original Eqn: b'MAX(available test kits, 0)'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.maximum(available_test_kits(), 0)


@cache('step')
def contact_infectivity_asymptomatic_self():
    """
    Real Name: b'contact infectivity asymptomatic self'
    Original Eqn: b'contacts per person normal self*infectivity per contact*social distancing policy*social distancing policy SWITCH self\\\\ +(1-social distancing policy SWITCH self)*contacts per person normal self*infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_normal_self() * infectivity_per_contact(
    ) * social_distancing_policy() * social_distancing_policy_switch_self() + (
        1 - social_distancing_policy_switch_self()
    ) * contacts_per_person_normal_self() * infectivity_per_contact()


@cache('step')
def contact_infectivity_quarantine_self():
    """
    Real Name: b'contact infectivity quarantine self'
    Original Eqn: b'contact infectivity asymptomatic self*(1-isolation effectiveness)'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contact_infectivity_asymptomatic_self() * (1 - isolation_effectiveness())


@cache('step')
def contact_infectivity_symptomatic_self():
    """
    Real Name: b'contact infectivity symptomatic self'
    Original Eqn: b'contacts per person symptomatic self*infectivity per contact*self quarantine policy*\\\\ self quarantine policy SWITCH self+(1-self quarantine policy SWITCH self)*contacts per person symptomatic self\\\\ *infectivity per contact'
    Units: b'1/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return contacts_per_person_symptomatic_self() * infectivity_per_contact(
    ) * self_quarantine_policy() * self_quarantine_policy_switch_self() + (
        1 - self_quarantine_policy_switch_self()
    ) * contacts_per_person_symptomatic_self() * infectivity_per_contact()


@cache('run')
def contacts_per_person_normal_self():
    """
    Real Name: b'contacts per person normal self'
    Original Eqn: b'30'
    Units: b'contact/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 30


@cache('step')
def critical_cases():
    """
    Real Name: b'Critical Cases'
    Original Eqn: b'INTEG ( infected critical case rate-critical cases recovery rate-death rate+isolated critical case rate\\\\ , init Critical Cases)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_cases()


@cache('step')
def critical_cases_recovery_rate():
    """
    Real Name: b'critical cases recovery rate'
    Original Eqn: b'Critical Cases*(1-fraction of death)/duration of treatment'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases() * (1 - fraction_of_death()) / duration_of_treatment()


@cache('step')
def death_rate():
    """
    Real Name: b'death rate'
    Original Eqn: b'Critical Cases*fraction of death/duration of treatment'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_cases() * fraction_of_death() / duration_of_treatment()


@cache('step')
def deimmunization_rate():
    """
    Real Name: b'deimmunization rate'
    Original Eqn: b'Recovered/immunity time'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered() / immunity_time()


@cache('step')
def diseased():
    """
    Real Name: b'Diseased'
    Original Eqn: b'INTEG ( death rate, init Diseased)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_diseased()


@cache('run')
def duration_of_treatment():
    """
    Real Name: b'duration of treatment'
    Original Eqn: b'10'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10


@cache('step')
def effect_of_kits_availability_on_effectiveness_of_testing():
    """
    Real Name: b'effect of kits availability on effectiveness of testing'
    Original Eqn: b'kits availability for testing table(kits population ratio/max kits population ratio)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return kits_availability_for_testing_table(kits_population_ratio() /
                                               max_kits_population_ratio())


@cache('run')
def fraction_of_asymptomatic_case_development():
    """
    Real Name: b'fraction of asymptomatic case development'
    Original Eqn: b'0.5'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('run')
def fraction_of_critical_cases():
    """
    Real Name: b'fraction of critical cases'
    Original Eqn: b'0.1'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def fraction_of_death():
    """
    Real Name: b'fraction of death'
    Original Eqn: b'0.4'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def immunity_time():
    """
    Real Name: b'immunity time'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('step')
def infected_asymptomatic():
    """
    Real Name: b'Infected asymptomatic'
    Original Eqn: b'INTEG ( infection rate-infected asymptomatic recovery rate-isolation rate asymptomatic-symptomatic rate\\\\ , init Infected asymptomatic)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_asymptomatic()


@cache('step')
def infected_symptomatic():
    """
    Real Name: b'Infected symptomatic'
    Original Eqn: b'INTEG ( symptomatic rate-infected critical case rate-infected symptomatic recovery rate-isolation rate symptomatic\\\\ , init Infected symptomatic)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_infected_symptomatic()


@cache('step')
def infected_critical_case_rate():
    """
    Real Name: b'infected critical case rate'
    Original Eqn: b'Infected symptomatic*fraction of critical cases/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * fraction_of_critical_cases() / symptomatic_duration()


@cache('step')
def infection_rate_asymptomatic_self():
    """
    Real Name: b'infection rate asymptomatic self'
    Original Eqn: b'Infected asymptomatic*Susceptible*contact infectivity asymptomatic self/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() * susceptible() * contact_infectivity_asymptomatic_self(
    ) / non_controlled_population()


@cache('step')
def infection_rate_quarantined_self():
    """
    Real Name: b'infection rate quarantined self'
    Original Eqn: b'Isolated*Susceptible*contact infectivity quarantine self/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * susceptible() * contact_infectivity_quarantine_self(
    ) / non_controlled_population()


@cache('step')
def infection_rate_symptomatic_self():
    """
    Real Name: b'infection rate symptomatic self'
    Original Eqn: b'Infected symptomatic*Susceptible*contact infectivity symptomatic self/non controlled population'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() * susceptible() * contact_infectivity_symptomatic_self(
    ) / non_controlled_population()


@cache('run')
def infectivity_per_contact():
    """
    Real Name: b'infectivity per contact'
    Original Eqn: b'0.0125'
    Units: b'1/contact'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.0125


@cache('run')
def init_available_test_kits():
    """
    Real Name: b'init available test kits'
    Original Eqn: b'0'
    Units: b'kit'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_critical_cases():
    """
    Real Name: b'init Critical Cases'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_diseased():
    """
    Real Name: b'init Diseased'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_infected_asymptomatic():
    """
    Real Name: b'init Infected asymptomatic'
    Original Eqn: b'1'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('run')
def init_infected_symptomatic():
    """
    Real Name: b'init Infected symptomatic'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_isolated():
    """
    Real Name: b'init Isolated'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_recovered():
    """
    Real Name: b'init Recovered'
    Original Eqn: b'0'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def init_susceptible():
    """
    Real Name: b'init Susceptible'
    Original Eqn: b'8e+06'
    Units: b'person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 8e+06


@cache('step')
def isolated():
    """
    Real Name: b'Isolated'
    Original Eqn: b'INTEG ( isolation rate symptomatic+isolation rate asymptomatic-isolated recovery rate-isolated critical case rate\\\\ , init Isolated)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_isolated()


@cache('step')
def isolated_recovery_rate():
    """
    Real Name: b'isolated recovery rate'
    Original Eqn: b'Isolated*(1-fraction of critical cases)/isolation duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * (1 - fraction_of_critical_cases()) / isolation_duration()


@cache('step')
def isolation_rate_symptomatic():
    """
    Real Name: b'isolation rate symptomatic'
    Original Eqn: b'tests for symptomatic/kits per person/testing duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return tests_for_symptomatic() / kits_per_person() / testing_duration()


def kits_availability_for_testing_table(x):
    """
    Real Name: b'kits availability for testing table'
    Original Eqn: b'( [(0,0)-(1,1)],(0,0),(0.25,0.6),(0.5,0.85),(1,1))'
    Units: b'dmnl'
    Limits: (None, None)
    Type: lookup

    b''
    """
    return functions.lookup(x, [0, 0.25, 0.5, 1], [0, 0.6, 0.85, 1])


@cache('run')
def kits_per_person():
    """
    Real Name: b'kits per person'
    Original Eqn: b'1'
    Units: b'kit/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def kits_population_ratio():
    """
    Real Name: b'kits population ratio'
    Original Eqn: b'available test kits for testing asymptomatic/non controlled population'
    Units: b'kit/person'
    Limits: (None, None)
    Type: component

    b''
    """
    return available_test_kits_for_testing_asymptomatic() / non_controlled_population()


@cache('run')
def max_kits_population_ratio():
    """
    Real Name: b'max kits population ratio'
    Original Eqn: b'1'
    Units: b'kit/person'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1


@cache('step')
def non_controlled_population():
    """
    Real Name: b'non controlled population'
    Original Eqn: b'Infected symptomatic+Susceptible+Infected asymptomatic+Isolated+Recovered'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_symptomatic() + susceptible() + infected_asymptomatic() + isolated(
    ) + recovered()


@cache('step')
def produced_test_kits():
    """
    Real Name: b'produced test kits'
    Original Eqn: b'(production phase1+production phase2+production phase3)*0'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return (production_phase1() + production_phase2() + production_phase3()) * 0


@cache('step')
def production_phase1():
    """
    Real Name: b'production phase1'
    Original Eqn: b'PULSE(production start phase1, production start phase2-production start phase1)*production volume phase1'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase1(),
        production_start_phase2() - production_start_phase1()) * production_volume_phase1()


@cache('step')
def production_phase2():
    """
    Real Name: b'production phase2'
    Original Eqn: b'PULSE(production start phase2, production start phase3-production start phase2)*production volume phase2'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase2(),
        production_start_phase3() - production_start_phase2()) * production_volume_phase2()


@cache('step')
def production_phase3():
    """
    Real Name: b'production phase3'
    Original Eqn: b'PULSE(production start phase3, FINAL TIME-production start phase3+1)*production volume phase3'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return functions.pulse(
        __data['time'], production_start_phase3(),
        final_time() - production_start_phase3() + 1) * production_volume_phase3()


@cache('run')
def production_start_phase1():
    """
    Real Name: b'production start phase1'
    Original Eqn: b'50'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 50


@cache('run')
def production_start_phase2():
    """
    Real Name: b'production start phase2'
    Original Eqn: b'90'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 90


@cache('run')
def production_start_phase3():
    """
    Real Name: b'production start phase3'
    Original Eqn: b'250'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 250


@cache('run')
def production_volume_phase1():
    """
    Real Name: b'production volume phase1'
    Original Eqn: b'500'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 500


@cache('run')
def production_volume_phase2():
    """
    Real Name: b'production volume phase2'
    Original Eqn: b'6000'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 6000


@cache('run')
def production_volume_phase3():
    """
    Real Name: b'production volume phase3'
    Original Eqn: b'10000'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 10000


@cache('run')
def isolation_duration():
    """
    Real Name: b'isolation duration'
    Original Eqn: b'14'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 14


@cache('step')
def isolated_critical_case_rate():
    """
    Real Name: b'isolated critical case rate'
    Original Eqn: b'Isolated*fraction of critical cases/symptomatic duration'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return isolated() * fraction_of_critical_cases() / symptomatic_duration()


@cache('run')
def isolation_effectiveness():
    """
    Real Name: b'isolation effectiveness'
    Original Eqn: b'0.9'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.9


@cache('step')
def recovered():
    """
    Real Name: b'Recovered'
    Original Eqn: b'INTEG ( critical cases recovery rate+infected asymptomatic recovery rate+infected symptomatic recovery rate\\\\ -deimmunization rate+isolated recovery rate, init Recovered)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_recovered()


@cache('run')
def self_quarantine_effectiveness():
    """
    Real Name: b'self quarantine effectiveness'
    Original Eqn: b'0.75'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.75


@cache('step')
def self_quarantine_policy():
    """
    Real Name: b'self quarantine policy'
    Original Eqn: b'1-PULSE(self quarantine start, FINAL TIME-self quarantine start+1)*self quarantine effectiveness'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(
        __data['time'], self_quarantine_start(),
        final_time() - self_quarantine_start() + 1) * self_quarantine_effectiveness()


@cache('run')
def self_quarantine_policy_switch_self():
    """
    Real Name: b'self quarantine policy SWITCH self'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def self_quarantine_start():
    """
    Real Name: b'self quarantine start'
    Original Eqn: b'21'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 21


@cache('run')
def social_distancing_effectiveness():
    """
    Real Name: b'social distancing effectiveness'
    Original Eqn: b'0.6'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('step')
def social_distancing_policy():
    """
    Real Name: b'social distancing policy'
    Original Eqn: b'1-PULSE(social distancing start, FINAL TIME-social distancing start+1)*social distancing effectiveness'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return 1 - functions.pulse(
        __data['time'], social_distancing_start(),
        final_time() - social_distancing_start() + 1) * social_distancing_effectiveness()


@cache('run')
def social_distancing_policy_switch_self():
    """
    Real Name: b'social distancing policy SWITCH self'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('run')
def social_distancing_start():
    """
    Real Name: b'social distancing start'
    Original Eqn: b'31'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 31


@cache('step')
def susceptible():
    """
    Real Name: b'Susceptible'
    Original Eqn: b'INTEG ( deimmunization rate-infection rate, init Susceptible)'
    Units: b'person'
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible()


@cache('run')
def symptomatic_duration():
    """
    Real Name: b'symptomatic duration'
    Original Eqn: b'5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 5


@cache('step')
def symptomatic_rate():
    """
    Real Name: b'symptomatic rate'
    Original Eqn: b'Infected asymptomatic/asymptomatic duration*(1-fraction of asymptomatic case development\\\\ )'
    Units: b'person/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected_asymptomatic() / asymptomatic_duration() * (
        1 - fraction_of_asymptomatic_case_development())


@cache('run')
def testing_duration():
    """
    Real Name: b'testing duration'
    Original Eqn: b'0.5'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.5


@cache('step')
def tests_for_symptomatic():
    """
    Real Name: b'tests for symptomatic'
    Original Eqn: b'MIN(available test kits for testing symptomatic, Infected symptomatic*kits per person\\\\ )'
    Units: b'kit'
    Limits: (None, None)
    Type: component

    b''
    """
    return np.minimum(available_test_kits_for_testing_symptomatic(),
                      infected_symptomatic() * kits_per_person())


@cache('step')
def used_test_kits():
    """
    Real Name: b'used test kits'
    Original Eqn: b'(infected critical case rate+isolation rate symptomatic+isolation rate asymptomatic)\\\\ *kits per person'
    Units: b'kit/Day'
    Limits: (None, None)
    Type: component

    b''
    """
    return (infected_critical_case_rate() + isolation_rate_symptomatic() +
            isolation_rate_asymptomatic()) * kits_per_person()


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'360'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 360


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'Day'
    Limits: (0.0, None)
    Type: component

    b''
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'0.015625'
    Units: b'Day'
    Limits: (0.0, None)
    Type: constant

    b''
    """
    return 0.015625


_integ_accumulated_cases = functions.Integ(lambda: new_cases(), lambda: init_accumulated_cases())

_integ_available_test_kits = functions.Integ(lambda: produced_test_kits() - used_test_kits(),
                                             lambda: init_available_test_kits())

_integ_critical_cases = functions.Integ(
    lambda: infected_critical_case_rate() - critical_cases_recovery_rate() - death_rate() +
    isolated_critical_case_rate(), lambda: init_critical_cases())

_integ_diseased = functions.Integ(lambda: death_rate(), lambda: init_diseased())

_integ_infected_asymptomatic = functions.Integ(
    lambda: infection_rate() - infected_asymptomatic_recovery_rate() - isolation_rate_asymptomatic(
    ) - symptomatic_rate(), lambda: init_infected_asymptomatic())

_integ_infected_symptomatic = functions.Integ(
    lambda: symptomatic_rate() - infected_critical_case_rate(
    ) - infected_symptomatic_recovery_rate() - isolation_rate_symptomatic(),
    lambda: init_infected_symptomatic())

_integ_isolated = functions.Integ(
    lambda: isolation_rate_symptomatic() + isolation_rate_asymptomatic() - isolated_recovery_rate(
    ) - isolated_critical_case_rate(), lambda: init_isolated())

_integ_recovered = functions.Integ(
    lambda: critical_cases_recovery_rate() + infected_asymptomatic_recovery_rate(
    ) + infected_symptomatic_recovery_rate() - deimmunization_rate() + isolated_recovery_rate(),
    lambda: init_recovered())

_integ_susceptible = functions.Integ(lambda: deimmunization_rate() - infection_rate(),
                                     lambda: init_susceptible())


# sys.stdout.flush()