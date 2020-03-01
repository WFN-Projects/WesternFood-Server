# this file scrapes transaction from given html file and then creates a list of transaction objects

import re
from bs4 import *
import os
from scraper.transactionClass import *

def scrapeFile(url):
    soup = BeautifulSoup(url, "html.parser")
    soup = soup.prettify()
    soup = BeautifulSoup(soup, "html.parser")
    text = soup.get_text()
    text = re.sub(' +', ' ', soup.get_text())
    text = os.linesep.join([s for s in text.splitlines() if s])
    text = re.sub(r'^$\n', '', text, flags=re.MULTILINE)

    # initialize the transaction list
    TransList = []

    # splits html string into a list of lines
    text = text.splitlines()

    print('\n\n\n\n\n')
    print(text)
    print('\n\n\n\n\n')


    # traverse through the text
    for x in range(0, len(text) - 1):
        # print('\n\n\n\n\n')
        # print(x)
        # print('\n\n\n\n\n')
        # current line
        line = text[x]

        # transactions are seperated by an A and end with another A
        if "A" in line:

            # create list for current entry
            entry = []
            for y in range(x + 1, len(text) - 1):

                # doesn't add to entry if it is the ending "A" mark
                if "A" in text[y]:
                    break

                # add to entry if it is not an empty line or end "A"
                elif "A" not in text[y] and text[y] != " ":

                    entry.append(text[y])

            # append the whole entry into transaction list
            TransList.append(entry)

    # cleaning the transaction list entries to format it nicely
    # print('\n\n\n\n\n')
    # print(TransList)
    # print('\n\n\n\n\n')
    TransListClean = [x for x in TransList if x != [] and " Date" in x]
    # TransListClean.remove(TransListClean[0])
    TransListClean.pop(0)
    TransListClean.pop(0)
    print('\n\n\n\n\n')
    print(TransListClean)
    print('\n\n\n\n\n')

    # list of final cleaned entries
    final = []

    # takes each entry and creates a Transaction object
    for element in TransListClean:
        # # you can uncomment this line to see the output
        # print(element)
        # trans = Transaction(element[1], element[2], element[3], element[7], element[8], element[8])
        trans = {
            'date': element[1],
            'price': element[2],
            'balance': element[3],
            'location': element[7]
        }
        final.append(trans)

    return final
