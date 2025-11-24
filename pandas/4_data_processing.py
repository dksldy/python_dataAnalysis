import pandas as pd
import numpy as np

# * products.csv 파일 데이터 읽어오기
print('products.csv 파일 데이터 읽어오기')
products = pd.read_csv('products.csv', index_col='id')
# index_col='xx'

print(f'read_csv products :\n{products}')
print('\n* ----- index 변경하기 ----- *')

# 상위 5개 데이터 출력하기
print('\n* ----- 상위 5개 데이터 출력 ----- *')
print(pd.DataFrame.head(products))
print('\n* ----- 하위 5개 데이터 출력 ----- *')
print(pd.DataFrame.tail(products))

print('\n* ----- 상위 2개 하위 2개 데이터 출력 ----- *')
print(f'상위 2개 :\n{pd.DataFrame.head(products,n=2)}')
print(f'하위 2개 :\n{pd.DataFrame.tail(products,n=2)}')

print('==' * 30)
print(products[:5])

print(f'index : {products.index}')
print(f'columns : {products.columns}')

# * 행 / 열 선택(인덱싱) 및 범위 선택(슬라이싱) : loc, iloc
#       loc (Label Location) : 라벨 기반 선택
#           loc[행_선택, 열_선택]
#           - 행 선택 : 인덱스 라벨(문자열, 숫자, 지정한 이름, ...)
#           - 열 선택 : 컬럼 라벨(열 이름, 문자열, ...)
#           => 슬라이싱 시 끝 라벨을 포함

#       iloc (Integer Location) : 정수(위치) 기반 선택
#           iloc[행_선택, 열_선택]
#            - 행 선택 : 0 부터 시작하는 순서(위치)
#            - 열 선택 : 0 부터 시작하는 순서(위치)
#            => 위치 기반으로 기존 슬라이싱과 동일. 끝 위치(인덱스) 미포함(제외)
print('==' * 30)
print('==' * 30)

def practice_loc():
  print("\n* ==== 상품명만 조회(출력) ==== *")
  print(products['상품명'])   # 데이터 프레임에 [] 로 인덱싱 할 때는 컬럼을 기준으로 선택. 행 X

  print("\n* ==== 113번 행의 데이터 조회 ==== *")
  print(products.loc[113])

  print("\n* ==== 113번 행의 상품명 조회 ==== *")
  print(products.loc[113,'상품명'])

  print("\n* ==== 113번 행의 상품명, 가격 조회 ==== *")
  print(products.loc[113, ['상품명', '가격']])    # 여러 개의 열을 리스트 형태로 전달
  print(products.loc[113, '상품명':'가격'])       # 슬라이싱 적용

  print("\n* ==== 110번 행의 상품명, 재고 조회 ==== *")
  print(" === 리스트 방식 === ")
  print(products.loc[110, ['상품명', '재고']])    # 리스트
  print(" === 슬라이싱 방식 === ")
  print(products.loc[110, '상품명' : '재고' : 2])     # 슬라이싱

# practice_loc()

def practice_iloc():
  print("\n* ===== 첫번째 행의 전체 컬럼 조회 ==== *")
  print(products.iloc[0])
  # print(products.iloc[0, 0:4:2])

  print("\n* ===== 첫번째 행의 마지막 컬럼 조회 ==== *")
  print(f'결과 : {products.iloc[0,-1]}')  # => Scalar
  print(products.iloc[0,::3])             # => Series

  print("\n * ===== 3 ~ 5 번째 행의 모든 컬럼 조회 ===== *")
  print(products.iloc[2:5])   # => products.iloc[2:5, 0:4]

  print("\n * ===== 3 ~ 5 번째 행의 두번째 컬럼 조회 ===== *")
  print(products.iloc[2:5, 1:2])
# practice_iloc()

'''
    데이터 프레임(DataFrame)의 인덱스는 반드시 숫자가 아닐 수 있음.
    문자나 날짜 등 다양한 값이 라벨이 될수 있음
    따라서, 위치(index)로 선택하는 것 인지, 라벨(label)로 선택하는 것 인지
    모호해 질수 있음.

    이러한 혼란을 방지하고 의도를 명확하게 하기 위해
    판다스(Pandas)에서는 라벨 기반 선택은 loc 사용
                         위치 기반 선택은 iloc 사용
    으로 구분 하여 기능 제공.
'''

# ======================================================================

# * 새로운 컬럼 생성
#   df[추가할_컬럼명] = 저장할_데이터
def add_column_test():
  products_test = products.copy()

  products_test['TEST'] = '테스트 데이터'
  print(products_test.head(2))

  # 컬럼 삭제 => drop(columns=[삭제할 컬럼])
  products_test = products_test.drop(columns=['TEST'])
  print(products_test.head(1))
# add_column_test()

def add_total_price():
  print("* ==== 총 금액 컬럼 추가 ==== *")
  # 총 금액 = 가격 * 재고
  products['총 금액'] = products['가격'] * products['재고']
  print(products.head())

  print("\n* ==== 재고 수량에 따른 상태 컬럼 추가 ==== *")
  # 재고 상태 => 재고가 130 미만이면, '부족', 그렇지 않으면 '충분'
  # numpy.where(조건, 조건만족시_사용할 값, 만족하지_않을경우_사용할값)
  products['재고 상태'] = np.where(products['재고'] > 130, '충분', '부족')
  print(products.head())
  
  print("\n* ==== 재고 상태별 데이터 개수 조회 ==== *")
  print(products['재고 상태'].value_counts())
# add_total_price()

# ========================================================================

# * 문자열 처리
def str_processing():
  # * 상품명 정보 조회
  print(products['상품명'])

  # 괄호가 포함된 상품의 정보 분리

  # 1) 괄호를 기준으로 분리

  # df.str : 시리즈 내의 데이터가 문자열 이거나 문자열 리스트일 때,
  #          문자열 자체에 접근 가능한 방법 (특별한 통로)
  #          => 전체 데이터를 대상으로 문자열 처리 가능

  # str.split(구분자, n=분리횟수, expand=컬럼확장여부)
  #       * n : 구분자에 해당하는 부분이 여러개 일 때 몇번 분리할 것 인지
  #       * expand : False - 리스트 시리즈 형태로 반환 (하나만 빠르게 추출할 때)
  #                  True  - 데이터프레임 형태로 반환 
  #                 (하나의 컬럼을 여러개의 독립된 컬럼으로 나눌 때. 일반적인 방식)

  # 구분자, 분리횟수 설정하여 분리
  #   '('      1
  split_df = products['상품명'].str.split( '(' , n=1 )
  print(split_df)

  print(split_df.str[0])   # 첫번째 요소(메인 이름)만 추출
  print('* ---- *' * 30)

  # 구분자, 분리횟수, 컬럼확장 설정 분리
  split_df = products['상품명'].str.split('(', n=1, expand=True)
  # print(split_df)
  # print(split_df.columns)

  # print(split_df[0])    # 메인 이름
  # print(split_df[1])      # 용량 / 부가 정보 => 없는 데이터 None

  # '메인 이름' 컬럼을 추가, 구분한 첫번째 데이터를 저장 (양끝 공백 제거)
  # '용량' 컬럼을 추가, 구분한 두번째 데이터를 저장 ( ')' 를 제거 )
  print('')
  products['메인 이름'] = split_df[0].str.strip()
  products['용량'] = split_df[1].str.replace(')', '')

  print('\n* ===== 메인이름, 용량 컬럼 추가 ===== *')
  print(products.head())

  print('\n* ===== 용량 데이터만 조회 ===== *')
  print(products['용량'])

  # 결측치 확인 : isnull()
  #   -> 결측치 : 유효하지 않은 값 (수집x, ...)
  #      * NaN    : Not a Number. 수치형 데이터에서 주로 다룸
  #      * None   : Python 객체에서 "값이 없음" 을 명시
  #      * Nat    : Not a Time. 날짜 / 시간 데이터에서 사용

  # print(products['용량'].isnull())
  # 유효한 값을 확인 => isnull()의 결과를 부정
  #                     부정 연산자 : (~) 사용
  # print(~products['용량'].isnull())

  print(products[~products['용량'].isnull()])

  # * 유효한 값이 있는지 확인 하는 확인 : notna
  #   - 유효한 값(결측치 X) : True
  #   - 결측치 (NaN, Null)  : False
  print("* ===== notna() ===== *")
  print(products['용량'].notna())
  print(products[products['용량'].notna()])
  
str_processing()