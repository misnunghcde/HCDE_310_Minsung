from flask import (Flask, render_template, request)
from functions import get_country_info, get_exchange_rate



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'POST':
        current_country = request.form['current_country']
        target_country = request.form['target_country']
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == 'POST':

        current_country = request.form['current_country']
        country_info_dict = get_country_info(current_country)
        target_country = request.form['target_country']
        target_info_dict = get_country_info(target_country)

        if country_info_dict is None or target_info_dict is None:
            return render_template('error.html')

        current_name = country_info_dict["name"]
        current_capital = country_info_dict["capital"]
        current_languages = country_info_dict["languages"]
        current_flag = country_info_dict["flag"]
        current_country_code = country_info_dict["country_code"]
        current_population = country_info_dict["population"]
        current_currency = country_info_dict["currency"]

        target_name = target_info_dict["name"]
        target_capital = target_info_dict["capital"]
        target_languages = target_info_dict["languages"]
        target_flag = target_info_dict["flag"]
        target_country_code = target_info_dict["country_code"]
        target_population = target_info_dict["population"]
        target_currency = target_info_dict["currency"]

        exchange_rate = get_exchange_rate(current_country, target_country)

        current_country = request.form['current_country']
        country_info_dict = get_country_info(current_country)
        return render_template("results.html",
                               current_name = current_name,
                               current_capital = current_capital, current_languages = current_languages,
                               current_flag = current_flag, current_country_code = current_country_code,
                               current_population = current_population, current_currency = current_currency,
                               target_name = target_name, target_capital = target_capital, target_languages = target_languages,
                               target_flag= target_flag, target_country_code = target_country_code, target_population = target_population,
                               target_currency = target_currency, exchange_rate = exchange_rate)

if __name__ == '__main__':
    app.run(debug=True)



