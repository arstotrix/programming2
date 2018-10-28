import urllib.request

def getfiles(url):
    req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        text = response.read().decode('utf-8')
    return text
        
def main():
    url = "http://korolev.news" 
    code = getfiles(url)
    #print(code[:100])

if __name__ == '__main__':
    main()
