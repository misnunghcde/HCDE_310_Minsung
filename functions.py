import urllib.request
import json
from urllib.parse import quote

def get_country_info(country):

    country_encoded = quote(country)

    url = f"https://restcountries.com/v3.1/name/{country_encoded}?fullText=true"

    try:
        with urllib.request.urlopen(url) as response:

            data = response.read()

            countries = json.loads(data)

            country_info = countries[0]

            info_dict = {
                'name': country_info['name']['common'],
                'capital': country_info['capital'][0],
                'location': country_info['region'],
                'languages': ', '.join(country_info['languages'].values()),
                'flag': country_info['flags']['png'],
                'country_code': country_info['cca3'],
                'population': country_info['population'],
                'currency': ', '.join([f"{value['name']} ({key})" for key, value in country_info['currencies'].items()]),
                "timezones" : country_info["timezones"]
            }
            return info_dict

    except urllib.error.HTTPError:
        return None

def get_exchange_rate(currenty_country, target_country):
    current_country_dict = get_country_info(currenty_country)
    target_country_dict = get_country_info(target_country)
    index_start_base = current_country_dict["currency"].find("(")
    base_currency = current_country_dict["currency"][index_start_base + 1 : index_start_base + 4]
    index_start_target = target_country_dict["currency"].find("(")
    target_currency = target_country_dict["currency"][index_start_target+1 : index_start_target + 4]

    exchange_rate_url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        with urllib.request.urlopen(exchange_rate_url) as response:

            exchange_data = response.read()

            exchange_rates = json.loads(exchange_data)

            exchange_rate = exchange_rates['rates'][target_currency]

            return exchange_rate

    except urllib.error.HTTPError:
        return None


