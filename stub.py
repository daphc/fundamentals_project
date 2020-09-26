#this is a VERY rough draft of a potential outline for our project.
import requests
import matplotlib.pyplot as mpl
import numpy as np

def collect_by_year(filename): #input: a CSV file from RCSB web services
    """ get ids of structures that were released in a particular year """
    #append to years_ids.

def get_avg_mw(dates_files):
    """ get the average molecular weight from structures released in a particular year """
    #from years_ids, extract the average molecular weight and append to years_mw.

def get_num_struct(dates_files):
    """ get the number of released structures from a particular year """"
    #from years_ids, get the number of structures and append to years_num.

def main():
    """ gather the relevant quantities to make the plot """
    years_ids = {} #keys are the years. values are lists of pdb ids
    years_mw = {} #keys are the years. values are the avg molecular weight from each year.
    years_num = {} #keys are the years. values are the number of structures from each year.
    collect_by_year(csv_file)
    get_avg_mw(years_ids)
    get_num_struct(years_ids)
    #plotting: x values are dictionary keys, y values are key values
