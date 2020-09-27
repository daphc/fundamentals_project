import pandas
import matplotlib.pyplot as mpl
import numpy as np

def collect_by_year():
    """ get ids of structures that were released in a particular year """
    # test: data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    years_ids = {} #keys are the years. values are lists of pdb ids
    data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    final_data = data.dropna()
    for index, row in final_data.iterrows():
         year = row[1][0:4]
         if year not in years_ids.keys(): #year not in dictionary
            # print("new year and PDB ID added to dictionary.")
            years_ids[year] = [row[0]]
         elif year in years_ids.keys() and row[0] not in years_ids[year]: #year in dictionary but a pdb id from that year isn't
            # print("new PDB ID added to already existing year.")
            years_ids[year].append(row[0])
         elif year in years_ids.keys() and row[0] in years_ids[year]:
             pass
            # print("Duplicate skipped.")
         else:
            print("Something went wrong.")
    counting_list = []
    for list in years_ids.values():
        for i in range(0, len(list)):
            if list[i] in counting_list:
                pass
            else:
                counting_list.append(list[i])
    print("There are", len(counting_list), "structures")
    print(final_data.shape)
    return years_ids

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
    entries = collect_by_year()
    # get_avg_mw(entries)
    # get_num_struct(entries)
    #plotting: x values are dictionary keys, y values are key values

if __name__ == "__main__":
    main()
