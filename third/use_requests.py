import requests

requestHeaders = {
    'Content-Type': 'application/json'
}

requestBody = {'key1': 'value1', 'key2': 'value2'}

response = requests.get('https://www.baidu.com/', params={'a': 'a'},headers=requestHeaders,data=requestBody)


if response.status_code == 200:
    print('请求成功')
    print(response.text)
else:
    print(f'请求失败，状态码: {response.status_code}')


