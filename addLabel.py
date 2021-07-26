import requests

## 地址
url='http://dev.bocaimedia.1daas.com/admin/modue/label/ajax.php'
#头  headers
heard={'Content-Type': 'application/x-www-form-urlencoded',
      'cookie':'PHPSESSID=v07cj7a2evrnbaabh3295ra3l0'}

payload={
    'ac':'edit',
    'id':'',
    'name':'练习02',
    'indexid':1
}

resp=requests.post(url,data=payload,headers=heard)
resp.encoding='unicode_escape'
print(resp.text)


