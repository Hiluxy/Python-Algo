#재귀,문자열,조합

def comb(arr, n):
    result = []
    # if n > len(arr):
    #     return result
 
    if n == 1:
        for i in arr:
            result.append([i])
           
    elif n > 1:
        for i in range(len(arr) - n + 1): #[1,2,3,4,5,6,7] 이면 i=0,1
            for j in comb(arr[i + 1:], n - 1): #i=0일때 0다음부터 조합 찾기
                result.append([arr[i]] + j)
 
    return result


if __name__ == "__main__":
    while True:
        arr=list(map(str,input().split()))
        if arr[0]=='0':
            break
        else:
            arr.pop(0) #첫 인덱스 지우기
            com_arr=comb(arr,6)
            for c in com_arr:
                print(' '.join(c))
            print()

