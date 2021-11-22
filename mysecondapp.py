import streamlit as st
import numpy as np
import pandas as pd


st.title("Movie/TV Show Recommendation App ✨")

st.markdown("""
This web app simply recommend some Movie or TV Show for the user according to their preferences. Hope enjoy my simple web app!!
* **Data Source:** [Netflix-Movies-and-TV-Shows.kaggle](https://www.kaggle.com/satpreetmakhija/netflix-movies-and-tv-shows-2021)
""" )

st.balloons()

df = pd.read_csv('netflixData.csv')
df = df.drop(['Show Id','Director','Date Added','Cast','Production Country','Duration'], axis = 1)
df = df.dropna(axis = 0, how ='any')
df = df.rename(columns={'Release Date': 'Year','Content Type':'Type'})
df.drop(df[df.Rating == 'R'].index, inplace=True)
df.drop(df[df.Rating == 'TV-MA'].index, inplace=True)
df = df.astype({"Year": int})
df.drop(df[df.Year < 2010].index, inplace=True)
#st.dataframe(df)



st.sidebar. write('Prepared by : Fatin Arisya Binti Azhar')




#Type

option = st.sidebar.selectbox(
    'Select Type',
     ['TV Show','Movie'])

if option=='TV Show':
    rslt_df = df.loc[df['Type'] == 'TV Show']
   

else:
    rslt_df = df.loc[df['Type'] == 'Movie']
   

#year

values = st.sidebar.slider('Pick a year', 2010, 2021)

if  values==2010:
    rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2010]
    

elif values==2011:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2011]
     

elif values==2012:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2012]
     

elif values==2013:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2013]
     

elif values==2014:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2014]
        

elif values==2015:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2015]
     

elif values==2016:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2016]
     

elif values==2017:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2017]
     

elif values==2018:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2018]
     

elif values==2019:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2019]
     

elif values==2020:
     rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2020]
     

else:
    rslt_df_1 = rslt_df.loc[rslt_df['Year'] == 2021]
    st.dataframe(rslt_df_1)




#Genres

option = st.sidebar.selectbox(
    'Select Genres',
     ['Stand-Up Comedy','Dramas, International Movies','Comedies, Dramas, International Movies','Documentaries','Dramas, Independent Movies, International Movies','All'])



if  option=='Stand-Up Comedy':
    rslt_df_2 = rslt_df_1.loc[rslt_df['Genres'] =='Stand-Up Comedy']
    st.dataframe(rslt_df_2)

elif option=='Dramas, International Movies':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Genres'] =='Dramas, International Movies']
     st.dataframe(rslt_df_2)

elif option=='Comedies, Dramas, International Movies':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Genres'] =='Comedies, Dramas, International Movies']
     st.dataframe(rslt_df_2)

elif option=='Documentaries':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Genres'] =='Documentaries']
     st.dataframe(rslt_df_2)

elif option=='Dramas, Independent Movies, International Movies':
     rslt_df_2 = rslt_df_1.loc[rslt_df['Genres'] =='Dramas, Independent Movies, International Movies']
     st.dataframe(rslt_df_2)

else:
     st.dataframe(rslt_df_1)


