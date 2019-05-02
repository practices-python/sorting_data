def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        elif right[j]>left[i]:
            result.append(left[i])
            i+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
def sort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=sort(array[:mid])
    right=sort(array[mid:])
    return merge(left,right)
    
