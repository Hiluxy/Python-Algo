#틀림, 8/15 7565,,

from collections import deque


def getMinimumHealth(initial_players, new_players, rank):
    arr=initial_players
    initial_players.sort(reverse=True) #3,2,1
    hp=arr[rank-1]
    print(arr)
    for new in new_players:
        for i in range(len(arr)):
            if arr[i]<=new:
                arr.insert(i,new) =
                print(arr)
                hp+=arr[rank-1]
                break
    return hp

if __name__ == '__main__':
    a=[82, 99, 84, 84, 59, 59, 58, 11, 33, 100, 32, 43, 26, 88, 61, 58, 86, 79, 69, 29, 24, 78, 19, 41, 62, 97, 54, 70, 91, 100, 32, 4, 71, 21, 26, 80, 11, 13, 69, 74, 29, 52, 34, 43, 76, 53, 83, 33, 26, 89, 97, 80, 24, 98, 85, 6, 49, 15, 38, 61, 10, 89, 8, 94, 65, 24, 96, 82, 18, 63, 85, 4, 19, 96, 40, 25, 80, 92, 77, 57, 38, 58, 48, 13, 92, 98, 24, 43, 78, 80, 95, 52, 70, 58, 27, 10, 56, 99, 71, 10]
    b=[25, 16, 25, 93, 2, 79, 55, 23, 73, 71, 93, 67, 36, 32, 68, 44, 33, 82, 94, 37, 41, 62, 49, 75, 86, 2, 76, 25, 13, 7, 33, 31, 84, 50, 45, 26, 54, 82, 93, 32, 100, 81, 15, 59, 51, 51, 53, 15, 78, 17, 67, 74, 28, 92, 99, 92, 84, 32, 35, 19, 54, 49, 25, 29, 14, 94, 91, 26, 91, 59, 24, 20, 88, 4, 1, 77, 81, 52, 14, 80, 41, 47, 86, 45, 86, 40, 68, 45, 32, 67, 82, 63, 19, 82, 87, 92, 95, 41, 30, 91]
    c=43
    print(getMinimumHealth([1,2],[3,4],2))#6
    print(getMinimumHealth([1,1,3],[2,2,4],2))#8
    print(getMinimumHealth([1,2,3],[6,5,4],1))#21
    print(getMinimumHealth(a,b,c))