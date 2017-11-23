"""
module docstring

http://david.abcc.ncifcrf.gov/api.jsp?type=xxxxx&ids=XXXXX,XXXXX,XXXXXX,&tool=xxxx&annot=xxxxx,xxxxxx,xxxxx,
"""

import os
import valid_values
import pandas as pd
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_html(id_type, ids, annot, tool="chartReport"):
    """
    docstring

    Parameters:
    -----------
    id_type:
        one of DAVID recognised gene types

    ids:
        a list of user's gene IDs, separated

    tool:
        one of DAVID tool names

    annot:
        a list of desired annotation categories


    Returns:
    --------
    html dump
    """
    _check_arguments(id_type, tool, annot)
    # use firefox in headless mode to parse webpage
    # can't use requests.get as there's a load of javascript that needs
    # to run before the page is actually loaded
    os.environ["MOZ_HEADLESS"] = "1"
    binary = FirefoxBinary("/usr/bin/firefox")
    driver = webdriver.Firefox(firefox_binary=binary)
    # if passed a list, convert to a string separated by commas
    if isinstance(ids, list):
        ids = ",".join(ids)
    if isinstance(annot, list):
        annot = ",".join(annot)
    url_prefix = "http://david.abcc.ncifcrf.gov/api.jsp?"
    url = "{prefix}type={id_type}&ids={ids},&tool={tool}&annot={annot}".format(
            prefix = url_prefix, id_type = id_type, ids=ids, tool=tool,
            annot=annot)
    print("Fetching url: \n {}".format(url))
    driver.get(url)
    return driver.page_source


def _check_arguments(id_type, tool, annot):
    """docstring"""
    if id_type not in valid_values.ID_TYPES:
        raise ValueError("Invalid id_type.")
    if tool not in valid_values.TOOLS:
        raise ValueError("Invalid tool")
    if isinstance(annot, str):
        if annot not in valid_values.ANNOT:
            raise ValueError("Invalid annot: {}".format(annot))
    if isinstance(annot, list):
        incorrect = []
        for i in annot:
            if i not in valid_values.ANNOT:
                incorrect.append(i)
        if len(incorrect) > 0:
            raise ValueError("Invalid annot: {}".format(incorrect))


def get_data_from_html(html):
    """docstring"""
    david_url_prefix = "https://david.ncifcrf.gov"
    soup = BeautifulSoup.BeautifulSoup(html)
    for link in soup.findAll("a"):
        tmp_url = link.get("href")
        if tmp_url.startswith("data/download/chart_"):
            url_suffix = tmp_url
            break
    chart_url = os.path.join(david_url_prefix, url_suffix)
    return pd.read_table(chart_url)


# TODO: proper arguments
def get_table(*args, **kwargs):
    """docstring"""
    html = get_html(*args, **kwargs)
    return get_data_from_html(html)

