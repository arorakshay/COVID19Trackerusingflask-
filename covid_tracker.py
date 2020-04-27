from flask import Flask, flash, redirect, url_for, render_template, request, session, abort
import time
from datetime import datetime
import os
import requests,json, random

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(12)

@app.route("/")
@app.route("/home")
def home():
    return redirect(url_for('covid19')) 

@app.route("/covid19", methods = ["GET","POST"])
def covid19():
    try: 
        country_name = request.form.get("country")
        print(country_name)
        
        if country_name==None:
            country_url =  "https://corona.lmao.ninja/v2/countries/india"
            country_name = "India"
        else:
            country_url =  "https://corona.lmao.ninja/v2/countries/"+country_name
        
        country_content = requests.get(country_url)
        country_data = country_content.json()


        worldwide_data_url = "https://corona.lmao.ninja/v2/all"
        worldwide_content = requests.get(worldwide_data_url)
        corona_data = worldwide_content.json()
        print("*\n"*5, corona_data) 
        print(type(corona_data)) 
        tm = corona_data['updated']/1000

        corona_data
        ts = 1586783891980 / 1000
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tm)) #("%Y-%m-%d %H:%M:%S")
        #timestamp = corona_data['updated']
        
        d1 = {'updated' : tm}
        corona_data.update(d1)


        date_cases = []
        date_count = []

        date_count_deaths = []

        date_count_recovered = []

        final_date_all = []
        final_count_all = []

        final_count_deaths = []
        final_count_recovered = []

        worldwide_hist_url = "https://corona.lmao.ninja/v2/historical/all"
        worldwide_hist_content = requests.get(worldwide_hist_url)
        corona_hist_data = worldwide_hist_content.json() 


        # To get total number of cases
        #print((corona_hist_data['cases']))
        dict = (corona_hist_data['cases'])
        for key, value in dict.items():
            date_cases.append(key)
            date_count.append(value)
        hist_date_all = date_cases[-1:-30:-5]#.append(date_cases[-1]) 
        hist_count_all =date_count[-1:-30:-5]
        for i in reversed(hist_count_all):
            final_count_all.append(i)
        #print(final_count_all)
        for i in reversed(hist_date_all):
            final_date_all.append(i)
        #print(final_date_all)


        #To get total number of deaths
        #print((corona_hist_data['deaths']))
        dict1 = (corona_hist_data['deaths'])
        for key, value in dict1.items():
            date_count_deaths.append(value)
        hist_count_all_deaths =date_count_deaths[-1:-30:-5]
        for i in reversed(hist_count_all_deaths):
            final_count_deaths.append(i)
        #print(final_count_deaths)

        #To get total number of recovered global
        #print((corona_hist_data['recovered']))
        dict2 = (corona_hist_data['recovered'])
        for key, value in dict2.items():
            date_count_recovered.append(value)
        hist_count_all_recovered =date_count_recovered[-1:-30:-5]
        for i in reversed(hist_count_all_recovered):
            final_count_recovered.append(i)
        #print(final_count_recovered)


        if country_name==None:
            country_url_hist =  "https://corona.lmao.ninja/v2/historical/india"
            country_name = "India"
        else:
            country_url_hist =  "https://corona.lmao.ninja/v2/historical/"+country_name


        country_content_hist = requests.get(country_url_hist)
        country_data_hist = country_content_hist.json()


        print(country_data_hist) 

        date_cases_country = []
        date_count_country = []

        date_count_deaths_country = []

        date_count_recovered_country = []

        final_date_all_country = []
        final_count_all_country = []

        final_count_deaths_country = []
        final_count_recovered_country = []

       
        #To get total number of cases in specific countries
        #print((corona_hist_data['cases']))
        country_dict = (country_data_hist['timeline']['cases'])
        for key, value in country_dict.items():
            date_cases_country.append(key)
            date_count_country.append(value)
        hist_date_all_country = date_cases_country[-1:-30:-5]#.append(date_cases[-1]) 
        hist_count_all_country =date_count_country[-1:-30:-5]
        for i in reversed(hist_count_all_country):
            final_count_all_country.append(i)
        #print(final_count_all)
        for i in reversed(hist_date_all_country):
            final_date_all_country.append(i)
        #print(final_date_all)
        print(final_count_all_country)
        print(final_date_all_country)


        #To get total number of deaths in specific country
        #print((corona_hist_data['deaths']))
        country_dict1 = (country_data_hist['timeline']['deaths'])
        for key, value in country_dict1.items():
            date_count_deaths_country.append(value)
        hist_count_all_deaths_country =date_count_deaths_country[-1:-30:-5]
        for i in reversed(hist_count_all_deaths_country):
            final_count_deaths_country.append(i)
        #print(final_count_deaths)

        #To get total number of recovered in specific country
        #print((corona_hist_data['recovered']))
        country_dict2 = (country_data_hist['timeline']['recovered'])
        for key, value in country_dict2.items():
            date_count_recovered_country.append(value)
        hist_count_all_recovered_country =date_count_recovered_country[-1:-30:-5]
        for i in reversed(hist_count_all_recovered_country):
            final_count_recovered_country.append(i)
        #print(final_count_recovered)'''


        return render_template("covid.html", data=corona_data, country_name = country_name, country_data = country_data,values=final_count_all, labels=final_date_all,
                              final_count_deaths=final_count_deaths,final_count_recovered=final_count_recovered,
                              final_date_all_country=final_date_all_country,final_count_all_country=final_count_all_country,
                              final_count_deaths_country=final_count_deaths_country, 
                              final_count_recovered_country=final_count_recovered_country)

    except Exception as e:
        print("Exception: \n"*5, e)
        return redirect(url_for('covid19'))   

if __name__ == "__main__":
    app.run(debug=True) 