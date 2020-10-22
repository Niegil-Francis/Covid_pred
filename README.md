# Covid-19 Global Forecasting

Amidst the unfortunate chaos of COVID-19 around the world, there has been an overload of information regarding the pandemic present online. With such massive amounts of data, it is crucial not only to identify and collect verified information, but to also structure it in a way that allows us to pick worthy insights. In this context, data visualization is perfect for enabling quick and accurate comprehension of information, whilst providing the relevant insights into our current global situation.

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
4. Change the directory to Covid_App and run: streamlit run Covid_dash.py 

