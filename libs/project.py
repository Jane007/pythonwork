# @Project : pythonwork
# @File    : project.py
# @Author  : zhangjing
# @Time    : 2022/8/24 13:34
# @Software : Pycharm
# @Description :
import json

import pytest
import requests


class Project:
    def __init__(self,inToken,url):
        self.heard = {"Authorization" : inToken}
        self.url = url


    def project_list(self,inData):
        payload = inData
        result = requests.get(self.url,params=payload,headers=self.heard)
        return result.json()

    def project_update(self,url,inData):
        payLoad = inData
        print(type(payLoad))
        print(payLoad)
        requests.put(url,json=payLoad,headers=self.heard)



if __name__ == '__main__':
    url = 'http://192.168.1.212:8987/element/project/350'
    inData = {'name': '蜂喔新标签（勿删，唐祺峰11111）', 'description': '蜂喔新标签', 'title': '蜂喔新标签', 'clientType': '1'}
    inData = json.dumps(str(inData))
    token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MTMzNWI2MzI5MjQ0ZTcyYjE0MDJkMzk5ZGVmMjNmMiIsImlhdCI6MTY2MTMxMDM5Miwic3ViIjoie1widXNlcklkXCI6XCI2YzE3Mjc2Ni1iMzM4LTExZTgtYjUzNy0wMDUwNTZjMDAwMDhcIixcIm5pY2tuYW1lXCI6bnVsbCxcImV4cGlyZWRBdFwiOjE2NjEzOTY3OTIzOTUsXCJwZXJtaXNzaW9uc1wiOltcIjAwXCIsXCIxMFwiLFwiMDAwMFwiLFwiMDAwMVwiLFwiMDAwMlwiLFwiMDAwMDAxXCIsXCIwMDAwMDJcIixcIjAwMDAwNFwiLFwiMDAwMDA1XCIsXCIwMDAxMDFcIixcIjAwMDEwMTAxXCIsXCIwMDAxMDEwMlwiLFwiMDAwMTAxMDNcIixcIjAwMDEwMTA0XCIsXCIwMDAxMDEwNVwiLFwiMDAwMTAxMDZcIixcIjAwMDIwMVwiLFwiMDAwMjAxMDFcIixcIjAwMDIwMTAyXCIsXCIwMDAyMDEwM1wiLFwiMDAwMjAxMDRcIixcIjAwMDIwMTA1XCIsXCIwMDAyMDEwNlwiLFwiMTAwMFwiLFwiMTAwMVwiLFwiMTAwMDAxXCIsXCIxMDAwMDJcIixcIjEwMDA5OVwiLFwiMTAwMDAxMDBcIixcIjEwMDAwMTAyXCIsXCIxMDAwMDEwM1wiLFwiMTAwMDAyMDBcIixcIjEwMDAwMjAxXCIsXCIxMDAwMDIwM1wiLFwiMTAwMDk5MDFcIixcIjEwMDA5OTAyXCIsXCIxMDAxMDFcIixcIjEwMDEwMlwiXSxcInRlYW1JZHNcIjpcIlwiLFwidGVhbVR5cGVzXCI6XCJcIixcIndvcmtDaXR5XCI6NjEwMSxcInJvbGVcIjpcIkFETUlOXCIsXCJzZXJ2aWNlQ2l0eVwiOlszMjAxLDM3MTMsMzIwMiwzMjAzLDMyMDQsNDIyOCwzMjA1LDQxMDEsMzIwNiw0MTAzLDUwMDEsNDExMiwzNjAxLDQxMTMsMzYwNCwxMzAxLDQ1MDEsNDUwMiwzNjA3LDQ1MDMsMjIwMSwyMjAyLDMxMDEsMzUwMSwzNTAyLDM1MDMsMTIwMSwzNTA1LDQ0MDEsNDQwMyw0NDA0LDIxMDEsNTMwMSwyMTAyLDQ0MDYsMjEwMyw0NDA5LDYyMDEsNDQxMyw0NDE5LDQ0MjAsMzQwMSwzNDAyLDExMDEsNDMwMSw0MzAyLDM0MDgsNTIwMSw1MjAzLDYxMDEsNjEwMyw2MTA0LDMzMDEsMzMwMiwzMzAzLDQyMDEsNDIwMyw0MjA1LDUxMDEsNDIwNiw1MTA3LDM3MDEsMzcwMiwxNDAxLDQ2MDEsMzcwNiw0NjAyLDM3MDcsMjMwMSwzNzEwXX0iLCJleHAiOjE2NjEzOTY3OTJ9.SqPttW_now9GhOEuqf8q6ePqdS_2MeEYxNZaEJL5l1I'
    Project(token,'aaa').project_update(url,inData)

