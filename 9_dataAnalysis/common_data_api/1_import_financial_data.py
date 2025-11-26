import math
import requests
import pandas as pd

# 환경 변수 관련 모듈 ----
from dotenv import load_dotenv
import os
# ------------------------
load_dotenv()     # .env 파일 불러오기

# * 공공데이터 포털 사이트에서 발급받은 서비스 키(인증키)
SERVICE_KEY=os.environ.get('SERVICE_KEY')

# * BASE URL
BASE_SERVICE_URL='https://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2'

# * 재무상태표 조회 API
API_PATH='getBs_V2'

REQUEST_URL = f'{BASE_SERVICE_URL}/{API_PATH}'
# print(REQUEST_URL)    # URL 링크 접속 => Unauthorized 확인

'''
# * API 연동 테스트 ===============================================================
params = {
  "numOfRows" : "10",
  "pageNo" : "1",
  "resultType" : "json",
  "serviceKey" : SERVICE_KEY,
  "crno" : "1301110006246"      # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회
}
response = requests.get(REQUEST_URL, params=params)
data = response.json()
# print(data)

# 응답 데이터 추출
items = data.get('response',{}).get('body',{}).get('items',{}).get('item',[])
# response 안에 body 안에 items 안에 item [](리스트) 데이터 추출

# ---- 반복문 이용하여 출력
for x in items:
  print(x,'\n')
# * ===============================================================================
'''

# * API 요청 후 수집된 데이터를 CSV 파일로 저장 ===================================
def get_first_data():
  '''
    재무 상태표 API의 첫번째 페이지의 데이터(item)와
                      전체 건수(totalCount)를 반환해주는 함수
  '''
  params = {
    "numOfRows" : "10",
    "pageNo" : "1",
    "resultType" : "json",
    "serviceKey" : SERVICE_KEY,
    "crno" : "1301110006246"
  }
  response = requests.get(REQUEST_URL, params=params)
  data = response.json()
  items = \
    data.get('response',{}).get('body',{}).get('items',{}).get('item', [])  # 조회한 데이터 목록
  totalCount = data.get('response',{}).get('body',{}).get('totalCount', 0)        # 전체 건수

  # print('\n',items[0],'\n')
  # print(f'totalCount : {totalCount}')

  if data:
    return items, totalCount
  else:
    return [], 0
'''
data_list, totalCount = get_first_data()
print(len(data_list), totalCount)

filename = 'financial_ss.csv'

if totalCount > 0:
  # CSV 파일로 저장 : financial_ss.csv
  df = pd.DataFrame(data_list)
  df.to_csv(filename, encoding='utf-8')
  print('* --- 파일 저장 완료 --- *')
'''  
  
# numOfRows : 10, totalCount : 172 --> math.ceil(totalCount / numOfRows) 올림처리 -> 전체 페이지 수 : 18
# numOfRows : 100, totalCount : 172 --> 전체 페이지 수 : 2

# 전체 데이터를 수집하여 csv 파일로 저장 -> financial_ss.csv
'''
def get_params():
  page_no = 1
  num_of_rows = 10
  zx = []
  while(True):
    params = {
      "numOfRows" : str(num_of_rows),
      "pageNo" : str(page_no),
      "resultType" : "json",
      "serviceKey" : SERVICE_KEY,
      "crno" : "1301110006246"
    }
    response = requests.get(REQUEST_URL, params=params)
    data = response.json()
    items = data.get('response',{}).get('body',{}).get('items',{}).get('item',[])
    totalCount = data.get('response',{}).get('body',{}).get('totalCount', 0)

    if math.ceil(totalCount / num_of_rows) == page_no-1:
      break
    # print(items[:],'\n')
    page_no += 1
    zx += items
    # print(f'반복 ------------------ {page_no}')
  # print(zx)
  filename = 'financial_ss.csv'
  df = pd.DataFrame(zx)
  df.to_csv(filename, encoding='utf-8')
  print('* --- 파일 저장 완료 --- *')
# get_params()
'''
def get_params():
  num_of_rows = 100  # 성능 위해 크게 (100~1000 권장)
  page_no = 1
  all_items = []

  # ----------------------
  # 1) 첫 페이지 요청 → 전체 페이지 수 계산
  # ----------------------
  params = {
      "numOfRows": str(num_of_rows),
      "pageNo": str(page_no),
      "resultType": "json",
      "serviceKey": SERVICE_KEY,
      "crno": "1301110006246"
  }

  response = requests.get(REQUEST_URL, params=params)
  data = response.json()

  body = data['response']['body']
  totalCount = body['totalCount']
  total_pages = math.ceil(totalCount / num_of_rows)

  print(f"총 데이터: {totalCount}, 총 페이지: {total_pages}")

  # 첫 페이지 데이터 저장
  all_items.extend(body.get('items', {}).get('item', []))

  # ----------------------
  # 2) 남은 페이지 빠르게 수집
  # ----------------------
  for page in range(2, total_pages + 1):
      params["pageNo"] = str(page)

      response = requests.get(REQUEST_URL, params=params)
      data = response.json()

      items = data['response']['body'].get('items', {}).get('item', [])
      all_items.extend(items)

      print(f"{page}/{total_pages} 페이지 수집 완료")

  # ----------------------
  # 3) CSV 저장
  # ----------------------
  df = pd.DataFrame(all_items)
  df.to_csv("financial_ss_1.csv", encoding="utf-8", index=False)

  print("\n* --- 파일 저장 완료 --- *")
get_params()