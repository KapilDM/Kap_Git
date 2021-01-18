import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
import plotly
import os,sys

root_path = os.path.dirname(os.getcwd())
sys.path.append(root_path)
sys.path = list(set(sys.path)) 

def total_deaths_year(df):
    """Gives total deaths per year""" 
    df12 = df.groupby(["year"]).count()
    ax = plt.figure()
    sns.set_style("whitegrid")
    ax = sns.barplot(x=df12.index,y=df12["Name"])
    plt.title("Total Fatal Police Shooting in the US", fontdict={"fontweight":"bold"})
    plt.xlabel("Year", fontdict={"fontname":"Comic Sans MS"})
    plt.ylabel("People killed")
    plt.savefig(root_path + "\\resources\\total_deaths_year.png")
    plt.show()

def shot_or_tasered(df): 
    """Manner of Death"""
    shot = df.loc[df["Manner_Of_Death"] == "shot"].count()[0]
    shot_and_Tasered = df.loc[df["Manner_Of_Death"] == "shot and Tasered"].count()[0]
    labels = ["Shot", "Shot and Tasered"]
    colors = ["#3434eb","#eb34c9"]
    plt.pie([shot,shot_and_Tasered], labels= labels, colors=colors, autopct="%.1f %%")    
    plt.title("Manner Of Death")
    plt.savefig(root_path + "\\resources\\shot_or_tasered.png")
    plt.show()

def weapon_carried(df): 
    """Weapon carried when killed"""
    armed_lista = df.groupby(["Armed"]).count() 
    armed_lista1 = armed_lista.sort_values("Name",ascending=False).head(10)
    fig = px.bar(armed_lista1, y=armed_lista1.index, x="Name",
                 color=armed_lista1.index, orientation="h",  
                 color_discrete_sequence=px.colors.sequential.Plasma_r,
                 title="Weapon carried at the moment they were killed", 
                 labels={'Name':'Total amount'})
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\weapon_carried.html")
    fig.show()

def age_distribution(df): 
    """Age of people killed"""
    fig = px.histogram(df["Age"])
    fig.update_traces(marker_line_color='midnightblue', marker_color="lightskyblue", 
                      marker_line_width=1.5)
    fig.update_layout(title="Deaths by age",width=550,showlegend=False, 
                      yaxis_title="Number of People" ,xaxis_title="Age")
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\age_distribution.html")
    fig.show()

def gender_killed(df): 
    """Shows the difference between Male vs Female killed by police"""
    fig = px.pie(df, names='Gender', title='% of Male vs Female killed by police',                     
                   color_discrete_sequence=px.colors.sequential.RdBu)
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\gender_killed.html")               
    fig.show()

def total_race(df):
    """Total population killing by race in the US"""
    cant_dif = df.Race.value_counts(normalize=True)
    cant_dif.index = ['White', 'Black', 'Hispanic', 'Asian', 'Native American',"Other"]
    ax = plt.figure(figsize=(7,3))
    ax = sns.barplot(x=cant_dif.index, y=cant_dif.values,palette="rocket")
    plt.title("Total Police Shooting by Race", fontdict={"fontweight":"bold"})
    plt.xlabel("Race", fontdict={"fontweight":"bold"})
    plt.ylabel("Frequency", fontdict={"fontweight":"bold"})
    plt.savefig(root_path + "\\resources\\total_race.png")
    plt.show()


def most_shooting_cities(df): 
    """Cities where more Police Shooting were registered"""
    df_cities = pd.DataFrame({"City":df.City, "tot_count":1})
    most_dang_cities = df_cities.groupby("City").count().sort_values("tot_count",
    ascending=False)
    most_dang_cities = most_dang_cities.head(5)
    plt.figure(figsize=(8,4))
    ax = sns.barplot(data=most_dang_cities, x=most_dang_cities.index, y="tot_count")
    ax.set(xlabel="City", ylabel = "Amount People Killed")
    plt.title("Top 5 cities with more Police Shooting", fontsize=17)
    plt.savefig(root_path + "\\resources\\most_shooting_cities.png")
    plt.show()


def mapa_killings_states(df):
    """States where more police Shooting were registered""" 
    indice = df.State.value_counts().index
    tamanio = list(df.State.value_counts())
    new_df = pd.DataFrame({"State":indice, "Shootings":tamanio})
    fig = go.Figure(data=go.Choropleth(locations=new_df['State'],
                    z = new_df['Shootings'], locationmode = 'USA-states', 
                    colorscale = 'Reds', colorbar_title = "Shootings",))
    fig.update_layout(title_text = 'Total shooting in the USA',
                      geo_scope='usa',)
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\mapa_killing_states.html")
    fig.show()


def threat_level(df):
    """Level of threat"""
    fig = px.pie(df, names='Threat_Level', title='Threat Level',
                 color_discrete_sequence=["Purple", "green", "blue"])
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\threat_level.html")
    fig.show()


def finished_hs(df):
    """Population that has finished high school"""
    amount_appearence = df.groupby("State").count()
    Hs_tot = df.groupby("State").sum()["Percent_Completed_Hs"]
    df_nue = pd.DataFrame({"State":amount_appearence.index, "High School" : Hs_tot,
                           "Dividir" : amount_appearence["Name"]})
    df_nue["High School"] = df_nue["High School"]/df_nue["Dividir"]
    df_nue = df_nue.sort_values("High School",ascending=False)
    df_nue = df_nue.tail(10)
    ax = plt.figure(figsize=(10,6))
    ax = sns.barplot(x=df_nue["State"], y=df_nue["High School"], orient="v")
    ax.set_xlabel("States", fontsize=12)
    ax.set_ylabel("Percentage", fontsize=12)
    ax.set_title("Amount of people with High School finished", fontsize = 15);
    plt.savefig(root_path + "\\resources\\finished_hs.png")

def poverty_rate_func(df):
    """States with highest Poverty Rates"""
    amount_appearence = df.groupby("State").count()
    pov_tot = df.groupby("State").sum()["Poverty_Rate"]
    df_nue = pd.DataFrame({"State":amount_appearence.index, "Poverty Rate" : pov_tot ,
                          "Dividir" : amount_appearence["Name"]})
    df_nue["Poverty Rate"] = df_nue["Poverty Rate"]/df_nue["Dividir"]
    df_nue.sort_values("Poverty Rate",ascending=False)
    df_nue = df_nue.head(5)
    fig = go.Figure(data=go.Choropleth(locations=df_nue["State"],
                    z = df_nue["Poverty Rate"], locationmode = 'USA-states', 
                    colorscale = 'Reds', colorbar_title = "Poverty Rate",))
    fig.update_layout(title_text = 'States with the highest Poverty Rate',
                      geo_scope='usa',)
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\poverty_rate_func.html")
    fig.show()

def amount_race_shot(df):
    """Amount of people killed of a race over total race population"""
    df_nuevo = df.copy()
    df_nuevo.Race.value_counts()
    deci = df_nuevo.Race.value_counts(normalize=True)
    df_nuevo.drop_duplicates(subset ="City", 
                     keep = False, inplace = True)

    lista = [df_nuevo["Share_White"].mean(),df_nuevo["Share_Black"].mean(), 
    df_nuevo["Share_Native_American"].mean() , df_nuevo["Share_Asian"].mean(),
    df_nuevo["Share_Hispanic"].mean()]

    lista_razas = ["Share_White","Share_Black","Share_Native_American","Share_Asian",
    "Share_Hispanic"]

    df_tot_pob = pd.DataFrame({"Race":lista_razas, "Population Percentage": lista})

    vari = df.Race.value_counts(normalize=True)
    vari_porcen = vari*100

    df_tot_pob["Death Percentage"] = [vari_porcen[0],vari_porcen[1],vari_porcen[4],
    vari_porcen[3],vari_porcen[2]]

    df_tot_pob = df_tot_pob.set_index("Race")
    df_tot_pob["Frecuency"] = df_tot_pob["Death Percentage"]/df_tot_pob["Population Percentage"]
    df_tot_pob = df_tot_pob.sort_values("Frecuency",ascending=False)

    ax =plt.figure(figsize=(9,4))
    ax = sns.barplot(x=df_tot_pob.index, y=df_tot_pob.Frecuency,palette="Reds_r")
    ax.set_title("Amount of people killed over total population of the race in the US",fontsize = 15);
    ax.set_xlabel("Race", fontsize=15)
    ax.set_ylabel("Frequency", fontsize=15)
    plt.savefig(root_path + "\\resources\\amount_race_shot.png")


def relation_poverty_black_deaths(df):
    """Function to know if there is a relation between amount of black people killed
    and the poverty rate of a state"""
    amount = df.groupby("State").count()
    pv_tot = df.groupby("State").sum()["Poverty_Rate"]
    black_tot = df.groupby("State").sum()["Share_Black"]
    df_ = pd.DataFrame({"State":amount.index,"Poverty Rate":pv_tot,"Share_Black_Killed":black_tot,"Dividir":amount["Name"]})
    df_["Poverty Rate"] = df_["Poverty Rate"]/df_["Dividir"]
    df_["Share_Black_Killed"] = df_["Share_Black_Killed"]/df_["Dividir"]
    fig = px.scatter(df_, x=df_.index, y="Share_Black_Killed", color="Poverty Rate",
             color_discrete_sequence=["red", "blue"],
             title="Share Black killed in relation with Poverty Rate")
    fig.update_layout(yaxis_title="Amount of black people killed (%)" ,xaxis_title="States")
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\relation_poverty_black_deaths.html")
    fig.show()

def project_step_time():
    "Pie chart to show the time spent on each step of the project"
    Research = 10
    Get_Data = 10
    Data_Wrangling = 10
    Data_Mining = 35
    Visualization = 35
    labels = ["Research", "Get Data", "Data Wrangling", "Data Mining","Visualization"]
    colors = ["#e5eb34","#34eb56", "#34ebbd", "#348feb", "#ae34eb"]
    plt.pie([Research,Get_Data,Data_Wrangling, Data_Mining, Visualization], labels= labels,        colors=colors, autopct="%.1f %%")    
    plt.title("Time needed for each project step")
    plt.savefig(root_path + "\\resources\\project_step_time.png")
    plt.show()


def mapa_killings_states_blacks(df):
    """States with police Shooting against black people""" 
    indice = df.State.value_counts().index
    tamanio = list(df.State.value_counts())
    new_df = pd.DataFrame({"State":indice, "Shootings":tamanio})
    fig = go.Figure(data=go.Choropleth(locations=new_df['State'],
                    z = new_df['Shootings'], locationmode = 'USA-states', 
                    colorscale = 'Reds', colorbar_title = "Shootings",))
    fig.update_layout(title_text = 'Total shooting in the USA',
                      geo_scope='usa',)
    #plotly.offline.plot(fig, filename= root_path + "\\resources\\mapa_killing_states.html")
    fig.show()


def correlate(df):
    """Correlation Matrix, heatmap"""
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True,cmap= 'coolwarm', linewidths=2)
    plt.title("Correlation Fatal Police Shooting in the USA")
    plt.savefig(root_path + "\\resources\\correlate.png")
    plt.show()
    