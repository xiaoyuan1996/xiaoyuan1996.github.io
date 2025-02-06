import requests

url = 'https://yuanzhiqiang.site/dev/arxiv/make_post_and_comments'
params = {
    'openid': 'oAve25WvLXyOZZUs42j69XJmEPTo',
    'contents': '88888',
    'post_link': '',
    'area': 'Quantitative Finance-Economics'
}
headers = {
    'accept': 'application/json'
}

response = requests.post(url, params=params, headers=headers)

print(response.status_code)
print(response.json())