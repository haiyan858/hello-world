import requests
url = 'https://admin-wemall-test.ssl.cdao007.com/api/permission/login'
data = {
    'username': 'zlytest1',
    'rememberMe':'true',
    'password':'123456a' ,
}
header = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
r= requests.post(url, data=data, headers=header)
print(r.status_code)

