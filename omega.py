
import time
import cloudscraper
from bs4 import BeautifulSoup 
print("Everything Looks Good! Lets Continue.")

url = "https://mdisk.pro/pgGIlBt"  #@param {type:"string"}


# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def mdisk(url):
    
    client = cloudscraper.create_scraper(allow_brotli=False)
    
    
    DOMAIN = "https://mdisk.pro"

    ref = "https://m.meclipstudy.in/"
    
    h = {"referer": ref}
  
    resp = client.get(url,headers=h)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    
    inputs = soup.find_all("input")
   
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(8)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
    
# ---------------------------------------------------------------------------------------------------------------------
print(mdisk(url))
