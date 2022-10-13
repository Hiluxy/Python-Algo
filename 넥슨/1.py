#통과

def minNum(samDaily, kellyDaily, difference):
    sam=samDaily+difference
    kelly=kellyDaily
    cnt=1
    if sam>=kelly and samDaily>=kellyDaily:
        return -1
    else:
        while sam>=kelly:
            sam+=samDaily
            kelly+=kellyDaily
            cnt+=1
        return cnt

if __name__ == '__main__':
    print(minNum(3,5,1)) #1
