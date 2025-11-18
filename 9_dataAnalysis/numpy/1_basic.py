import numpy as np

# 0차원 배열 생성 -> 스칼라(Scalar). 축(Axis)이 없는 배열
def zero_dimension_arr():
  # 연산 일관성 유지, 브로드 캐스팅, 내부 처리 구조를 통일하기 위해 NumPy 에서는 스칼라도 배열로 취급

  arr = np.array(55)

  print(arr)
  print(type(arr))
  print(arr.ndim)   # 차원수
  print(arr.shape)  # 배열 형태

  # print(arr[0])   # 인덱싱 불가 IndexError 발생..
# zero_dimension_arr()

# 1차원 배열 생성 -> 백터(Vector). 축이 한개. 
def one_dimension_arr():
  arr =np.array([1,2,3,4,5])

  print(arr)
  print(type(arr))

  print(arr.ndim)   # 차원수
  print(arr.shape)  # 배열 형태

  # 0으로 채워진 배열 생성 : np.zeros(개수)
  # 0이 5개 들어있는 배열 생성
  zeros_arr = np.zeros(5)
  print(zeros_arr)
  print(zeros_arr.dtype)    # 요소의 데이터 타입

  # 1로 채워진 배열 생성 : np.ones(개수)
  # 1이 10개 채워져 있는 배열 생성
  ones_arr = np.ones(10)
  print(ones_arr)
  print(ones_arr.dtype)

  # 특정 범위 내의 숫자로 채워진 배열 생성 : np.arange(시작값, 끝값,증가값)
  # 0 ~ 9 까지 숫자가 담긴 배열을 생성
  arange_arr = np.arange(0,10,1)
  print(arange_arr)
  print(arange_arr.dtype)
# one_dimension_arr()

# 2차원 배열 생성 -> 행열(Matrix). 축 2개 (Axis 0: 행, 1: 열)
def two_dimension_arr():
  arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
  ])
  print(arr)
  print(type(arr))
  print(arr.ndim)
  print(arr.shape)

  # 0으로 채워진 배열 생성 => 3 x 4. np.zeros((행,열))
  zeros_arr = np.zeros((3,4))
  print(zeros_arr)
  print(zeros_arr.dtype)
  print(zeros_arr.ndim)
  print(zeros_arr.shape)

  # 1로 채워진 배열 생성 => 2x2. np.ones((행,열))
  one_arr = np.ones((2,2))
  print(one_arr)
  print(one_arr.dtype)
  print(one_arr.ndim)
  print(one_arr.shape)

  # 1 ~ 9로 채워진 배열 생성.
  # 1D -> 2D
  arange_arr = np.arange(1, 10).reshape(3,3)
  print(arange_arr)
  print(arange_arr.dtype)
  print(arange_arr.ndim)
  print(arange_arr.shape)
# two_dimension_arr()

# 3차원 배열 생성 -> 텐서 (Tensor). 축이 3개 (Axis 0: 깊이-면, 1: 행, 2: 열)
def three_dimension_arr():
  arr = np.array([
    [
      [1, 2, 3],
      [4, 5, 6]
    ],
    [
      [7, 8, 9],
      [10, 11, 12]
    ],
    [
      [13, 14, 15],
      [16, 17, 18]
    ]
  ])    # => ((3, 2, 3))
  print(arr)
  print(type(arr))
  print('차원수 : ', arr.ndim)
  print('배열 형태 : ', arr.shape)

  # 0으로 채워서 배열 생성 : np.zeros((면, 행, 열))
  zeros_arr = np.zeros((2,3,4))
  print(zeros_arr)

  # 1로 채워서 배열 생성 : np.ones((면, 행, 열))
  ones_arr = np.ones((1, 2, 3))
  print(ones_arr)

three_dimension_arr()