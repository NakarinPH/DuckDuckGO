import requests

import pytest
import pprint
import json

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    # assert "DuckDuckGo" in rsp_data["Heading"]
    assert "Presidents of the united states" in rsp_data["Heading"]
    assert "Washington" in rsp_data["RelatedTopics"][0]["Result"]
    assert "Adams" in rsp_data["RelatedTopics"][1]["Result"]
    assert "Jefferson" in rsp_data["RelatedTopics"][2]["Result"]
    assert "Madison" in rsp_data["RelatedTopics"][3]["Result"]
    assert "Monroe" in rsp_data["RelatedTopics"][4]["Result"]
    assert "Adams" in rsp_data["RelatedTopics"][5]["Result"]
    assert "Jackson" in rsp_data["RelatedTopics"][6]["Result"]
    assert "Buren" in rsp_data["RelatedTopics"][7]["Result"]
    assert "Harrison" in rsp_data["RelatedTopics"][8]["Result"]
    assert "Tyler" in rsp_data["RelatedTopics"][9]["Result"]
    assert "Polk" in rsp_data["RelatedTopics"][10]["Result"]
    assert "Taylor" in rsp_data["RelatedTopics"][11]["Result"]
    assert "Filmore" in rsp_data["RelatedTopics"][12]["Result"]
    assert "Pierce" in rsp_data["RelatedTopics"][13]["Result"]
    assert "Buchanan" in rsp_data["RelatedTopics"][14]["Result"]
    assert "Lincoln" in rsp_data["RelatedTopics"][15]["Result"]
    assert "Johnson" in rsp_data["RelatedTopics"][16]["Result"]
    assert "Grant" in rsp_data["RelatedTopics"][17]["Result"]
    assert "Hayes" in rsp_data["RelatedTopics"][18]["Result"]
    assert "Garfield" in rsp_data["RelatedTopics"][19]["Result"]
    assert "Arthur" in rsp_data["RelatedTopics"][20]["Result"]
    assert "Cleveland" in rsp_data["RelatedTopics"][21]["Result"]
    assert "Harrison" in rsp_data["RelatedTopics"][22]["Result"]
    assert "Mckinley" in rsp_data["RelatedTopics"][23]["Result"]
    assert "Roosevelt" in rsp_data["RelatedTopics"][24]["Result"]
    assert "Taft" in rsp_data["RelatedTopics"][25]["Result"]
    assert "Wilson" in rsp_data["RelatedTopics"][26]["Result"]
    assert "Harding" in rsp_data["RelatedTopics"][27]["Result"]
    assert "Coolidege" in rsp_data["RelatedTopics"][28]["Result"]
    assert "Hoover" in rsp_data["RelatedTopics"][29]["Result"]
    assert "Truman" in rsp_data["RelatedTopics"][30]["Result"]
    assert "Eisenhower" in rsp_data["RelatedTopics"][31]["Result"]
    assert "Kennedy" in rsp_data["RelatedTopics"][32]["Result"]
    assert "Johnson" in rsp_data["RelatedTopics"][33]["Result"]
    assert "Nixon" in rsp_data["RelatedTopics"][34]["Result"]
    assert "Ford" in rsp_data["RelatedTopics"][35]["Result"]
    assert "Carter" in rsp_data["RelatedTopics"][36]["Result"]
    assert "Reagan" in rsp_data["RelatedTopics"][37]["Result"]
    assert "Bush" in rsp_data["RelatedTopics"][38]["Result"]
    assert "Clinton" in rsp_data["RelatedTopics"][39]["Result"]
    assert "Obama" in rsp_data["RelatedTopics"][40]["Result"]
    assert "Trump" in rsp_data["RelatedTopics"][41]["Result"]
    assert "Biden" in rsp_data["RelatedTopics"][42]["Result"]


test_ddg0()
