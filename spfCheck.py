
import requests
from bs4 import BeautifulSoup

def checkspf(domainname):
    
    #Attaches the specified domain to the site URL where it is checked
    domainToCheck = "https://www.spf-record.com/spf-lookup/" + domainname
    
    #Use the requets library to make an HTTP request and store it in the 'r' response object.
    r = requests.get(domainToCheck)

    #Use BS to parse the HTML
    soup = BeautifulSoup(r.text,"html.parser")

    #Check the parsed HTML data for this CSS selector.
    spfCheck = soup.select('#spf_output')

    #Returns the needed SPF record
    return spfCheck[0].text

