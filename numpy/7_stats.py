'''
    통계 함수

    - mean, std, sum : 기본 통계량 함수 (axis 활용)
    -   percentile   : 백분위수 (사분위수 확인)
    -     clip       : 값의 범위를 제한 (클리핑)
'''
import numpy as np

def basic():
  arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
  ])
  print(f'원본 배열 :\n{arr_2d}')

  # 합계 출력
  print(f'전체 합계 : {arr_2d.sum()}')
  
  # 평균 출력
  print(f'전체 평균 : {arr_2d.mean():.1f}')
  
  # 표준편차 출력
  print(f'표준편차 : {arr_2d.std()}')

  # 열 기준으로 합계 / 평균 (각 열의 합계, 평균)
  print(f'\n열 기준 합계 : {arr_2d.sum(axis=0)}')
  print(f'열 기준 평균 : {arr_2d.mean(axis=0)}')
  
  # 행 기준으로 합계 / 평균 (각 행의 합계, 평균)
  print(f'\n행 기준 합계 : {arr_2d.sum(axis=1)}')
  print(f'행 기준 평균 : {arr_2d.mean(axis=1)}')
  
  print(f'\n열 표준편차 : {arr_2d.std(axis=0)}')
  print(f'행 표준편차 : {arr_2d.std(axis=1)}')
# basic()

def pct_and_qt():
  '''
      Q 백분위수 (Q Percentile)
      : 전체 데이터를 100등분 했을 때 , q% 지점에 해당하는 값
        - q% : q번째 백분위수에 해당하는 값

      사분위수 (Quartiles)
      : 백분위수 중 25%, 50%(중앙값), 75% 지점을 나타내는 데이터
  '''

  # data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
  data = np.arange(5, 51, 5)
  print(data)

  # 70 백분위수 값 (전체 데이터의 70%가 이값 이하)
  # np.percentile(배열, q값)
  p70 = np.percentile(data, 70)
  print(f'70 백분위수 : {p70}')
  p50 = np.percentile(data, 50)
  print(f'50 백분위수 : {p50}')

  # np.percentile(배열, [25, 50, 75])
  q_tile = np.percentile(data, [25, 50, 75, 100])
  print(f'사분위수 (25, 50, 70) : {q_tile}')
  print(f'사분위수 (25) : {q_tile[0]} / '
        ,f'사분위수 (50) : {q_tile[1]}\n'
        ,f'사분위수 (75) : {q_tile[2]} / '
        ,f'사분위수 (100) : {q_tile[3]}')
# pct_and_qt()

def clipping():
  '''
      클리핑(Clipping) : 데이터 값이 특정 범위를 벗어날 경우
                         그 값을 경계값으로 강제로 제한하는 작업
  '''
  arr = np.array([5, 150, 20, -10, 80])

  # 데이터 범위를 0 ~ 100 사이로 제한
  # => 150, -10
  arr_clip = np.clip(arr, 0, 100)
  # => arr_clip = np.clip(arr, a_min=0, a_max=100)
  print(f' 원본 배열  : {arr}')
  print(f'클리핑 결과 : {arr_clip}')
clipping()
