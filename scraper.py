import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


sites = [
["Mathematisch Naturwissenschaftliche Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=3300"],
["Lebenswissenschaftliche Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=21"],
["Juristische Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=1000"],
["Philosophische Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=51"],
["Wirtschaftswissenschaftliche Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=70"],
["Theologische Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=6000"],
["Sprach- und literaturwissenschaftliche Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=5200"],
["Studierendenvertretung ","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=0400"],
["Kultur-, Sozial, und Bildungswissenschaftliche Fakultät","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=5500"],
["Zentralinstitut Großbritannien","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=82"],
["Zentralinstitut Professional School of Education","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8300"],
["Zentralinstitut Hermann von Helmholtz- Zentrum für Kulturtechnik","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8400"],
["Integrative Forschungsinstitute","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8500"],
["Cluster im Rahmen der Exzellenzinitiative","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8600"],
["Humboldt Graduate School","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8700"],
["Interdisziplinäre Zentren","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=8800"],
["Zentraleinrichtung Universitätsbibliothek","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=92"],
["Zentraleinrichtung Computer & Medienenservice","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=93"],
["Weitere Zentralinstitute","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=93"],
["Charite","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=40"],
["Präsidium ","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=0100"],
["Universitätsverwaltung","https://www.hu-berlin.de/de/service/zisneu/zis?ifabsessid=dunjft1h4jj5glk3l2cen8ruij&ifab_modus=einrichtungergebnis&ifab_okz=02"]]

# list that contains all data from all faculties
globalPersonList = list()

for site in sites:
    # list that contains the data from one faculty/site
    personList = list()
    institution = site[0]
    siteUrl = site[1]
    url = siteUrl + "&ifab_seite=0"

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    # Get amount of pages of search request
    try:
        pageCount =  int(soup.table.td('a')[-1].text)
    
    # default to 1 if none is found
    except:
        pageCount = 1
    
    print(site[0], " - ", pageCount)
    
    # sleep to prevent being blocked
    time.sleep(1) 

    # loop trough the amount of pages in search request
    for page in range(pageCount):
        print(page)

        # request individual page of search request
        url = siteUrl + "&ifab_seite=" + str(page)
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # loop through the search results on one page (100 is default max since probably no more than 50 are shown per page)
        for x in range(0,100,2):
            try:
                name = soup.find_all('table',width="100%", cellspacing="0", cellpadding="0", border="0", style="border: 0px none transparent !important;")[x].find_all('td')[0].b.a.text.strip()
            except:
                # if the name cant be extracted skip the person
                continue

            try: 
                mail = soup.find_all('table',width="100%", cellspacing="0", cellpadding="0", border="0", style="border: 0px none transparent !important;")[x].find_all('td')[1].a.text.strip()
            except:
                mail = ""

            try:
                phone = soup.find_all('table',width="100%", cellspacing="0", cellpadding="0", border="0", style="border: 0px none transparent !important;")[x+1].find_all('td')[0].text.strip().split('Telefon: ')[1]
            except:
                phone = ""

            try:
                position = soup.find_all('table',width="100%", cellspacing="0", cellpadding="0", border="0", style="border: 0px none transparent !important;")[x+1].find_all('td')[1].text.strip()
            except:
                position = ""
             
            person = {
              "name": name,
              "mail": mail,
              "phone": phone,
              "position": position,
              "institution": institution
            }
            personList.append(person)
            globalPersonList.append(person)

    filenameXls = 'xls/' + site[0].strip() + '.xlsx'

    # Write results to xls for this faculty
    dfPersonList = pd.DataFrame(personList)
    dfPersonList.columns = ['Name', 'E-Mail', 'Telefonnummer', 'Position', 'Einrichtung']
    dfPersonList.to_excel(filenameXls, index=False)  

# Write results of all faculties to xls
dfGlobalList = pd.DataFrame(globalPersonList)
dfGlobalList.columns = ['Name', 'E-Mail', 'Telefonnummer', 'Position', 'Einrichtung']
dfGlobalList.to_excel('xls/global.xlsx', index=False)  
   
print("finished")
