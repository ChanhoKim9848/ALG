def SelectionSort(array):
    for i in range(len(array)):
        # 가장 작은 원소의 인덱스
        # the index of minimum element in the array
        min_index=i
        
        # 각 원소와 가장 작은원소와 비교
        # compare the minimum element with the next elements 
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                # 만약 가장 작은원소보다 작은 값이 나올경우
                # min_index를 더 작은 값의 인덱스로 교체
                # if the element is smaller than the minimum element 
                # change the previous element's index to the smaller one
                min_index=j
        # swap
        array[min_index],array[i]=array[i],array[min_index]
    return array

# Testing
array=[1,3,2,1,4]
print(SelectionSort(array))
