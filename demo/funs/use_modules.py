import sys

# sys.path.insert(0, r'c:\classroom\june16\demo\mylibs')
print(sys.path)

# import number_funs as nf
# from mylibs import *
from mylibs import number_funs

print(number_funs.iseven(10))
