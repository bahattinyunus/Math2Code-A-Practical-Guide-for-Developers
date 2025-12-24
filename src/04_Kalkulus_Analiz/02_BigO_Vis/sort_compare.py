import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    # O(n^2)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    # O(n log n) average
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(func, data_size):
    data = [random.randint(0, 1000) for _ in range(data_size)]
    start = time.time()
    func(data)
    end = time.time()
    return end - start

if __name__ == "__main__":
    print("--- Algorithmic Complexity Visualizer ---")
    sizes = [10, 50, 100, 200, 500, 1000]
    
    times_bubble = []
    times_quick = []
    
    print(f"{'Size':<10} | {'Bubble (s)':<15} | {'Quick (s)':<15}")
    print("-" * 45)
    
    for n in sizes:
        # Note: We copy data because sort modifies in place for Bubble
        t_b = measure_time(bubble_sort, n)
        t_q = measure_time(lambda d: quick_sort(d), n)
        
        times_bubble.append(t_b)
        times_quick.append(t_q)
        
        print(f"{n:<10} | {t_b:<15.6f} | {t_q:<15.6f}")
        
    try:
        plt.plot(sizes, times_bubble, label="Bubble Sort O(n^2)")
        plt.plot(sizes, times_quick, label="Quick Sort O(n log n)")
        plt.xlabel("Input Size (n)")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.title("Big O Notation in Action")
        # plt.show()
    except ImportError:
        pass
