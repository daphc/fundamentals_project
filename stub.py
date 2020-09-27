import pandas
import matplotlib.pyplot as mpl
import numpy as np

def collect_by_year():
    """ get ids of structures that were released in a particular year """
    # data = pandas.read_csv("https://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,molecularWeight&format=csv&service=wsfile")
    ## this has 625,129 structures

    years_ids = {} #keys are the years. values are lists of pdb ids
    # test link:
    # data = pandas.read_csv("https://www.rcsb.org/pdb/rest/customReport.csv?pdbids=100D,4HYA,3IRL&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&format=csv&service=wsfile")
    ## test data

    #data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,structureMolecularWeight,releaseDate&service=wsfile&format=csv")
    ## above data has 173,223 strucutures. So far this is closest to what the RCSB website has for strucutures

    # data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    new_data = data.dropna()
    print(new_data.head(10))
    # data = pandas.read_csv('./PDB_data.csv') ## pulls from file 140,480 strucutures
    # print (data.tail(n=10))
    # sort_by_year = new_data.sort_values('releaseDate') ## this sorts everything by data for new_data
    # print('This is data without Na\n', new_data.tail(n=10))
    # print ('This is data with Na\n', data.tail(n=10))
    # print ('This is length of without Na\n', len(new_data))

    for index, row in new_data.iterrows():
         if "Protein" not in row[3]:
             pass
         elif row[1] not in years_ids.keys(): #year not in dictionary
            # print("new year and PDB ID added to dictionary.")
            years_ids[row[1]] = [row[0]]
         elif row[1] in years_ids.keys() and row[0] not in years_ids[row[1]]: #year in dictionary but a pdb id from that year isn't
            # print("new PDB ID added to already existing year.")
            years_ids[row[1]].append(row[0])
         elif row[1] in years_ids.keys() and row[0] in years_ids[row[1]]:
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
