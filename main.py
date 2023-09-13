import requests
from bs4 import BeautifulSoup

def search_keyword_on_website(url, keyword):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to get URL. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.stripped_strings  
    
    for i, string in enumerate(texts):
        if keyword.lower() in string.lower():
            print(f"Keyword '{keyword}' found: {string}")

if __name__ == '__main__':
    url = "https://jobs.lever.co/MBRDNA/4d8a682e-c6ec-4523-9be4-21c0f73ac826/apply?utm_source=Simplify&ref=Simplify"  
    keyword = "Software Engineer"  
    search_keyword_on_website(url, keyword)
