import pandas
import matplotlib.pyplot as mpl
from statistics import mean
import urllib

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
    struct_data = []
    for keys,values in years_ids.items():
        data = keys, len(values) ## takes keys and counts the values in said key
        struct_data.append (data)
    final_data = pandas.DataFrame (data=struct_data) ## makes a data Fram for future graphing
    return final_data

def main():
    """ gather the relevant quantities and make the plot """
    try:
        data = pandas.read_csv("http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=*&customReportColumns=structureId,releaseDate,structureMolecularWeight,macromoleculeType&service=wsfile&format=csv")
        final_data = data.dropna().reset_index(drop=True)
        average_weight = get_avg_mw(final_data)
        number_of_structures = get_num_struct(final_data)
        plotting_data = pandas.concat([average_weight, number_of_structures[1]], axis=1 )
        plotting_data.columns = ["Year", "Average molecular weight", "Number of structures"]
        print("Average weight\n", average_weight)
        print("Number of structures\n", number_of_structures)
        plotting_data.sort_values(by="Year", axis=0, inplace=True)
        print("This is the dataframe for plotting\n", plotting_data)
        fig = mpl.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        width=0.3
        plotting_data.plot(x = "Year", y = "Average molecular weight", kind = "bar", ax = ax1, position=1, color="red", width=width, label="Average molecular weight")
        plotting_data.plot(x = "Year", y = "Number of structures", kind = "bar", ax = ax2, position=0, color="blue", width=width, label="Number of structures")
        ax1.set_title("Number of structures deposited and average molecular weight by year \n")
        ax1.set_ylabel("Average molecular weight")
        ax1.set_ylim(0,plotting_data.max(axis=0)["Average molecular weight"]+20000)
        ax1.legend(loc="upper left")
        ax2.set_ylabel("Number of structures")
        ax2.set_ylim(0,plotting_data.max(axis=0)["Number of structures"]+2000)
        mpl.show()
    except urllib.error.URLError:
        print("Please make sure you are connected to the Internet.")
        exit()

if __name__ == "__main__":
    main()