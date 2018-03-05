import numpy as np
import pandas as pd
from numpy.random import shuffle

filename = './shingle.txt'
NaN = float('nan')
DEBUG = True
DEBUG = False

files_size = 500
N = 100
min_hash_sig_mat = []
'''
shingles = pd.read_csv(filepath_or_buffer=filename)
shingles.drop(files_size-1, axis=0, inplace=True)
print shingles.loc[0]
'''
shingles = None
_file_content = []
with open(filename) as file:
    for _line in file:
        _line = _line.split(':')[1]
        _values = _line.split(',')
        _file_content.append(_values)
        if DEBUG:
            files_size -= 1
            if files_size <= 0:
                break
    del _line, _values
    del _file_content[-1]
shingles = pd.DataFrame(_file_content, dtype=np.int8).T
pd.DataFrame([]).reindex()
# shingles = shingles.T
# print shingles.shape
# print shingles[:][shingles.index[0]]
# print shingles[0][shingles.index[17]]
# print shingles.get_value(17, 0)
# r=17
# j=0
# print shingles.iloc[r][shingles.columns[j]]
# shingles.loc['sss']

for i in range(N):
    if DEBUG:
        _shingles = shingles.sample(n=10, axis=0)   # [TEST]
    else:
        _shingles = shingles.reindex(np.random.permutation(shingles.getIndex))
    # _shingles = shingles.copy()
    # _shingles.drop(_shingles.index[len(_shingles) - 1])
    # _shingles = _shingles.T
    # shingles.drop(shingles.columns[[-1]], axis=1, inplace=True)
    print '--[1] done [%f%%]--' % ((i+1) * 0.95 / N),
    rows_size = _shingles.shape[0]
    cols_size = _shingles.shape[1]
    # print rows_size, 'x', cols_size
    # _shingles.apply(shuffle)
    min_hash_signature = np.array([NaN] * cols_size)
    print '--[2] done [%f%%]--' % ((i+1) * .97 / N),
    for j in range(cols_size):
        _signature = min_hash_signature[j]
        for r in range(rows_size):
            # print '[%d, %d]:' % (r, j),
            # print type(r), type(j)
            # print _shingles.iloc[r][_shingles.columns[j]], '\t',
            # if (_signature != _signature) and (_shingles[j][_shingles.index[r]] == 1):
            # if _shingles.loc[j][_shingles.index[r]] == 1:
            if _shingles.iloc[r][_shingles.columns[j]] == 1:
                min_hash_signature[j] = j
                break
        del _signature
    del _shingles
    print '--[3] done [%f%%]--' % ((i+1) * 1. / N)
    min_hash_sig_mat.append(min_hash_signature)
min_hash_sig_mat = np.array(min_hash_sig_mat)
for j in range(shingles.shape[1]):
    for k in range(j+1, shingles.shape[1]):
        # print min_hash_sig_mat.shape[1]
        p = 1. * sum(np.equal(min_hash_sig_mat[:, j], min_hash_sig_mat[:, k])) / N
        # if p > 0:
        print "Compare(%d, %d)=%f%%" % (j, k, p)
# print shingles
'''
N = 100
for i in range(N):
    min_hash_signature = [] * shingles.shape[1]
    shingles = pd.read_csv(filepath_or_buffer=filename)
    shingles.apply(shuffle)
    print shingles
'''