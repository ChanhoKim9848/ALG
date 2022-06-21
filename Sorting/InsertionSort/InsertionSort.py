def InsertionSort(array):
    # 첫번째 원소는 이미 정렬이 되어있다고 가정
    # Assuming that the first element in the array is already sorted
    for i in range(1,len(array)):
        # 인덱스 i부터 1까지 1씩 감소하며 반복
        # from index i to 1, it decreases by 1
        # and compare two elements
        for j in range(i,0,-1):
            if array[j]<array[j-1]: # 한칸씩 이동
                                    # moves one by one to the left
                array[j],array[j-1]=array[j-1],array[j]
            else:   # 자신보다 작은 값을 만나면 종료
                    # if it is less than the left one, it stops
                break
    return array

# Testing
array=[1,4,2,5,6]
print(InsertionSort(array))