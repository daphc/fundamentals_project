import pandas
import matplotlib.pyplot as mpl
import numpy as np

def collect_by_year():
    """ get ids of structures that were released in a particular year """
    #all PDBS: data = pandas.read_csv("https://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,molecularWeight&format=csv&service=wsfile")
    years_ids = {} #keys are the years. values are lists of pdb ids
    #test link:
    data = pandas.read_csv("https://www.rcsb.org/pdb/rest/customReport.csv?pdbids=100D,4HYA,3IRL&customReportColumns=structureId,releaseDate,molecularWeight&format=csv&service=wsfile")
    print(data.head())
    #Investigate NaN displayed -- maybe we need to ask for a diffferent property, not molecularWeight
    for index, row in data.iterrows():
         if row[2] not in years_ids.keys(): #year not in dictionary
            print("new year and PDB ID added to dictionary.")
            years_ids[row[2]] = [row[0]]
         elif row[2] in years_ids.keys() and row[0] not in years_ids[row[2]]: #year in dictionary but a pdb id from that year isn't
            print("new PDB ID added to already existing year.")
            years_ids[row[2]].append(row[0])
         elif row[2] in years_ids.keys() and row[0] in years_ids[row[2]]:
            print("Duplicate skipped.")
         else:
            print("Something went wrong.")
        # need to incorporate error handling for NaN molecular weight.
    print(years_ids)
    #append to years_ids.

def get_avg_mw(dates_files):
    """ get the average molecular weight from structures released in a particular year """
    #from years_ids, extract the average molecular weight and append to years_mw.

def get_num_struct(dates_files):
    """ get the number of released structures from a particular year """
    #from years_ids, get the number of structures and append to years_num.

def main():
    """ gather the relevant quantities and make the plot """
    years_mw = {} #keys are the years. values are the avg molecular weight from each year.
    years_num = {} #keys are the years. values are the number of structures from each year.
    collect_by_year()
    # get_avg_mw(years_ids)
    # get_num_struct(years_ids)
    #plotting: x values are dictionary keys, y values are key values

if __name__ == "__main__":
    main()
