import random
import os
import time

num_arr=[]

def random_arr(number): # Generate the amount of random float numbers into the list
    for i in range(int(number)):
        num=round(random.uniform(0, 1), 5)
        num_arr.append(num)
    print(f'Original Array: {num_arr}')

def insertion_sort(bucket): # Insertion sort is used to sort numbers within every bucket
    for i in range(1, len(bucket)):
        key=bucket[i]
        j=i-1
        while j>=0 and bucket[j]>key:
            bucket[j+1]=bucket[j]
            j-=1
        bucket[j+1]=key

def bucket_sort(array):
    start_time=time.time() # Stores the start of time
    length=len(array)
    buckets=[[] for _ in range(length)]
    
    for item in array: # The list is divided into multiple buckets, the numbers with the same intoger after multiplication will be placed inside a bucket
        temp=int(length*item) 
        buckets[temp].append(item)
    print('\nBuckets:')
    for i in range(len(buckets)):
        print(buckets[i], end='\n')
    
    for bucket in buckets: # Implementation of insertion sort
        insertion_sort(bucket)

    index=0
    for bucket in buckets: # The buckets after the insertion sorts are combined together
        for num in bucket:
            num_arr[index]=num
            index+=1
    print(f'\nSorted Array: {num_arr}')

    end_time=time.time()
    time_used=end_time-start_time # Calculate the time used to do the entire sorting
    print(f'time used: {time_used} second')

os.system('cls||clear')
value=input('Enter the amount of random numbers you want to generate: ') # Users can choose the number of random numbers to be generated
random_arr(value)
bucket_sort(num_arr)