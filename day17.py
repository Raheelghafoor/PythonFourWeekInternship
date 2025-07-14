#Question 1
import tracemalloc, functools, time, gc, sys

def memory_profiler_q1(func):
    def wrapper_memory_profiler_q1(*args, **kwargs):
        tracemalloc.start()
        snap_before_q1 = tracemalloc.take_snapshot()
        start_q1 = time.perf_counter()
        result_q1 = func(*args, **kwargs)
        end_q1 = time.perf_counter()
        snap_after_q1 = tracemalloc.take_snapshot()
        tracemalloc.stop()
        diff_q1 = snap_after_q1.compare_to(snap_before_q1, 'filename')
        bytes_used_q1 = sum(stat.size_diff for stat in diff_q1)
        print(f"[Memory] {func.__name__} ran in {(end_q1 - start_q1):.6f}s; Δ = {bytes_used_q1 / 1024:.2f} KB")
        return result_q1
    return wrapper_memory_profiler_q1

@memory_profiler_q1
def sample_task_q1(n_q1):
    data_q1 = [i * i for i in range(n_q1)]
    return sum(data_q1)

#Question 2
def performance_benchmark_q2(functions_q2, args_q2=None):
    if args_q2 is None:
        args_q2 = []

    results_q2 = []

    for func_q2 in functions_q2:
        start_q2 = time.perf_counter()
        func_q2(*args_q2)
        end_q2 = time.perf_counter()
        duration_q2 = end_q2 - start_q2
        results_q2.append((func_q2.__name__, duration_q2))

    print("Execution Time Report:")
    for name_q2, time_taken_q2 in results_q2:
        print(f"{name_q2}: {time_taken_q2:.6f} seconds")

def method_list_comp_q2(n_q2):
    return [i * 2 for i in range(n_q2)]

def method_loop_q2(n_q2):
    result_q2 = []
    for i in range(n_q2):
        result_q2.append(i * 2)
    return result_q2

#Question 3
class LeakyClass_q3:
    def __init__(self):
        self.ref_q3 = self

def simulate_memory_leak_q3():
    leaks_q3 = []
    for _ in range(1000):
        leaks_q3.append(LeakyClass_q3())
    return leaks_q3

def detect_memory_leaks_q3():
    gc.collect()
    objects_q3 = gc.get_objects()
    leak_candidates_q3 = []
    for obj_q3 in objects_q3:
        if isinstance(obj_q3, LeakyClass_q3):
            ref_count_q3 = sys.getrefcount(obj_q3)
            if ref_count_q3 > 3:
                leak_candidates_q3.append((type(obj_q3), ref_count_q3))
    print(f"Potential leaks detected: {len(leak_candidates_q3)}")
    for typ_q3, ref_q3 in leak_candidates_q3[:5]:
        print(f"{typ_q3} with ref count: {ref_q3}")

#Question 4
def gc_analyzer_q4():
    gc.enable()
    print("--- Garbage Collection Analyzer ---")
    print(f"GC Enabled: {gc.isenabled()}")
    print(f"GC Thresholds: {gc.get_threshold()}")
    collected_before_q4 = gc.get_count()
    print(f"GC Objects (before): {collected_before_q4}")
    temp_q4 = []
    for _ in range(100000):
        temp_q4.append([0] * 10)
    del temp_q4
    time.sleep(1)
    collected_now_q4 = gc.collect()
    collected_after_q4 = gc.get_count()
    print(f"GC Collected: {collected_now_q4} objects")
    print(f"GC Objects (after): {collected_after_q4}")
if __name__ == "__main__":
    sample_task_q1(1_000_000)

    funcs_to_test_q2 = [method_list_comp_q2, method_loop_q2]
    performance_benchmark_q2(funcs_to_test_q2, args_q2=[1000000])

    simulate_memory_leak_q3()
    detect_memory_leaks_q3()

    gc_analyzer_q4()


#Question 5
class MemoryPoolManager_q5:
    def __init__(self, pool_size_q5):
        self.pool_q5 = [None] * pool_size_q5
        self.in_use_q5 = [False] * pool_size_q5
        self.size_q5 = pool_size_q5

    def allocate_q5(self, obj_q5):
        for i in range(self.size_q5):
            if not self.in_use_q5[i]:
                self.pool_q5[i] = obj_q5
                self.in_use_q5[i] = True
                print(f"[ALLOCATED] Slot {i} → {obj_q5}")
                return i
        print("[ERROR] No available memory slots!")
        return -1

    def deallocate_q5(self, index_q5):
        if 0 <= index_q5 < self.size_q5 and self.in_use_q5[index_q5]:
            print(f"[DEALLOCATED] Slot {index_q5} ← {self.pool_q5[index_q5]}")
            self.pool_q5[index_q5] = None
            self.in_use_q5[index_q5] = False
        else:
            print("[ERROR] Invalid or unused slot")

    def status_q5(self):
        print("--- Memory Pool Status ---")
        for i in range(self.size_q5):
            status_q5 = "Used" if self.in_use_q5[i] else "Free"
            print(f"Slot {i}: {status_q5}, Value: {self.pool_q5[i]}")

if __name__ == "__main__":
    pool_q5 = MemoryPoolManager_q5(pool_size_q5=5)
    
    a_q5 = pool_q5.allocate_q5("ObjectA")
    b_q5 = pool_q5.allocate_q5("ObjectB")
    c_q5 = pool_q5.allocate_q5("ObjectC")

    pool_q5.status_q5()

    pool_q5.deallocate_q5(b_q5)

    pool_q5.status_q5()

    pool_q5.allocate_q5("ObjectD")
    pool_q5.allocate_q5("ObjectE")
    pool_q5.allocate_q5("ObjectF")

#Question 6
class LifecycleTracker_q6:
    def __init__(self, name_q6):
        self.name_q6 = name_q6
        print(f"[CREATED] Object '{self.name_q6}' initialized.")

    def __del__(self):
        print(f"[DESTROYED] Object '{self.name_q6}' deleted.")
def run_lifecycle_demo_q6():
    print("--- Object Lifecycle Tracker ---")
    obj1_q6 = LifecycleTracker_q6("Alpha")
    obj2_q6 = LifecycleTracker_q6("Beta")
    print("Doing some work with the objects...")
    del obj1_q6
    print("Deleted obj1_q6")
if __name__ == "__main__":
    run_lifecycle_demo_q6()

#Question 7

class RegularPerson_q7:
    def __init__(self, name_q7, age_q7, city_q7):
        self.name_q7 = name_q7
        self.age_q7 = age_q7
        self.city_q7 = city_q7

class OptimizedPerson_q7:
    __slots__ = ['name_q7', 'age_q7', 'city_q7']
    def __init__(self, name_q7, age_q7, city_q7):
        self.name_q7 = name_q7
        self.age_q7 = age_q7
        self.city_q7 = city_q7

def people_generator_q7(count_q7):
    for i in range(count_q7):
        yield OptimizedPerson_q7(f"Name{i}", 20 + i % 10, f"City{i % 5}")

def compare_memory_q7():
    import sys
    print("--- Memory Usage Comparison ---")
    people_regular_q7 = [RegularPerson_q7(f"Name{i}", 25, "City") for i in range(1000)]
    total_regular_q7 = sum(sys.getsizeof(p) for p in people_regular_q7)
    print(f"RegularPerson total size: {total_regular_q7 / 1024:.2f} KB")

    people_optimized_q7 = [OptimizedPerson_q7(f"Name{i}", 25, "City") for i in range(1000)]
    total_optimized_q7 = sum(sys.getsizeof(p) for p in people_optimized_q7)
    print(f"OptimizedPerson total size: {total_optimized_q7 / 1024:.2f} KB")

    print("Iterating with generator:")
    for person_q7 in people_generator_q7(5):
        print(f"{person_q7.name_q7}, {person_q7.age_q7}, {person_q7.city_q7}")

#Question 8
import cProfile, pstats, io, random, time
def bottleneck_finder_q8(func_q8, *args_q8, **kwargs_q8):
    profiler_q8 = cProfile.Profile()
    profiler_q8.enable()
    result_q8 = func_q8(*args_q8, **kwargs_q8)
    profiler_q8.disable()

    report_stream_q8 = io.StringIO()
    pstats.Stats(profiler_q8, stream=report_stream_q8)\
          .strip_dirs()\
          .sort_stats('cumtime')\
          .print_stats(10)
    print("--- Bottleneck Report (cumtime) ---")
    print(report_stream_q8.getvalue())
    return result_q8

def sample_pipeline_q8(size_q8):
    data_stage1_q8 = [random.random() for _ in range(size_q8)]
    data_stage2_q8 = [val_q8 ** 2 for val_q8 in data_stage1_q8]
    data_stage3_q8 = sorted(data_stage2_q8)
    result_stage4_q8 = sum(data_stage3_q8)
    time.sleep(0.2)
    return result_stage4_q8

#Question 9
from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci_q9(n_q9):
    if n_q9 < 2:
        return n_q9
    return fibonacci_q9(n_q9 - 1) + fibonacci_q9(n_q9 - 2)

def cache_stats_report_q9():
    print("--- LRU Cache Efficiency Analyzer ---")
    fibonacci_q9.cache_clear()
    for i in range(30):
        fibonacci_q9(i)

    stats_q9 = fibonacci_q9.cache_info()
    print(f"Hits: {stats_q9.hits}")
    print(f"Misses: {stats_q9.misses}")
    print(f"Max Size: {stats_q9.maxsize}")
    print(f"Current Size: {stats_q9.currsize}")

if __name__ == "__main__":
    compare_memory_q7()
    bottleneck_finder_q8(sample_pipeline_q8, 1_000_000)
    cache_stats_report_q9()

#Question 10
import random
import time

class MemoryBlock_q10:
    def __init__(self, size_q10, label_q10):
        self.data_q10 = bytearray(size_q10)
        self.label_q10 = label_q10

class MemorySimulator_q10:
    def __init__(self, total_blocks_q10):
        self.pool_q10 = [None] * total_blocks_q10
        self.total_q10 = total_blocks_q10

    def allocate_q10(self, size_q10, label_q10):
        for i in range(self.total_q10):
            if self.pool_q10[i] is None:
                self.pool_q10[i] = MemoryBlock_q10(size_q10, label_q10)
                print(f"[ALLOCATED] Slot {i} ← '{label_q10}' ({size_q10} bytes)")
                return i
        print("[ERROR] No available memory slot.")
        return -1

    def free_q10(self, index_q10):
        if 0 <= index_q10 < self.total_q10 and self.pool_q10[index_q10]:
            print(f"[FREED] Slot {index_q10} ← '{self.pool_q10[index_q10].label_q10}'")
            self.pool_q10[index_q10] = None

    def visualize_q10(self):
        print("--- Memory Fragmentation Map ---")
        for i, block_q10 in enumerate(self.pool_q10):
            if block_q10:
                print(f"[{i}] {block_q10.label_q10}", end="  ")
            else:
                print(f"[{i}] ....", end="  ")
        print("\n")

def simulate_fragmentation_q10():
    sim_q10 = MemorySimulator_q10(20)
    ids_q10 = []
    ids_q10.append(sim_q10.allocate_q10(1000, "LargeA"))
    ids_q10.append(sim_q10.allocate_q10(100, "SmallB"))
    ids_q10.append(sim_q10.allocate_q10(1000, "LargeC"))
    ids_q10.append(sim_q10.allocate_q10(100, "SmallD"))
    sim_q10.visualize_q10()
    sim_q10.free_q10(ids_q10[1])
    sim_q10.free_q10(ids_q10[3])
    sim_q10.visualize_q10()
    sim_q10.allocate_q10(100, "TinyE")
    sim_q10.allocate_q10(100, "TinyF")
    sim_q10.visualize_q10()

if __name__ == "__main__":
    simulate_fragmentation_q10()

#Question 11
import psutil
import os
import time

def resource_usage_monitor_q11(duration_q11=10, interval_q11=2):
    print("--- Live Resource Usage Monitor ---")
    process_q11 = psutil.Process(os.getpid())

    start_time_q11 = time.time()
    while time.time() - start_time_q11 < duration_q11:
        cpu_percent_q11 = process_q11.cpu_percent(interval=None)
        mem_info_q11 = process_q11.memory_info()
        print(f"[CPU] {cpu_percent_q11:.2f}%  |  [Memory] RSS: {mem_info_q11.rss / 1024 / 1024:.2f} MB")
        time.sleep(interval_q11)

if __name__ == "__main__":
    resource_usage_monitor_q11(duration_q11=10, interval_q11=2)

#Question 12
import time
import json
import os

benchmark_file_q12 = "benchmarks_q12.json"

def save_benchmark_q12(func_name_q12, time_q12):
    data_q12 = {}
    if os.path.exists(benchmark_file_q12):
        with open(benchmark_file_q12, "r") as f_q12:
            data_q12 = json.load(f_q12)
    data_q12[func_name_q12] = time_q12
    with open(benchmark_file_q12, "w") as f_q12:
        json.dump(data_q12, f_q12, indent=2)
    print(f"[Saved] Benchmark for {func_name_q12}: {time_q12:.6f}s")

def load_benchmark_q12(func_name_q12):
    if not os.path.exists(benchmark_file_q12):
        return None
    with open(benchmark_file_q12, "r") as f_q12:
        data_q12 = json.load(f_q12)
    return data_q12.get(func_name_q12)

def performance_test_q12(func_q12, *args_q12, threshold_q12=1.10, save=False):
    start_q12 = time.perf_counter()
    result_q12 = func_q12(*args_q12)
    end_q12 = time.perf_counter()
    elapsed_q12 = end_q12 - start_q12

    previous_q12 = load_benchmark_q12(func_q12.__name__)
    print(f"[Tested] {func_q12.__name__} took {elapsed_q12:.6f}s")

    if previous_q12:
        if elapsed_q12 > previous_q12 * threshold_q12:
            print(f"[WARNING] Performance regression detected! "
                  f"Previous: {previous_q12:.6f}s, Now: {elapsed_q12:.6f}s")
        else:
            print(f"[OK] No regression. Previous: {previous_q12:.6f}s")

    if save or previous_q12 is None:
        save_benchmark_q12(func_q12.__name__, elapsed_q12)

    return result_q12

def slow_function_q12(n_q12):
    return sum(i * i for i in range(n_q12))

#Question 13
import psutil

def memory_stress_test_q13():
    print("--- Simple Memory Stress Test ---")
    process_q13 = psutil.Process(os.getpid())

    for size_q13 in [1_000_000, 2_000_000, 4_000_000, 8_000_000]:
        start_mem_q13 = process_q13.memory_info().rss / 1024 / 1024
        start_time_q13 = time.time()

        data_q13 = [x * 2 for x in range(size_q13)]
        total_q13 = sum(data_q13)

        end_time_q13 = time.time()
        end_mem_q13 = process_q13.memory_info().rss / 1024 / 1024

        print(f"Size: {size_q13:,}")
        print(f"Time Taken: {end_time_q13 - start_time_q13:.2f} seconds")
        print(f"Memory Used: {end_mem_q13 - start_mem_q13:.2f} MB\n")

        del data_q13, total_q13

if __name__ == "__main__":
    performance_test_q12(slow_function_q12, 10_000_000, save=True)
    memory_stress_test_q13()

# Question 14 ────────────────────────────────────────────────
import ast, inspect

def performance_tips_q14(func_q14):
    print(f"--- Optimization Tips for: {func_q14.__name__} ---")
    source_q14 = inspect.getsource(func_q14)
    tree_q14   = ast.parse(source_q14)

    tips_q14 = set()
    for node_q14 in ast.walk(tree_q14):
        if isinstance(node_q14, ast.For):
            tips_q14.add("Consider using list comprehensions or generator expressions.")
        if isinstance(node_q14, ast.Import):
            tips_q14.add("Use lazy imports (inside functions) if the module isn’t always needed.")
        if isinstance(node_q14, ast.List):
            tips_q14.add("Use a generator (`()`) instead of a list (`[]`) if you only iterate once.")
        if isinstance(node_q14, ast.Call) and isinstance(node_q14.func, ast.Name):
            if node_q14.func.id == "range":
                tips_q14.add("If looping over huge ranges, iterate in chunks to save memory.")
        if isinstance(node_q14, ast.Assign) and isinstance(node_q14.value, ast.BinOp):
            tips_q14.add("Consider loop unrolling when repeating arithmetic operations.")

    if tips_q14:
        for tip in tips_q14:
            print("•", tip)
    else:
        print("No obvious optimizations found ✅")

def sample_user_function_q14():
    import math
    total = 0
    for i in range(1000):
        total += i * 2
    mylist = [i**2 for i in range(1000)]
    return sum(mylist)

# Question 15 ────────────────────────────────────────────────
import tracemalloc, psutil, os, gc, sys

class MemoryDebuggerToolkit_q15:
    def __init__(self):
        self.proc = psutil.Process(os.getpid())

    def show_mem(self, label="Memory"):
        print(f"[{label}] {self.proc.memory_info().rss / 1024 / 1024:.2f} MB")

    def start_track(self):
        tracemalloc.start()
        self.snap_start = tracemalloc.take_snapshot()
        print("[Tracker] started")

    def stop_track(self):
        top = tracemalloc.take_snapshot().compare_to(self.snap_start, "lineno")
        print("[Tracker] top allocations:")
        for stat in top[:5]:
            print(stat)
        tracemalloc.stop()

    def detect_leaks(self, clazz=None):
        gc.collect()
        suspects = []
        for obj in gc.get_objects():
            if clazz and not isinstance(obj, clazz):
                continue
            if sys.getrefcount(obj) > 3:
                suspects.append((type(obj), sys.getrefcount(obj)))
        print(f"[Leaks] {len(suspects)} potential leaks")
        for t, r in suspects[:5]:
            print(t, "refcount =", r)

class Dummy_q15:
    def __init__(self):
        self.loop = self  # self‑ref for leak demo

def simulate_leak_q15():
    return [Dummy_q15() for _ in range(1000)]

# Unified demo ───────────────────────────────────────────────
if __name__ == "__main__":
    # Q‑14 demo
    performance_tips_q14(sample_user_function_q14)
    print()

    # Q‑15 demo
    toolkit = MemoryDebuggerToolkit_q15()
    toolkit.show_mem("Before work")

    toolkit.start_track()
    _data = [i * 2 for i in range(1_000_000)]  # load
    toolkit.stop_track()

    toolkit.show_mem("After load")

    simulate_leak_q15()
    toolkit.detect_leaks(Dummy_q15)

#✅ 15 Python Coding Tasks – Algorithm Complexity Analysis
#Question 1
import ast, inspect

def big_o_analyzer_q1(func_q1):
    print(f"--- Time Complexity Estimator for: {func_q1.__name__} ---")
    source_q1 = inspect.getsource(func_q1)
    tree_q1 = ast.parse(source_q1)

    max_depth_q1 = [0]

    def analyze_node_q1(node_q1, depth_q1=0):
        if isinstance(node_q1, (ast.For, ast.While)):
            depth_q1 += 1
            max_depth_q1[0] = max(max_depth_q1[0], depth_q1)
        for child_q1 in ast.iter_child_nodes(node_q1):
            analyze_node_q1(child_q1, depth_q1)

    analyze_node_q1(tree_q1)

    if max_depth_q1[0] == 0:
        print("Estimated Time Complexity: O(1) – No loops found")
    elif max_depth_q1[0] == 1:
        print("Estimated Time Complexity: O(n) – Single loop")
    elif max_depth_q1[0] == 2:
        print("Estimated Time Complexity: O(n^2) – Nested loop")
    elif max_depth_q1[0] == 3:
        print("Estimated Time Complexity: O(n^3) – Triple nested loop")
    else:
        print("Estimated Time Complexity: O(n^k) – Deep nesting")

def example_loop_q1():
    for i in range(10):          
        for j in range(10):      
            print(i, j)
if __name__ == "__main__":
    performance_tips_q14(sample_user_function_q14)
    print()
    toolkit = MemoryDebuggerToolkit_q15()
    toolkit.show_mem("Before work")
    toolkit.start_track()
    _data = [i * 2 for i in range(1_000_000)]
    toolkit.stop_track()
    toolkit.show_mem("After load")
    simulate_leak_q15()
    toolkit.detect_leaks(Dummy_q15)
    print()
    big_o_analyzer_q1(example_loop_q1)

#Question 2
import time
import matplotlib.pyplot as plt

def time_complexity_plot_q2(func_q2, input_sizes_q2):
    times_q2 = []

    for size_q2 in input_sizes_q2:
        start_q2 = time.perf_counter()
        func_q2(size_q2)
        end_q2 = time.perf_counter()
        elapsed_q2 = end_q2 - start_q2
        times_q2.append(elapsed_q2)
        print(f"Input: {size_q2:,} → Time: {elapsed_q2:.6f}s")

    plt.plot(input_sizes_q2, times_q2, marker='o')
    plt.title(f"Time Complexity Estimation: {func_q2.__name__}")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def sample_linear_task_q2(n_q2):
    return [i * 2 for i in range(n_q2)]


#Question 3
import tracemalloc

def space_complexity_tracker_q3(func_q3, input_sizes_q3):
    print(f"--- Space Complexity Tracker: {func_q3.__name__} ---")
    results_q3 = []

    for size_q3 in input_sizes_q3:
        tracemalloc.start()
        func_q3(size_q3)
        current_q3, peak_q3 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results_q3.append((size_q3, peak_q3 / 1024))  # in KB
        print(f"Input: {size_q3:,} → Peak Memory: {peak_q3 / 1024:.2f} KB")

    print("\nSummary Table:")
    for size_q3, mem_q3 in results_q3:
        print(f"• n = {size_q3:<8} → Peak = {mem_q3:.2f} KB")

def sample_memory_task_q3(n_q3):
    return [i * 2 for i in range(n_q3)]

#Question 4

import time
import tracemalloc
import random

def compare_algorithms_q4(funcs_q4, input_data_q4, target_q4=None):
    print(f"--- Algorithm Comparison ---")
    for func_q4 in funcs_q4:
        # Measure time
        start_q4 = time.perf_counter()
        tracemalloc.start()
        if target_q4 is not None:
            func_q4(input_data_q4, target_q4)
        else:
            func_q4(input_data_q4)
        current_q4, peak_q4 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_q4 = time.perf_counter()
        
        duration_q4 = end_q4 - start_q4
        print(f"{func_q4.__name__}: Time = {duration_q4:.6f}s | Peak Memory = {peak_q4 / 1024:.2f} KB")

# --- Linear Search ---
def linear_search_q4(arr_q4, target_q4):
    for item_q4 in arr_q4:
        if item_q4 == target_q4:
            return True
    return False

# --- Binary Search ---
def binary_search_q4(arr_q4, target_q4):
    left_q4, right_q4 = 0, len(arr_q4) - 1
    while left_q4 <= right_q4:
        mid_q4 = (left_q4 + right_q4) // 2
        if arr_q4[mid_q4] == target_q4:
            return True
        elif arr_q4[mid_q4] < target_q4:
            left_q4 = mid_q4 + 1
        else:
            right_q4 = mid_q4 - 1
    return False

def bubble_sort_q4(arr_q4):
    n_q4 = len(arr_q4)
    for i_q4 in range(n_q4):
        for j_q4 in range(0, n_q4 - i_q4 - 1):
            if arr_q4[j_q4] > arr_q4[j_q4 + 1]:
                arr_q4[j_q4], arr_q4[j_q4 + 1] = arr_q4[j_q4 + 1], arr_q4[j_q4]

def builtin_sort_q4(arr_q4):
    return sorted(arr_q4)

#Question 5
def performance_predictor_q5(past_sizes_q5, past_times_q5, future_size_q5):
    """
    past_sizes_q5  : list[int]   – previously‑measured input sizes
    past_times_q5  : list[float] – corresponding execution times (seconds)
    future_size_q5 : int         – input size you want to predict for

    Returns the predicted runtime (seconds) using y = a·n + b.
    """
    if len(past_sizes_q5) != len(past_times_q5) or len(past_sizes_q5) == 0:
        raise ValueError("Past sizes and times must be the same non‑zero length.")

  
    n = len(past_sizes_q5)
    sum_x  = sum(past_sizes_q5)
    sum_y  = sum(past_times_q5)
    sum_xx = sum(x * x for x in past_sizes_q5)
    sum_xy = sum(x * y for x, y in zip(past_sizes_q5, past_times_q5))

    denominator = n * sum_xx - sum_x ** 2
    if denominator == 0:
        raise ValueError("Cannot compute predictor (denominator zero).")

    a = (n * sum_xy - sum_x * sum_y) / denominator   
    b = (sum_y * sum_xx - sum_x * sum_xy) / denominator  

    predicted = a * future_size_q5 + b
    print(f"[Predictor] Using y = {a:.6e}·n + {b:.6e}")
    print(f"[Predictor] For n = {future_size_q5:,} → predicted time ≈ {predicted:.6f}s")
    return predicted

#Question 6
import ast
import inspect

def optimization_suggester_q6(func_q6):
    print(f"--- Optimization Suggestions for: {func_q6.__name__} ---")
    source_q6 = inspect.getsource(func_q6)
    tree_q6 = ast.parse(source_q6)

    suggestions_q6 = []

    for node_q6 in ast.walk(tree_q6):
        if isinstance(node_q6, ast.For):
            if isinstance(node_q6.iter, ast.Call) and getattr(node_q6.iter.func, 'id', '') == "range":
                suggestions_q6.append("Consider using list comprehension if appending to a list inside loop.")
        if isinstance(node_q6, ast.ListComp):
            suggestions_q6.append("If result is used only once, consider using generator expression for less memory.")
        if isinstance(node_q6, ast.Call) and isinstance(node_q6.func, ast.Name):
            if node_q6.func.id == "sorted":
                suggestions_q6.append("Use in-place sort (list.sort()) if you don’t need a new list.")
        if isinstance(node_q6, ast.Assign) and isinstance(node_q6.value, ast.BinOp):
            if isinstance(node_q6.value.op, ast.Add):
                suggestions_q6.append("Avoid string concatenation in loops; use ''.join() instead.")

    if suggestions_q6:
        for s_q6 in set(suggestions_q6):
            print(f"• {s_q6}")
    else:
        print("No obvious improvements found.")

def sample_algorithm_q6():
    result = []
    for i in range(1000):
        result.append(i * i)
    sorted_result = sorted(result)
    combined = ""
    for i in range(10):
        combined += str(i)
    return combined

#Question 7
import matplotlib.pyplot as plt
import time
import psutil
import os

def complexity_visualizer_q7(func_q7, input_sizes_q7):
    times_q7 = []
    memories_q7 = []
    process_q7 = psutil.Process(os.getpid())

    for size_q7 in input_sizes_q7:
        start_mem_q7 = process_q7.memory_info().rss / 1024 / 1024
        start_time_q7 = time.perf_counter()

        func_q7(size_q7)  # run the function

        end_time_q7 = time.perf_counter()
        end_mem_q7 = process_q7.memory_info().rss / 1024 / 1024

        times_q7.append(end_time_q7 - start_time_q7)
        memories_q7.append(end_mem_q7 - start_mem_q7)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(input_sizes_q7, times_q7, marker='o')
    plt.title("Time Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")

    plt.subplot(1, 2, 2)
    plt.plot(input_sizes_q7, memories_q7, marker='o', color='orange')
    plt.title("Memory Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Memory Used (MB)")

    plt.tight_layout()
    plt.show()

def example_function_q7(n_q7):
    return [i ** 2 for i in range(n_q7)]

#Question 8
import time

def recursive_fib_q8(n_q8):
    if n_q8 <= 1:
        return n_q8
    return recursive_fib_q8(n_q8 - 1) + recursive_fib_q8(n_q8 - 2)

def iterative_fib_q8(n_q8):
    if n_q8 <= 1:
        return n_q8
    a_q8, b_q8 = 0, 1
    for _ in range(2, n_q8 + 1):
        a_q8, b_q8 = b_q8, a_q8 + b_q8
    return b_q8

def test_efficiency_q8(funcs_q8, input_q8):
    print(f"--- Algorithm Efficiency Tester (n = {input_q8}) ---")
    for func_q8 in funcs_q8:
        start_q8 = time.perf_counter()
        result_q8 = func_q8(input_q8)
        end_q8 = time.perf_counter()
        print(f"{func_q8.__name__} = {result_q8}, Time: {(end_q8 - start_q8):.6f}s")

#Question 9
import time
def detect_regression_q9(old_func_q9, new_func_q9, input_q9, threshold_q9=1.10):
    print(f"--- Performance Regression Detector (n = {input_q9}) ---")
    start_old_q9 = time.perf_counter()
    old_result_q9 = old_func_q9(input_q9)
    end_old_q9 = time.perf_counter()
    time_old_q9 = end_old_q9 - start_old_q9
    start_new_q9 = time.perf_counter()
    new_result_q9 = new_func_q9(input_q9)
    end_new_q9 = time.perf_counter()
    time_new_q9 = end_new_q9 - start_new_q9
    print(f"Old Function Time: {time_old_q9:.6f}s")
    print(f"New Function Time: {time_new_q9:.6f}s")
    if new_result_q9 != old_result_q9:
        print("[ERROR] Functions return different results!")
    elif time_new_q9 > time_old_q9 * threshold_q9:
        print("[⚠ WARNING] Performance regression detected!")
    else:
        print("[ OK] No regression detected.")
def slow_version_q9(n_q9):
    total_q9 = 0
    for i in range(n_q9):
        total_q9 += i * i
    return total_q9

def fast_version_q9(n_q9):
    return sum(i * i for i in range(n_q9))

#Question 10
import time
import psutil
import os

def scalability_analyzer_q10(func_q10, input_sizes_q10):
    print("--- Scalability Analyzer ---")
    process_q10 = psutil.Process(os.getpid())

    for size_q10 in input_sizes_q10:
        print(f"\nInput Size: {size_q10:,}")

        start_mem_q10 = process_q10.memory_info().rss / 1024 / 1024  # in MB
        start_time_q10 = time.perf_counter()

        func_q10(size_q10) 

        end_time_q10 = time.perf_counter()
        end_mem_q10 = process_q10.memory_info().rss / 1024 / 1024

        print(f"Time Taken: {(end_time_q10 - start_time_q10):.4f} seconds")
        print(f"Memory Used: {(end_mem_q10 - start_mem_q10):.4f} MB")

def scalable_example_q10(n_q10):
    return [i * i for i in range(n_q10)]

#Question 11
import time

def bottleneck_identifier_q11():
    print("--- Bottleneck Identifier ---")

    start1_q11 = time.perf_counter()
    data_q11 = [i for i in range(1_000_000)]  # Line 1
    end1_q11 = time.perf_counter()

    start2_q11 = time.perf_counter()
    squared_q11 = [x * x for x in data_q11]  # Line 2
    end2_q11 = time.perf_counter()

    start3_q11 = time.perf_counter()
    total_q11 = sum(squared_q11)  # Line 3
    end3_q11 = time.perf_counter()

    print(f"Line 1 (Create list): {end1_q11 - start1_q11:.6f}s")
    print(f"Line 2 (Square values): {end2_q11 - start2_q11:.6f}s")
    print(f"Line 3 (Sum): {end3_q11 - start3_q11:.6f}s")

#Question 12
import psutil
import os
import time

def resource_utilization_tracker_q12(func_q12, *args_q12, **kwargs_q12):
    print("--- Resource Utilization Tracker ---")
    process_q12 = psutil.Process(os.getpid())

    cpu_start_q12 = psutil.cpu_percent(interval=None)
    mem_before_q12 = process_q12.memory_info().rss / 1024 / 1024
    io_before_q12 = process_q12.io_counters()

    start_time_q12 = time.perf_counter()
    result_q12 = func_q12(*args_q12, **kwargs_q12)
    end_time_q12 = time.perf_counter()

    cpu_end_q12 = psutil.cpu_percent(interval=None)
    mem_after_q12 = process_q12.memory_info().rss / 1024 / 1024
    io_after_q12 = process_q12.io_counters()

    print(f"Time Taken: {end_time_q12 - start_time_q12:.4f} seconds")
    print(f"Memory Used: {mem_after_q12 - mem_before_q12:.2f} MB")
    print(f"CPU % (avg snapshot): {(cpu_start_q12 + cpu_end_q12) / 2:.2f}%")
    print(f"Disk Read Bytes: {(io_after_q12.read_bytes - io_before_q12.read_bytes) / 1024:.2f} KB")
    print(f"Disk Write Bytes: {(io_after_q12.write_bytes - io_before_q12.write_bytes) / 1024:.2f} KB")

    return result_q12

def example_workload_q12(n_q12):
    data_q12 = [i ** 2 for i in range(n_q12)]
    return sum(data_q12)

#Question 13
import time
import psutil
import os

def measure_metrics_q13(func_q13, *args_q13):
    process_q13 = psutil.Process(os.getpid())

    mem_before_q13 = process_q13.memory_info().rss / 1024 / 1024
    start_time_q13 = time.perf_counter()

    result_q13 = func_q13(*args_q13)

    end_time_q13 = time.perf_counter()
    mem_after_q13 = process_q13.memory_info().rss / 1024 / 1024

    time_taken_q13 = end_time_q13 - start_time_q13
    mem_used_q13 = mem_after_q13 - mem_before_q13

    return {
        "function": func_q13.__name__,
        "time": round(time_taken_q13, 4),
        "memory": round(mem_used_q13, 2)
    }

def show_dashboard_q13(algorithms_q13, input_arg_q13):
    print("--- Performance Metrics Dashboard ---")
    print("{:<25} {:>10} {:>10}".format("Function", "Time (s)", "Memory (MB)"))
    print("-" * 50)
    for algo_q13 in algorithms_q13:
        metrics_q13 = measure_metrics_q13(algo_q13, input_arg_q13)
        print("{:<25} {:>10} {:>10}".format(metrics_q13["function"], metrics_q13["time"], metrics_q13["memory"]))

def linear_sum_q13(n_q13):
    return sum(range(n_q13))

def quadratic_sum_q13(n_q13):
    return sum(i * j for i in range(n_q13) for j in range(n_q13))

#Question 14

def algorithm_selector_q14(task_q14, constraint_q14):
    task_q14 = task_q14.lower()
    constraint_q14 = constraint_q14.lower()

    if "search" in task_q14:
        if "sorted" in task_q14 and "low memory" in constraint_q14:
            return "Use Binary Search (low memory, fast on sorted data)"
        elif "low time" in constraint_q14:
            return "Use Hash Table or Dictionary Search"
        else:
            return "Use Linear Search"

    elif "sort" in task_q14:
        if "low memory" in constraint_q14:
            return "Use In-Place Quick Sort or Selection Sort"
        elif "stable" in constraint_q14:
            return "Use Merge Sort (stable but more memory)"
        else:
            return "Use Quick Sort"

    elif "path" in task_q14 or "graph" in task_q14:
        if "shortest" in task_q14:
            return "Use Dijkstra's Algorithm"
        elif "all pairs" in task_q14:
            return "Use Floyd-Warshall Algorithm"
        else:
            return "Use BFS or DFS"

    elif "matrix" in task_q14:
        if "sparse" in constraint_q14:
            return "Use Sparse Matrix Representation (CSR/COO)"
        else:
            return "Use 2D List or NumPy Array"

    elif "optimize" in task_q14:
        return "Use Dynamic Programming or Greedy Algorithms"

    return "No suitable algorithm found. Try to be more specific with task/constraints."

if __name__ == "__main__":
    print("--- Algorithm Selector Tool ---")
    print(algorithm_selector_q14("Find element in sorted list", "low memory"))
    print(algorithm_selector_q14("Sort large dataset", "stable"))
    print(algorithm_selector_q14("Find shortest path", "low time"))


#Question 15
import time, psutil, os, tracemalloc, inspect, ast

def optimisation_framework_q15(func_q15, *args_q15, time_thresh_q15=0.5, mem_thresh_q15=50.0):
    """
    Runs `func_q15`, measures runtime & peak memory, then prints simple tips
    if the thresholds are exceeded.

    • time_thresh_q15  – seconds considered “slow”
    • mem_thresh_q15   – MB considered “high memory”
    """
    proc_q15 = psutil.Process(os.getpid())

   
    tracemalloc.start()
    mem_before_q15 = proc_q15.memory_info().rss / 1024 / 1024

    t0_q15 = time.perf_counter()
    result_q15 = func_q15(*args_q15)
    t1_q15 = time.perf_counter()

    current_q15, peak_q15 = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    mem_after_q15 = proc_q15.memory_info().rss / 1024 / 1024

    runtime_q15 = t1_q15 - t0_q15                       
    delta_mem_q15 = mem_after_q15 - mem_before_q15      
    peak_mem_q15  = peak_q15 / 1024 / 1024              

    print(f"--- Optimisation Framework for: {func_q15.__name__} ---")
    print(f"Time Taken  : {runtime_q15:.4f} s")
    print(f"Δ RSS       : {delta_mem_q15:.2f} MB")
    print(f"Peak Memory : {peak_mem_q15:.2f} MB")

   
    suggestions_q15 = []

    if runtime_q15 > time_thresh_q15:
        suggestions_q15.append("• Function is slow → consider algorithmic improvements "
                               "(e.g., avoid nested loops, use vectorisation, caching, or C‑extensions).")

    if peak_mem_q15 > mem_thresh_q15:
        suggestions_q15.append("• High peak memory → consider generators, chunked processing, "
                               "or in‑place operations.")

  
    src_q15  = inspect.getsource(func_q15)
    tree_q15 = ast.parse(src_q15)

    for node_q15 in ast.walk(tree_q15):
        if isinstance(node_q15, ast.For) and isinstance(node_q15.iter, ast.Call):
            if getattr(node_q15.iter.func, "id", "") == "range":
                suggestions_q15.append("• Detected `for … range()` loop → if possible, use NumPy/itertools "
                                       "or comprehension for speed.")
        if isinstance(node_q15, ast.ListComp):
            suggestions_q15.append("• Detected list comprehension → if result is consumed once, "
                                   "switch to generator expression to save memory.")
        if isinstance(node_q15, ast.Call) and getattr(node_q15.func, "id", "") == "append":
            suggestions_q15.append("• Many `.append()` calls → pre‑allocate list or use comprehension.")

    if suggestions_q15:
        print("\nSuggestions:")
        for tip_q15 in dict.fromkeys(suggestions_q15):   
            print(tip_q15)
    else:
        print("\nNo suggestions — performance looks fine ")

    return result_q15 







