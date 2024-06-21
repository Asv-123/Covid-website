import plotly.express as px
import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return data
    st.write(data)
    var = st.sidebar.checkbox('Show raw data')
    st.write(var)
def proccess_data(data):
    new_data = (data.melt(id_vars = ['Province/State','Country/Region','Lat','Long'], var_name = 'Data',value_name= 'Confirmed'))
    new_data['Date'] = pd.to_datetime(new_data['Data'])
    return new_data

def select_country(data):
    unique_data = data['Country/Region'].unique()
    drop_list = st.sidebar.selectbox('Select a country',unique_data)
    return drop_list

def filter_data_by_country(data,country):
    filtered_data = data[data['Country/Region'] == country ]
    return filtered_data

def plot_line_graph(data,country):
    fig = px.line(data,x  = 'Data', y = 'Confirmed',title = 'Covid-19 Cases from')
    st.plotly_chart(fig)

def plot_3d(data,country):
    fig = px.scatter_3d(data,x='Data',y='Confirmed',z='Long',color='Confirmed',title='3D-Scatter plot of confirmed covid cases')
    st.plotly_chart(fig)



def main():
    raw_data = load_data()
    new_Date = proccess_data(raw_data)

    var = st.sidebar.checkbox('Show raw data')
    if var == True:
        st.write('Raw data')
        st.write(raw_data)
    else:
        st.write('Processed Data')
        st.write(new_Date)
    country = select_country(new_Date)

    filtered_data = filter_data_by_country(new_Date,country)
    st.write(filtered_data)
    plot_line_graph(filtered_data,country)
    plot_3d(filtered_data,country)






main()
