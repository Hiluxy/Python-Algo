# m,n,h=map(int,input().split())
# g=[]
# for _ in range(h):
#     g.append([list(map(int,input().split())) for _ in range(n)])
# print(g)
# # 5 3 2
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 1 0 0
# # 0 0 0 0 0
# #[[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

# visited=[[[False]*m for _ in range(n)] for _ in range(h)]
# print(visited)

a=[[0,0,1],[0,0,2]]
b=[[[0,0,1],[0,0,2]],[[0,0,3],[0,0,4]]]
print(map(max,a)) #<map object at 0x10522c490>
print(max(map(max,a))) #2
print(max(map(max,b))) #[0, 0, 4]
print(max(map(max,b[0])))#2
print(max(map(max,b[1])))