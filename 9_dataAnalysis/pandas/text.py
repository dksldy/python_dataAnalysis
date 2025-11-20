import pandas as pd

s = pd.Series([100, 200, 300], index=['kk','mm','yy'])
print(f'   s    :\n{s}')
print(f'values  : {s.values}')
print(f'index   : {s.index}')
print(f'dtype   : {s.dtype}')

print('* ======== *')
data = {
  'name' : ['a', 'b', 'c'],
  'age'  : [1, 2, 3],
  'score': [10, 20, 30]
}
index = ['user1', 'user2', 'user3']
df = pd.DataFrame(data, index=index)

print(f'data    : {data}')
print(f'index   : {df.index}')
print(f'columns : {df.columns}')
print(f'values  :\n {df.values}')
print(f'dtypes  : {df.dtypes}')