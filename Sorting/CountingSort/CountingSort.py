def CountingSort(array):
    # 각 원소의 갯수를 세기위해 
    # 배열 안에 가장 큰 원소의 수의 크기를 가진 배열을 생성
    # make an array list that its size is the maximum number in the array
    # to count the number of each element in it
    count=[0]*(max(array)+1)
    
    # 배열 안에있는 각 원소의 갯수를 세서 count에 저장
    # count the number of each element and save it into count array
    for i in array:
        count[i]+=1
    
    # array안에 있는 원소들을 다시 오름차순으로 배치하기 위해 초기화
    # empty the array to sort elements in ascending order
    array=[]

    # array 배열안에 다시 순서대로 각 원소를 오름차순으로 넣기
    # insert index number of count array by the number of each element
    for i in range(len(count)):
        for j in range(count[i]):
            array.append(i)
    return array

# Testing
array=[1,4,2,3,2]
print(CountingSort(array))
