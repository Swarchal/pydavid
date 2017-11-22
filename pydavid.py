"""
module docstring

http://david.abcc.ncifcrf.gov/api.jsp?type=xxxxx&ids=XXXXX,XXXXX,XXXXXX,&tool=xxxx&annot=xxxxx,xxxxxx,xxxxx,
"""

import valid_values
import pandas as pd
from selenium import webdriver


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
    # if passed a list, convert to a string separated by commas
    if isinstance(ids, list):
        ids = ",".join(ids)
    if isinstance(annot, list):
        annot = ",".join(annot)
    url_prefix = "http://david.abcc.ncifcrf.gov/api.jsp?"
    url = "{prefix}type={id_type}&ids={ids},&tool={tool}&annot={annot}".format(
            prefix = url_prefix, id_type = id_type, ids=ids, tool=tool,
            annot=annot)
    # FIXME returning a pretty sparse html page
    print("Fetching url: \n {}".format(url))
    driver = webdriver.PhantomJS()
    driver.get(url)
    # FIXME need to get chartReport.jsp from this page
    return driver


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



# DEBUGGING
# TODO: remove this once done
if __name__ == "__main__":

    id_type = "ENTREZ_GENE_ID"
    ids = ["2919", "6347", "6348", "6364"]
    tool = "chartReport"
    annot = ["GOTERM_BP_FAT", "GOTERM_MF_FAT", "INTERPRO"]

    result = get_html(
        id_type=id_type,
        ids=ids,
        tool=tool,
        annot=annot)

