country='India'       # User Input 1
type_of_analysis=['new_cases', 'new_deaths', 'total_cases',
       'total_deaths', 'weekly_cases', 'weekly_deaths', 'biweekly_cases',
       'biweekly_deaths']   # User Input 2
forecast_period=10  # User Input 3

type_of_analysis={'Number of new cases':'new_cases', 'Number of new deaths':'new_deaths','Total number of cases':'total_cases',
       'Total number of deaths':'total_deaths','Number of weekly cases':'weekly_cases','Number of weekly deaths':'weekly_deaths','Number of biweekly cases':'biweekly_cases',
       'Number of biweekly deaths':'biweekly_deaths'}
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics

df= pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")

df=df[df['location']!='Hong Kong']
df['date']= pd.to_datetime(df['date'],utc=False)
countries=list(set(df.location))
countries.sort()
countries.remove('India')
countries.insert(0,'India')
st.markdown(
            '''
            <link rel="stylesheet"
            href="https://fonts.googleapis.com/css2?family=Suez+One">
            <div style="font-family: 'Suez One';font-size:70px; background-color:white; color:black"><center>Covid-19 Global Predictor</center></div>
            ''',unsafe_allow_html=True
        )
st.header(" ")
st.header("Region-wise predictions")
option1 = st.selectbox("Country",countries)
option2 = st.number_input("Forecast period in days",min_value=1,max_value=30)
option3 = st.selectbox("Select the forecasted variable",list(type_of_analysis.keys()))
if( len(option1) != 0):
    m=Prophet(seasonality_mode='additive',yearly_seasonality=True,weekly_seasonality=True,daily_seasonality=True)
    #,growth='logistic'
    data=df[df['location']==option1][['date',type_of_analysis[option3]]].rename(columns={"date":"ds",type_of_analysis[option3]:"y"})
    #data['floor']=0
    #data['cap']=data['y'].max()+data['y'].mean()
    m.fit(data)
    future=m.make_future_dataframe(periods=option2)
    #future['floor']=0
    #future['cap']=data['y'].max()+data['y'].mean()
    forecast = m.predict(future)
    fig=plot_plotly(m, forecast)
    fig.update_layout(
    title="Forecasting",
    xaxis_title="Date",
    yaxis_title=option3)
    st.plotly_chart(fig,config = {'displayModeBar': False})
    cross_validation_results = cross_validation(m,initial='100 days',horizon="50 days")
    #horizon='5 days'
    #, initial='210 days', period='15 days',
    performance_metrics_results = performance_metrics(cross_validation_results)
    st.write(performance_metrics_results)
    