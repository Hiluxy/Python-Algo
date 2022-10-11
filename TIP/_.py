
# def Size(a):
#     n=1
#     while a>n:
#         n*=2
#     return n

# print(Size(10))

# dic={1:[3,4]}
# print(dic[1][1])



# c='abc'
# c='#'*len(c)
# print(c)

# a='a.b.cd..'
# print(a.count('.'))

# a=[]
# a+=[(1,2,3),(4,5)]
# print(a)

# from typing import List
# from itertools import product
# alpha=[chr(i) for i in range(97,123)]
# print(alpha)
# dotlist=[]
# k=2
# for _ in range(1,k+1):
#     dotlist+=list(map("".join,(product(alpha,repeat=_))))

# print(dotlist)

# d=[ 'zu', 'zv', 'zw', 'zx', 'zy', 'zz']
# a='a.bc.'
# new=[]
# for i in range(len(d)):
#     new.append(a.replace('.',d[i] ))
# print(new)
#['azubczu', 'azvbczv', 'azwbczw', 'azxbczx', 'azybczy', 'azzbczz']



# #.부분만 대체
# c='.아.좀..'
# dot_num=c.count('.')
# dotlist=['a','b','c','d']
# new=[]
# f_idx=0
# n=0
# d_idx=0
# chat_list=c.split('.')
# print(chat_list)
#             #.의 개수 세기
#             dot_num=c.count('.')
#             #.부분만 대체
#             new=[]
#             for dot in dotlist:
#                 new.append(c.replace('.',dot))


U_dic={}
if 'A' in U_dic:
    U_dic['A']=1
print(U_dic)