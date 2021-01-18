import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def capitalize_first_letter_column(df): 
    """Capitalizing all the column names"""
    df.columns.str.title()
    df.columns = df.columns.str.title()
    return df

def changing_dates(df): 
    """changing the date type to datatime, extracting the year and making a new column
    with the year data"""
    df['Date'] = df['Date'].astype('datetime64[ns]')
    df['year'] = pd.DatetimeIndex(df['Date']).year
    return df

def merge_kill_social(df,df2): 
    """Merging the final dataframe"""
    df["City"].replace(["city", "CDP", "town"], "", regex=True, inplace=True)
    for i in range(len(df["City"])):
        df["City"][i] = df["City"][i].strip()
    total_merge = pd.merge(df2, df, on=["State","City"], how="outer")
    total_merge.dropna(inplace=True)
    return total_merge

def renaming_row_race_values(df): 
    """Renaming race columns to have a clearer visualization"""
    df['Race'] = df['Race'].replace(['B','A', 'W', 'O', 'H', 'N'], 
    ['Black', 'Asian', 'White', 'Other', 'Hispanic', 'Native America'])
    return df


def merging_dataframes(df,df1,df2):#,df3): 
    """Merging all the dataframes that can be merged in the database"""
    merging1 = df.merge(df1,on=["Geographic Area","City"])
    merging2 = merging1.merge(df2,on=["Geographic Area","City"])
    #merging3 = merging2.merge(df3,on=["Geographic Area","City"])
    return merging2 


def counting_nulls(df): 
    return df.isnull().sum()


def percent_missing_values(df):
     miss = df.isnull().sum() * 100 / len(df)
     return miss


def drop_columns_killing_df(df): 
    df = df.drop(["Id","Signs_Of_Mental_Illness", "Flee", "Body_Camera"], axis=1)
    return df

#Only keeping rows with values, not keeping NaN values
def drop_nan_rows(df,df_column):
   df_final = df[df_column.notna()]
   return df_final

def age_complete(df_column):
    df_column = df_column.fillna(value=df_column.mean(),inplace=True)
    return df_column


def delete_2_word_city(df):
    df['City_nuevo'] = df['City'].str.split(' ').str[0]
    df["City"] = df["City_nuevo"]
    del df["City_nuevo"]
    return df


def renaming_cols(df): 
    df = df.rename(columns={'Geographic Area': 'State'})
    return df


def transform_to_numeric(df,col):
    df1 = df[col].replace(['(X)'],0.0,inplace = True)
    df1 = df[col].astype(float)
    return df1

def transform_to_numeric_normal(df,col):
    df1 = df[col].replace(['(X)'],0.0,inplace = True)
    return df1


def replacing_non_numeric2(df,col):
    df = df[col].replace(["-"],0.0,inplace = True)
    return df


def pasando_a_nans(df):
    """Deleting unnecesary strings"""
    for pos,val in enumerate(df.columns):
        if pos >= 2:
            df[df.columns[pos]] = df[df.columns[pos]].replace("(X)", np.NaN)
            df[df.columns[pos]] = df[df.columns[pos]].replace("-", np.NaN)
            #df.dropna(inplace = True)
            df[df.columns[pos]] = df[df.columns[pos]].astype(float)
    return df