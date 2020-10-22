# Covid-19 Global Forecasting

With COVID-19 rising to a pandemic scale, there has been a growing need to understand how to efficiently tackle the situation. In this context, accurate forecasting of the spread of COVID-19 is vital in preparing individuals and countries for what lies ahead.

For this exact purpose, we have created a "Covid-19 Global Forecasting" app - an interactive visualization of the future spread of COVID-19 around the world. Within this dashboard, you can analyse the growth or shrink of Covid-19 cases and deaths based on a region of choice. 

Our future work would involve further exploring into patterns of correlation between age demographics, life expectancy rates and exploration of other factors that may or may not be intuitively obvious to improve our predictive model.

The dashboard is created with Streamlit using Plotly and Matplotlib for visualization and deployed using Heroku. 

The sources of the data used for this app are:
1. [covid.ourworldindata.org](https://ourworldindata.org/coronavirus)

Contributors: [Niegil](https://github.com/Niegil-Francis), [Rishabh](https://github.com/Rishabh-Lalla), [Vishnu](https://github.com/vishnu701) and [Sakthisree](https://github.com/Sakzsee).

Link to access the app: [Covid-19 Global Forecasting](https://covid-prediction.herokuapp.com/).

In order to run the app locally:
1. Install streamlit: pip install streamlit
2. Clone the repository: git clone https://github.com/Niegil-Francis/Covid_pred.git
3. Install the required packages present in requirements.txt
4. Change the directory to Covid_pred and run: streamlit run Covid_prediction.py 

