import requests
import urllib.request
from datetime import datetime
import threading
import time

# Burp Suite로 따오세요;

url = "http://school.gyo6.net/slecture/student/insert?menuId=0"

headers = {
    "Host": "school.gyo6.net",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
    "Referer": "http://school.gyo6.net/slecture/student/finsert?lectSeq=6264&menuId=83053&loginYN=N",
    "Cookie": "WMONID=-blTppkp7f8; JSESSIONID=KNfTuCDLesMU6vTWf0mnti6LC8zlbC0tQoZNDY5wBVIuam4OxfwLlCUQPGoHlcw2.school-was3_servlet_NewSchool3; _ga=GA1.2.175779495.1691826944; _gid=GA1.2.609019705.1691826944; _gat=1; _ga_WEW14EYCBB=GS1.2.1691826944.1.1.1691827018.0.0.0",
    "Connection": "close"
}

data = {
    "lectSeq": "0",
    "authYn": "N",
    "menuId": "0",
    "loginYN": "N",
    "stuName": "%AA%AA%AA%AA%AA%AA%AA%AA%AA",  # URL-encoded value
    "stuGrade": "0",
    "stuClass": "0",
    "stuNum": "0",
    "stuTell": "01012345678"
}

def SendRequest():
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    print(response.text)

    return response.status_code

def GetServerTime(unit):
    server = 'https://school.gyo6.net'
    time = urllib.request.urlopen(server).headers['Date'][5:-4]
    print(time, end="\r")

    if unit == "hour":
        return time[12:14]
    elif unit == "minute":
        return time[15:17]
    elif unit == "second":
        return time[18:20]
    
    return time

def TryApply():
    while True:
        if SendRequest() != "200":
            break

def AutoMate():
    while True:
        if int(GetServerTime("minute")) == 58:
            print("[*] 곧 프로세스가 시작됩니다.")

            while True:
                if int(GetServerTime("second")) >= 58:
                    break

            TryAtt = True
            for x in range(300): # 쓰레드 개수
                aaa = threading.Thread(target=TryApply)
                aaa.start()
            break
        else:
            print ("\033[A                             \033[A")
            print("[*] (ㅈ)대기중")
    return

while True:
    print("[i] Available Options: \n [1] Start Automating \n [2] Configure \n [3] Send Request Manually \n [4] Get Server Time \n [5] Quit")
    opti=input('Select Option:')

    if opti == "1":
        AutoMate()
    elif opti == "2":
        continue
    elif opti == "3":
        SendRequest()
    elif opti == "4":
        GetServerTime()
    elif opti == "5":
        quit()

    input("[<] 엔터를 눌러 계속")