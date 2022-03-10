print("i m here")
def bubblesort(arr):
    swap=True
    while swap:
        swap=False
       
        for num in range(len(arr)-1):
            if arr[num]>arr[num+1]:
                swap=True
                arr[num],arr[num+1]=arr[num+1],arr[num]

def merge_twosortedlist(arr1,arr2):
    i=0
    j=0
    sorted_arr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    while j<len(arr2):
        sorted_arr.append(arr2[j])
        j+=1
    while i<len(arr1):
        sorted_arr.append(arr1[i])
        i+=1
    return sorted_arr

def mergesort(arr):
    if len(arr)<2:
        return arr[:]
    else:
        mid=len(arr)//2
        l1=mergesort(arr[:mid])
        l2=mergesort(arr[mid:])
        return merge_twosortedlist(l1,l2)

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[-1]
        small, equal, large=[],[],[]
        for num in arr:
            if num<pivot:
                small.append(num)
            elif num>pivot:
                large.append(num)
            else:
                equal.append(num)
        return quicksort(small) + equal + quicksort(large)