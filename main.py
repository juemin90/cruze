import requests, sys

sys.path.append('..')
from libs.utils import getMysql

url = 'https://live.dszuqiu.com/ajax/score/data?mt=0&nr=1'

def getData():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            "cookie": 'ds_session=8i5ef0bgejl55a3h6pnr9rug87; uid=R-552638-f81a524a060222a002dbef; Hm_lvt_a68414d98536efc52eeb879f984d8923=1612686720,1612851714; Hm_lpvt_a68414d98536efc52eeb879f984d8923=1612859883',
        }
        body = requests.get(url, headers=headers)
        data = body.json()
        print(data)
        sys.exit(1)

    except Exception as e:
        print(e)


def insertData(data):
    db = getMysql()
    cursor = db.cursor()
    sql = 'select * from test'
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)



def start():
    # data = getData()
    data = []
    insertData(data)

start()