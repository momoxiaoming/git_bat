import requests

if __name__ == '__main__':
    ip="http://ipinfo.io/"
    res=requests.get(ip)
    print(res.text)
