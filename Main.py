import requests

def newAdConfig():
    url = "https://sunny.careduka.com/business-api/win-biz-config/get?prj_id=40288&user_type=old"
    data = requests.get(url)
    json = data.json()

    spacesData = json["data"]["spaces"]
    print(spacesData)
    rit_aar = []
    for item in spacesData:
        rit_group = item["rit_group"]
        for item2 in rit_group:
            item3 = item2["rit"]
            print(item3)
            binding = item3["binding"]
            bottom = item3["bottom"]
            price = item3["price"]
            for b1 in binding:
                rit_id = b1["rit_id"]
                rit_aar.append(rit_id)
            for b2 in bottom:
                rit_id = b2["rit_id"]
                rit_aar.append(rit_id)
            for b2 in price:
                rit_id = b2["rit_id"]
                rit_aar.append(rit_id)

    print(rit_aar.__len__())

    print(rit_aar)

def oldAdConfig():
    url = "https://cfg.vigame.cn/getXmlByAdconfig?debug=1&c=json&pid=40288004&appid=40288&cha_id=viyy&buy_id=default&city=%E6%B7%B1%E5%9C%B3&"
    data = requests.get(url)
    json = data.json()


if __name__ == '__main__':
    111
