import requests
import json

from bs4 import BeautifulSoup as bs


def p_format(*args):
    ip_address, port, code, country, anonymity, google, https, last_checked = args
    
    return {
        "ip_address": ip_address,
        "port": port,
        "code": code,
        "country": country,
        "anonymity": anonymity,
        "google": google,
        "https": https,
        "last_checked": last_checked
    }


def Proxy_List():

    url = "https://free-proxy-list.net/"
    NUMBER_OF_ATTRIBUTES = 8
    try:
        
        page = requests.get(url)

    except:
        
        print("\nFailed to get Proxy List :(\nTry Running the script again..")
        return None

    if page.status_code != 200:
        print("\nSomething Went Wrong while Getting Proxy List!\n")
        return None

    soup = bs(page.text, 'html.parser')  

    table = soup.find('table')
    tbody = table.tbody if table else None  

    if tbody:
        infos = tbody.find_all('tr')
        for info in infos:
            
            proxy_data_temp = [i.text for i in info]
            if len(proxy_data_temp) == NUMBER_OF_ATTRIBUTES:

                proxies.append(p_format(*proxy_data_temp))

        return {"list_of_proxies": proxies,
                "count": len(proxies)}

def cacher():
    result = Proxy_List()
    try:
        for i in range(5):
            poxy_exp = result['list_of_proxies'][i]
            proxy = 'https://'+ poxy_exp['ip_address'] + ':' + poxy_exp['port']
            proxyDict = {
                'https' : proxy
            }

            print('Tying this proxy :', proxy)
            try:
                result_list = requests.get('https://api.github.com/search/users?q=location:india', proxies = proxyDict)
                data = result_list.json()

                print('Working on it ...')

                for i in range(len(data)):
                	for u in data['items']: 
                		repos = requests.get(u['repos_url'])
                		value = repos.json()
                if 'message' in value:
                    print('Exceded !')

                with open('profile.json', 'w') as file:
                    data = file.write(str(json.dumps(value)))
                    print('Data saved !')

                return
            except Exception as e:
                print(f'Something went wrong " {e} " check it ')
                continue
    except Exception as e:
        print('Check Exception Please : ', e)
cacher()