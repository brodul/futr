from __future__ import print_function

import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class NoMenuForTodayError(Exception):
    pass


class BaseAggregator(object):
    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def get_day_content(self, today=None):
        today = today or datetime.today()
        try:
            daily_content = self.weekly_content[today.date()]
        except KeyError:
            raise NoMenuForTodayError
        else:
            return daily_content


class PivnicaAggregator(BaseAggregator):
    url = "http://www.pivnica-union.si/si/"

    def __init__(self):
        self.weekly_content = {}

        self.html = self.get_html()
        self.rel_elements = self.get_relevant_elements(self.html)
        self.weekly_content = self.get_weekly_content(self.rel_elements)

    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def get_relevant_elements(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.find(class_=("menus", "tab-content"))
        soup = soup.findAll(class_=["tab-pane", "fade"])
        return soup

    def get_weekly_content(self, rel_elements):
        weekly_content = {}
        for day_content in rel_elements:
            raw_date = day_content.attrs['id']
            datetime_object = datetime.strptime(raw_date, '%d%m%Y')
            try:
                weekly_content[datetime_object.date()] = day_content.findAll(
                    class_='menu-wrap')[1]
            except IndexError:
                weekly_content[datetime_object.date()] = ""

        # returns a dict (date: html_str)
        return weekly_content


class PiramidaAggregator(BaseAggregator):
    url = "http://pizzerijapiramida.si/malice/"

    def __init__(self):
        self.weekly_content = {}

        self.html = self.get_html()
        self.rel_elements = self.get_relevant_elements(self.html)
        self.weekly_content = self.get_weekly_content(self.rel_elements)

    def get_relevant_elements(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.findAll(class_=["jsrm-menu-header", "jsrm-table"])
        print(soup)
        return soup

    def get_weekly_content(self, rel_elements):
        weekly_content = {}

        non_decimal = re.compile(r'[^\d.]+')
        today = datetime.today()
        for raw_date, day_content in zip(rel_elements[::2], rel_elements[1::2]):
            raw_date = raw_date.text.strip("-").strip()
            str_date = non_decimal.sub('', raw_date)
            datetime_object = datetime.strptime(str_date, '%d.%m.%y')
            date_object = datetime_object.date().replace(year=today.year)
            weekly_content[date_object] = day_content

        return weekly_content


class MaharajaAggregator(BaseAggregator):
    url = "http://www.maharaja.si/dnevna-kosila"

    def __init__(self):
        self.weekly_content = {}

        self.html = self.get_html()
        self.rel_elements = self.get_relevant_elements(self.html)
        self.weekly_content = self.get_weekly_content(self.rel_elements)

    def get_relevant_elements(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        soup.find_all(text=re.compile("MENU 10:"))[0].parent.parent.next_sibling.next_sibling
        soup = soup.findAll(class_=["jsrm-menu-header", "jsrm-table"])
        print(soup)
        return soup

    def get_weekly_content(self, rel_elements):
        weekly_content = {}

        non_decimal = re.compile(r'[^\d.]+')
        today = datetime.today()
        for raw_date, day_content in zip(rel_elements[::2], rel_elements[1::2]):
            raw_date = raw_date.text.strip("-").strip()
            str_date = non_decimal.sub('', raw_date)
            datetime_object = datetime.strptime(str_date, '%d.%m.%y')
            date_object = datetime_object.date().replace(year=today.year)
            weekly_content[date_object] = day_content

        return weekly_content
