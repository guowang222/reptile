import requests

url = 'https://www.21wecan.com/rcwjs/searchlist.jsp'
args={
    'searchword':'人才'
}
resp = requests.post(url,data=args)
print(resp.text)