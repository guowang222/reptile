js = ''
with open('js_56.js','r') as f:
    js = f.read()

import requests
import execjs
# publickey_mod = 'ce71150e4ce0d00dcd0544b3c20db8f4902281d519d44a196f77a4e1bfa071403b89f11506be89b93760d31e3682d295f59da73d5ae661481fc90cc6655cd4ecdeded5be962ced2747c6459941f2e1fb25c4123dca3497120c68b9d47297b245c4b75efb9284030568cecfc42fa027e332b245503494c194bc53336364d6f2500bcf597d971cd1185493078ffa6e13479e5b609f51a91455e60ba34a013b9e0f29e64930cca053f642e8e2de862a3c1d19e73cfaac137016e9ef10a8f3d3cb27396232a49d754892ebd6e02bb3d65f5edcda2ff33731dde95d8b291b03734673db82465fa61c9d2011db53415262f82cd5e136f14732395b089223212a5eb209'
# publickey_exp = '010001'


url = 'https://store.steampowered.com/login/getrsakey/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
resp = requests.post(url,headers=headers,data = {'username':'123'})
publickey_mod = resp.json().get('publickey_mod')
publickey_exp = resp.json().get('publickey_exp')

ctx = execjs.compile(js)
# pb_key = ctx.call('RSA.getPublicKey',publickey_mod,publickey_exp)
# pwd = ctx.call('RSA.encrypt','123456',pb_key)
pwd = ctx.call('get_pwd','123',publickey_mod,publickey_exp)
print(pwd)
