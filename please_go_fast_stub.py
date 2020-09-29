import pandas
import matplotlib.pyplot as mpl
from statistics import mean

def get_avg_mw(dataframe):
    """ get the average molecular weight from structures released in a particular year """
    years_mw = {}
    for keys in range (len(dataframe.index)):
        if dataframe["releaseDate"][keys][0:4] not in years_mw.keys():
            years_mw[dataframe["releaseDate"][keys][0:4]] = []
            molecularweight = dataframe["structureMolecularWeight"][keys]
            years_mw[dataframe["releaseDate"][keys][0:4]].append(molecularweight)
        else:
            molecularweight = dataframe["structureMolecularWeight"][keys]
            years_mw[dataframe["releaseDate"][keys][0:4]].append(molecularweight)
    mw_data= []
    for key, values in years_mw.items():
        data = key, mean (values)
        mw_data.append (data)
    final_data = pandas.DataFrame (data=mw_data)
    # print (final_data)

    """ Below code makes sure that the number of strucuters remains the same """

    # counting_list = 0
    # for keys in years_mw.keys():
    #     length =  len(years_mw[keys])
    #     print ('This is the length of:', keys, ":", length)
    #     counting_list = length + counting_list
    # print("There are", counting_list , "structures")
    # print (len(dataframe.index))


    return final_data

def get_num_struct(dataframe):
    """ get the number of released structures from a particular year """
    #from years_ids, get the number of structures and append to years_num.
    years_ids = {}
    for keys in range (len(dataframe.index)):
        if dataframe["releaseDate"][keys][0:4] not in years_ids.keys():
            years_ids[dataframe["releaseDate"][keys][0:4]] = []
            strucutureId = dataframe["structureId"][keys]
            years_ids[dataframe["releaseDate"][keys][0:4]].append(strucutureId)
        else:
            strucutureId = dataframe["structureId"][keys]
            years_ids[dataframe["releaseDate"][keys][0:4]].append(strucutureId)
    a = []
    for keys,values in years_ids.items():
        b = keys, len(list(filter(None, values))) ## takes keys and counts the values in said key
        a.append (b)
    data = pandas.DataFrame (data=a) ## makes a data Fram for future graphing
    # print (data)

    """ Below code makes sure that the number of strucuters remains the same """

    # counting_list = 0
    # for keys in years_ids.keys():
    #     length =  len(years_ids[keys])
    #     print ('This is the length of:', keys, ":", length)
    #     counting_list = length + counting_list
    # print("There are", counting_list , "structures")
    # print (len(dataframe.index))

    return data

def main():
    """ gather the relevant quantities and make the plot """
    # data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
    final_data = data.dropna().reset_index(drop=True)
    # average_weight = get_avg_mw(final_data)
    # number_of_strucuters = get_num_struct(final_data)
    print ('This is the average weight\n', get_avg_mw(final_data))
    print ('This is the number of strucuters\n', get_num_struct(final_data))
    #plotting: x values are dictionary keys, y values are key values

if __name__ == "__main__":
    main()