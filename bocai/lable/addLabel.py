import requests

from login_api.user_login import login
from login_api.user_login import login1
## 地址
def addLabel(name,indexid):
    url='http://dev.bocaimedia.1daas.com/admin/modue/label/ajax.php'
    #头  headers
    heard={'Content-Type': 'application/x-www-form-urlencoded'}
    payload={
        'ac':'edit',
        'id':'',
        'name':name,
        'indexid':indexid
    }
    resp=requests.post(url,data=payload,cookies=login1('yiwang','123456'),headers=heard)
    resp.encoding='unicode_escape'
    print(resp.text)

if __name__ == '__main__':
    addLabel('练习02',1)

