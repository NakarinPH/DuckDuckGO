# Nakarin Philangam
# 11/05/2022
import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

# get data
resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
# read data into a variable
rsp_data = resp.json()

related_topics = rsp_data['RelatedTopics']
# create a list for storing data
president_list = []
for data in related_topics:
    president_list.append(data['Text'])

president = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Van Buren',
             'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
             'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'McKinley',
             'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman',
             'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
             'Clinton', 'Obama', 'Trump', 'Biden']


@pytest.mark.parametrize("presidents", president)
def test_ddg0(presidents):
    for data in president_list:
        if presidents in data:
            assert president in related_topics
