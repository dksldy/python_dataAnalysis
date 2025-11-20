import numpy as np

def practice():
  arr = np.arange(1,10).reshape(3,-1)
  # print(arr)
  # print(arr[:,1:])
  # [면(시작 : 끝 : 증가값), 행, 열]
  # arr = np.arange(27).reshape(3, 3, 3)
  # arr = np.arange(1, 20)
  # arr = np.array([[8, 33, 15, 9], [25, 34, 7, 12]])
  # arr = np.arange(10, 110, 10).reshape(2, 5)
  # arr = np.array([[[13, 6],[8, 12]],[[77, 5],[41, 99]]])
  arr = np.arange(2, 38, 2).reshape(2, 3 ,3)
  print(f'원본 : \n{arr}')
  # 1 2 / 10 11
  print(f'테스트 : \n{arr[1:,:,::2]}')
practice()