def BinarySearch(array, target):
    # 찾고자 하는 target 은 array에 존재
    # array where the target which we want to find exists
    left=0
    right=len(array)-1
    mid = int((left+right)/2)

    # 배열은 오름차순으로 정렬이 돼 있어야함
    # array needs to be sorted in ascending order to find the target
    array.sort()
    
    # left와 right가 겹칠때까지 반복
    # iterates until left and right overlap each other
    while left<=right:

        # mid 값에 target이 존재한다면, mid값을 반환
        # if target is on the mid position, returns on it
        if array[mid]==target:
            return mid
        
        # 타겟이 mid보다 오른쪽에 있을경우, left를 mid 오른쪽에 위치
        # if target is on the right side of the mid, left goes to 
        # right side of the mid
        elif target>mid:
            left=mid+1

        # 그 외 경우는 right 가 mid에 왼쪽에 위치
        # else, right goes to the left side of the mid
        else:
            right=mid-1

    # 못 찾을경우 -1을 반환
    # if target is not found, then return -1
    return -1

# Testing

array=[1,2,4,5,6,7,8]
print(BinarySearch(array, 5))



            


    
