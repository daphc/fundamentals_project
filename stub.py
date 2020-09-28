
import pandas
import matplotlib.pyplot as mpl
import numpy as np
from statistics import mean

def collect_by_year(dataframe):
    """ get ids of structures that were released in a particular year """
    years_ids = {} #keys are the years. values are lists of pdb ids
    for index, row in dataframe.iterrows():
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
    return years_ids

def get_avg_mw(dates_files, dataframe):
    """ get the average molecular weight from structures released in a particular year """
    years_mw = {} #keys are the years. values are the avg molecular weight from each year.
    for year, lists in dates_files.items():
        weights = []
        for id in lists:
            row = dataframe.loc[dataframe["structureId"] == id]
            weight = float(row["structureMolecularWeight"])
            weights.append(weight)
        avg = mean(weights)
        years_mw[year] = avg
    print(years_mw)
    return years_mw

def get_num_struct(dates_files):
    """ get the number of released structures from a particular year """
    #from years_ids, get the number of structures and append to years_num.
    a = []
    for keys,values in dates_files.items():
        b = keys, len(list(filter(None, values))) ## takes keys and counts the values in said key
        a.append (b)
    data = pandas.DataFrame (data=a) ## makes a data Fram for future graphing
    # print (data)
    return data

def main():
    """ gather the relevant quantities and make the plot """
    # data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    final_data = data.dropna()
    entries = collect_by_year(final_data)
    average_weight = get_avg_mw(entries, final_data)
    get_num_struct(entries)
    #plotting: x values are dictionary keys, y values are key values

if __name__ == "__main__":
    main()