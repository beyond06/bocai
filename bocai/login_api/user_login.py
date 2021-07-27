import requests

## 登录获取cookie值
def login(username,password):
    url='http://dev.bocaimedia.1daas.com/admin/login.ajax.php'
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
    #参数
    payload={
        'username': username,
        'password': password
    }
    resp=requests.post(url,data=payload,headers=headers)
    return resp.cookies['PHPSESSID']

## 登录获取cookie对象
def login1(username,password):
    url='http://dev.bocaimedia.1daas.com/admin/login.ajax.php'
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
    #参数
    payload={
        'username': username,
        'password': password
    }
    resp=requests.post(url,data=payload,headers=headers)
    return resp.cookies