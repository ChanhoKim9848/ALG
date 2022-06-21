def BubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            # 배열 안에있는 처음부터 끝까지 모든 수들을 두 원소씩 서로 비교
            # compare two elements in the array until the end
            if array[i]>array[j]:
                # 만약 오른쪽 원소가 더 크다면 왼쪽 원소와 변경
                # if the right element is bigger, swap the left one for right one
                array[i], array[j] = array[j], array[i]
    return array

# Testing
array=[5,2,3,1,4,-1]
print(BubbleSort(array))
