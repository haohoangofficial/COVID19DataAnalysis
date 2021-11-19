# Import modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Task 02 Importing Covid19 datashet
def main():
    # Task 2.1
    # Load csv file from folder
    corona_dataset_csv = pd.read_csv('Datasets/corona_report.csv',index_col=0)
    corona_dataset_csv = corona_dataset_csv.sort_index()

    # Head
    # print(corona_dataset_csv.head(10))
    # Check the shape of the dataframe
    # print(corona_dataset_csv.shape)

    # Task 2.2 Delete the useless columns
    df = pd.DataFrame(corona_dataset_csv.drop(['day','month','year','popData2019'],axis=1,inplace=True))

    # Task 2.3 Aggregating the rows by the country
    # corona_dataset_aggregated = corona_dataset_csv.groupby('countriesAndTerritories').mean()

    corona_dataset_aggregated = corona_dataset_csv.loc[corona_dataset_csv['countriesAndTerritories'] == 'Afghanistan']
    # corona_dataset_aggregated = corona_dataset_csv.loc['countriesAndTerritories'].mean()
    print(corona_dataset_aggregated)
    # print(corona_dataset_aggregated.shape)
    # print(corona_dataset_aggregated.loc['Afghanistan'])

    # print(corona_dataset_aggregated)
    # print(corona_dataset_aggregated.loc['Afghanistan'])
    # print(corona_dataset_frame.loc['Afghanistan'].shape)

    # Task 2.4 Visualizing data related to a country for example
    # corona_dataset_aggregated.loc['Afghanistan'].plot()
    # plt.plot(corona_dataset_aggregated.loc['Afghanistan'])
    # plt.legend()
    # Task 3 Calculating a good measures
    # corona_dataset_aggregated.loc['Afghanistan'].plot()
    # Task 3.1 Calculating and plotting the first derivative of the curve
    # plt.interactive(False)
    # plt.show(block=True)
    # corona_dataset_aggregated = corona_dataset_csv.groupby('cases').mean()
    # print(corona_dataset_aggregated)
    # Plot cases of Afghanistan
    corona_dataset_aggregated['cases'].plot()
    # Plot deaths of Afghanistan
    corona_dataset_aggregated['deaths'].plot()
    plt.legend()
    plt.show(block=True)
    plt.interactive(False)
if(__name__ == '__main__'):
    main()