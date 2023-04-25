#6-1선택 정렬
array=[7,5,9,0,3,1,6,2,4,8]


for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            i=j
    array[i],array[j]=array[j],array[i] #스와프


print(array)