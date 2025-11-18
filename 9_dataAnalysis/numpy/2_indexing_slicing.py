import numpy as np

def practice_1d():
  # 1차원 배열 생성 -> [10, 20, 30, 40, 50, 60]
  # arr = np.arange(10, 61, 10)
  arr = np.array([10, 20, 30, 40, 50, 60])

  print('---- 1D ----')
  print(arr)

  print('\n','* indexing *')
  print('세번째 요소 : ', arr[2])
  print('마지막 요소 : ', arr[-1])

  print('\n* slicing *')
  print('2번째 요소부터 4번째 요소까지 : ', arr[1:4:]) 
  # => 1, 2, 3 번 인덱스에 해당하는 요소 추출
  print('앞의 3개 요소 추출 : ', arr[:3])
  # => 0, 1, 2 번 인덱스에 해당하는 요소 추출. 시작 인덱스 생략
  print('짝수번째 요소 추출 : ', arr[1::2])
  # => 1, 3, 5 번 인덱스에 해당하는 요소 추출. 끝 인덱스 생략
  print('역순으로 추출 : ', arr[::-1]) # => [-1:-7:-1]
# practice_1d()

def practice_2d():
  # 3행 4열 형태로 1 ~ 12 까지 데이터를 담아 생성
  arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
  ])
  print(arr)
  
  # print('** arange 사용 **')
  # arr = np.arange(1, 13).reshape(3,4)
  # print(arr,'\n')

  print('\n** indexing **')
  print('배열에서 7을 출력 : ', arr[1,2]) # => ndarray 객체에서 접근 방법 
                                          # arr[1][2] => 기존 리스트에서 접근 방법
  print('\n** slicing **')
  print('배열에서 3, 4, 7, 8 출출 : \n', arr[ : 2, 2 : ])
  # 행 : 처음부터 1번 인덱스 까지 / 열 : 2번부터 끝 인덱스까지

  print('배열에서 1, 2, 3, 4를 추출 : \n', arr[ : 1, ]) # arr[0] => 기존 리스트 접근 방법
  print('배열에서 2, 6, 10을 추출 : \n', arr[ :, 1 : 2 ]) # arr[0:3:1, 1:2:1]
  # =>    print(arr[:, 1])
# practice_2d()

def practice_3d():
  # 1 ~ 12 데이터를 저장하는 3차원 배열 (2x3 배열이 2개)
  # arr = np.arange(1, 13).reshape(2,2,3)
  # print(arr,'\n')

  arr = np.array([[
    [1, 2, 3],
    [4, 5, 6]
  ],
  [
    [7, 8, 9],
    [10, 11, 12]
  ]])
  print(arr)

  print('\n ** indexing **')
  print('데이터 중 6을 출력 : ', arr[0, 1, 2])
  print('\n ** slicing **')
  print('7 ~ 12 값을 추출 : \n', arr[1:,:2])
  print('1, 2, 3, 7, 8, 9 값을 추출 : \n', arr[:2,:1]) # arr[:, 0]
# practice_3d()

def practice_boolean_indexing():
  # 1차원 배열 생성
  arr = np.array([10, 21, 30 , 43, 50, 8])
  print(arr)

  # 30 보다 큰 요소만 추출
  test = arr > 30       # 새로 정의
  print(test)
  print(arr > 30)       # [False False False  True  True False]
  print(arr[arr > 30])  # 조건에 해당하는 요소로만 다시 배열 생성

  # 2차원 배열 생성
  # 10 ~ 90 까지 총 9개의 데이터를 저장(3x3), 간격 :10
  arr = np.arange(10,91,10).reshape(3,3)
  print('\n', arr)
  # 50 < x < 80 데이터만 추출
  print('\n', arr[(arr > 50) & (arr < 80)])
  # => 각 조건은 소괄호로 묶어주고, AND 연산은 & 기호를 사용해야함

  result = (arr > 50) & (arr < 80)    # True / False 구분
  print('\n', result)
  print('\n',arr[result])             # True / False 값과 arr 인덱스 대조후 True 값 추출

  # 최대값 추출 : max()
  print(arr.max(), arr.min(), arr.sum(axis=0), arr.sum(axis=1), arr.mean())
  print(arr[arr == arr.max()])
practice_boolean_indexing()
