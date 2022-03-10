from demos import quicksort, mergesort, bubblesort
import time
import random

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list
def analyze_func(func_name, arr):
    tic=time.time()
    func_name(arr)
    toc=time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")
size = int(input("what size list do you want to create?"))
max = int(input("what is the max value of the range?"))
run_times = int(input("how many times do you want to run?"))
for num in range(run_times):
    print(f"Run: {num+1}")
    l= create_random_list(size,max)
    analyze_func(bubblesort, l.copy())
    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    print("-"*40)