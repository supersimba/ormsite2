#coding:utf-8
#https://oapi.dingtalk.com/robot/send?access_token=6353e664b63710e3dfe88128d118aa89cb6114a546b8936baca6f6646ed3dba1
import json,urllib2

url = 'https://oapi.dingtalk.com/robot/send?access_token=6353e664b63710e3dfe88128d118aa89cb6114a546b8936baca6f6646ed3dba1'
header = {
    "Content-Type": "application/json",
    "charset": "utf-8"
    }
data = {
     "msgtype": "text",
        "text": {
            "content": "[Warnning]法人清算adg lns服务停止，测试告警"
        },
     "at": {
        "atMobiles": [
            "13883123877",
            "15213028181",
            "13391238727"
        ],
            "isAtAll":False   # at为非必须
         },
    }
sendData = json.dumps(data)
request = urllib2.Request(url,data = sendData,headers = header)
urlopen = urllib2.urlopen(request)
print urlopen.read()