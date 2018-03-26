import urllib2, csv
#import stands for Python module that lets users download web pages. This function will import csv files which is easily imported into other programs like Excel, Google Sheets etc. 
from bs4 import BeautifulSoup
#BeautifulSoup is a Python library for pulling data out of HTML and XML files. The following command stands for importing BeautifulSoup from bs4.
outfile = open('jaildata.csv', 'w')
# Output the header row 
writer = csv.writer(outfile)
#defines a writer string. Return a writer object responsible for converting the user's data into delimited strings on the given file-like object.
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#declares a varaibale for the url
html = urllib2.urlopen(url).read()
#urllib2 module provides an updated API for using internet resources identifies by URLs.The module will open a url indicated in a string above.           
soup = BeautifulSoup(html, "html.parser")
#parse the html using beautiful soup and store in varaible "soup"
tbody = soup.find('tbody', {'class': 'stripe'})
#This module will extract data with find() from the tbody              
rows = tbody.find_all('tr')
#We set variable in rows to find in the tablein the body of the webpage(?)
for row in rows:
#Now this will iterate over rows. Creates the "for" loop
    cells = row.find_all('td')
#for cells find row in table data cell
    data = []
#data() method allows us to attach data of any type to DOM elements in a way that is safe from circular references and therefore from memory leaks.
    for cell in cells:
        #for loop
        data.append(cell.text)
#updates the list by adding cell.text
    writer.writerow(data)
    #the writerow() method contains a key not found in fieldnames, the optional extrasaction parameter indicates what action to take.