'''
    브로드 캐스팅

    - 크기가 다른 배열 간에 연산을 가능하게 하는 기술
    - 작은 배열이 자동으로 확장되어 큰 배열의 shape에 맞춰짐
'''
import numpy as np

def scalar_to_array():
  scalar = 5
  arr = np.array([[10, 20], [30, 40]])
  
  # 스칼라(0D) + 행렬(2D)
  result = scalar + arr
  print(f'matrix :\n {arr}')
  print(f'scalar + matrix :\n {result}')
  # => [10, 20], [30, 40] + [5, 5], [5, 5]
  # scalar 값이 matrix 구조로 확장되어 연산이 수행됨
# scalar_to_array()

def different_shapes():
  vector = np.array([10, 20, 30])           # shape : (3,)

  matrix = np.array([[1, 2, 3],[4, 5, 6]])  # shape : (2, 3)

  result = vector + matrix
  print(f'vector + matrix :\n {result}')
  ''' =>
      vector (3,) -> (2, 3)
      [
        [10, 20, 30],
        [10, 20, 30]
      ]
  '''

  # vector2 = np.array([100, 200])
  # result2 = matrix + vector2
  # print(f'matrix + vector2 : {result2}')  
  # => ValueError : coule not be broadcast

  # => 열 벡터로 변환하여 연산 수행
  '''
      [100, 200]

      [[100], [200]]

      [[100, 100, 100], [200, 200, 200]]
  '''
  vector2 = np.array([100, 200]).reshape(-1, 1)
  result2 = matrix + vector2
  print(f'matrix + vector2 :\n {result2}')  

different_shapes()
