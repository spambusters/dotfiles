#!/usr/bin/python

import logging
import os

import requests
from bs4 import BeautifulSoup

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(BASE_PATH, 'weather.log'),
                    level=logging.INFO,
                    format='%(levelname)s %(asctime)s - %(message)s',
                    filemode='a')
LOGGER = logging.getLogger('weather')

USER_AGENT = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) '
              'Gecko/20100101 Firefox/52.0')
LAT = ''
LONG = ''


def main():
    """Retrieve the current weather temperature to display in polybar.

    The future forecast will also be saved to weather-current.txt in
    the polybar folder. This can be displayed in the default GUI
    text editor (e.g. Leafpad) by left clicking the temperature in polybar.

    Current temperature and any errors are logged to weather.log

    """
    if not LAT or not LONG:
        raise WeatherError('You forgot to enter LAT/LONG in weather.py')

    url = f'https://forecast.weather.gov/MapClick.php?lat={LAT}&lon={LONG}'
    try:
        resp = requests.get(url,
                            headers={'User-Agent': USER_AGENT},
                            timeout=10)
        if resp.status_code != 200:
            raise WeatherError(f'Response was {resp.status_code}')
    except requests.exceptions.RequestException as err:
        raise WeatherError(err)

    soup = BeautifulSoup(resp.text, 'html5lib')

    forecast_rows = soup.find_all('div', class_='row-forecast')
    if forecast_rows:
        with open(os.path.join(BASE_PATH, 'weather-current.txt'), 'w') as file:
            for row in forecast_rows:
                day = row.find('div', class_='forecast-label').text
                info = row.find('div', class_='forecast-text').text
                file.write(f'{day}: {info}\n\n')

    temperature = soup.find('p', class_='myforecast-current-lrg').text
    if temperature:
        print(temperature)
        LOGGER.info(temperature)
    else:
        raise WeatherError('Error parsing the temperature from soup')


class WeatherError(Exception):
    """Custom exception for weather errors"""

    def __init__(self, err):
        super().__init__()
        print('Error: check weather.log')
        LOGGER.critical(err)


if __name__ == '__main__':

    main()
