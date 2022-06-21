def QuickSort(array,start,end):
    pivot=start
    left=start+1
    right=end
                   # 원소가 1개인 경우 종료
    if start>=end: # if array has one element, stop
        return

    while left<=right:
        # 피벗보다 큰 데이터를 찾을때까지 반복
        # loops until it finds bigger data
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
                        # left와 right 가 엇갈릴 경우 피벗과 right와 교체
        if left>right:  # if left and right cross each other, swap pivot for right
            array[pivot],array[right]=array[right],array[pivot] 
        

        else:          # 작은 데이터와 큰 데이터를 교체
                       # else, swap left for right
            array[left],array[right]=array[right],array[left]

    # 분할 이후 왼쪽과 오른쪽도 똑같이 실행
    # after the array is divided into two parts left and right
    # each part repeats sorting
    QuickSort(array,start,right-1)
    QuickSort(array,right+1,end)


    return array
    
# Testing
array=[1,2,5,6,2,4,3]
print(QuickSort(array,0,len(array)-1))
