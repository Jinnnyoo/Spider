import requests
from urllib.parse import urlencode

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'


# Ajax加载
def get_page(page):
    params = {
        "countryId": "",
        "cityId": "",
        "bgIds": "",
        "productId": "",
        "categoryId": "",
        "parentCategoryId": "",
        "attrId": "",
        "keyword": "",
        "pageIndex": page,
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn"
    }
    # 拼接URL
    fullurl = url + urlencode(params)
    try:
        # 请求
        response = requests.get(fullurl)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("NO", e.args)

def parse_page(json):
    data = json.get("Data")
    # print(data)
    if data:
        # 根据Data中的数据获取Posts数据
        res = data.get('Posts')
        # print(res)
        for item in res:
            tencent = {}
            # 职位名称
            tencent['职位名称'] = item['RecruitPostName']
            # 工作地点
            tencent['工作地点'] = item['LocationName']
            #工作类型
            tencent['工作类型']=item['CategoryName']
            # 职位描述
            tencent['职位描述'] = item['Responsibility']

            yield  tencent

if __name__ == '__main__':
    # json = get_page(1)
    # result = parse_page(json)
    max_page=10
    for page in range(1,max_page+1):
        json = get_page(page)
        result = parse_page(json)
        for res in result:
            data=str(res)
            with open('tx.txt','a',encoding='utf8') as f:
                f.write(data+"\n")

