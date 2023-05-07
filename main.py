import requests
from twocaptcha import TwoCaptcha # pip install 2captcha-python
solver = TwoCaptcha('ТОКЕН rucaptcha.com', server="rucaptcha.com")



email = ""
password = ""

cookies = requests.get('https://5sim.biz/v1/guest/csrf').cookies

json_data = {
    'email': email,
    'password': password,
    'captcha': solver.recaptcha(sitekey="6Lf5qwgTAAAAAKci_ZYBESf9Z_rQXtJbw7YSBBTt", url="https://5sim.biz/", version=1)['code']
}

response = requests.post('https://5sim.org/v1/guest/auth/login', headers={'x-xsrf-token': cookies["XSRF-TOKEN"]}, json=json_data, cookies=cookies)
print(response.text)
