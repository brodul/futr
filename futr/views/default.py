import re
from datetime import datetime

from pyramid.view import view_config
from bs4 import BeautifulSoup
import requests

non_decimal = re.compile(r'[^\d.]+')


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    response = requests.get("http://www.pivnica-union.si/si/")
    soup = BeautifulSoup(response.text, 'html.parser')
    nom = soup.find(class_="foodDayMenu")
    nom = nom.findAll(class_=["foodDayMenuBlockTitle", "foodDayMenuBlock"])
    # import ipdb; ipdb.set_trace()
    for raw_date, meni in zip(nom[::2], nom[1::2]):
        raw_date = raw_date.text.strip("-").strip()
        str_date = non_decimal.sub('', raw_date)
        datetime_object = datetime.strptime(str_date, '%d.%m.%Y')
        if datetime_object.date() == datetime.today():
            break

    return {'union': ((raw_date, meni),)}
