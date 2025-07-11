#Question 1
print("\n#Question 1 - Bubble Sort (Ascending Order)")
unsorted_list_q1 = [5, 2, 9, 1, 7]
length_q1 = len(unsorted_list_q1)
for pass_q1 in range(length_q1 - 1):
    for i_q1 in range(length_q1 - pass_q1 - 1):
        if unsorted_list_q1[i_q1] > unsorted_list_q1[i_q1 + 1]:
            temp_q1                   = unsorted_list_q1[i_q1]
            unsorted_list_q1[i_q1]    = unsorted_list_q1[i_q1 + 1]
            unsorted_list_q1[i_q1 + 1] = temp_q1
print("Sorted List:", unsorted_list_q1)

#Question 2
print("\n#Question 2 - Selection Sort (Ascending Order)")
unsorted_list_q2 = [5, 2, 9, 1, 7]
length_q2 = len(unsorted_list_q2)
for position_q2 in range(length_q2 - 1):
    min_index_q2 = position_q2
    for i_q2 in range(position_q2 + 1, length_q2):
        if unsorted_list_q2[i_q2] < unsorted_list_q2[min_index_q2]:
            min_index_q2 = i_q2
    if min_index_q2 != position_q2:
        temp_q2 = unsorted_list_q2[position_q2]
        unsorted_list_q2[position_q2] = unsorted_list_q2[min_index_q2]
        unsorted_list_q2[min_index_q2] = temp_q2
print("Sorted List:", unsorted_list_q2)

#Question 3
print("\n#Question 3 - Insertion Sort (Ascending)")
lst3  = [5, 2, 9, 1, 7]
for idx3 in range(1, len(lst3)):
    val3 = lst3[idx3]
    pos3 = idx3 - 1
    while pos3 >= 0 and lst3[pos3] > val3:
        lst3[pos3 + 1] = lst3[pos3]
        pos3 -= 1
    lst3[pos3 + 1] = val3
print("Sorted List:", lst3)

#Question 4
print("\n#Question 4 – Merge Sort")
def merge4(arr4):
    if len(arr4) <= 1:
        return arr4
    mid4 = len(arr4) // 2
    left4 = merge4(arr4[:mid4])
    right4 = merge4(arr4[mid4:])
    return join4(left4, right4)
def join4(left4, right4):
    res4, i4, j4 = [], 0, 0
    while i4 < len(left4) and j4 < len(right4):
        if left4[i4] < right4[j4]:
             res4.append(left4[i4]); i4 += 1
        else:
            res4.append(right4[j4]); j4 += 1
    res4.extend(left4[i4:]); res4.extend(right4[j4:])
    return res4
lst4 = [5, 2, 9, 1, 7]
print("Sorted:", merge4(lst4))

#Question 5
print("\n#Question 5 – Quick Sort")
def sort5(arr5, low5, high5):
    if low5 < high5:
        p5 = split5(arr5, low5, high5)
        sort5(arr5, low5, p5 - 1)
        sort5(arr5, p5 + 1, high5)
def split5(arr5, low5, high5):
    piv5 = arr5[high5]
    i5   = low5 - 1
    for j5 in range(low5, high5):
        if arr5[j5] <= piv5:
            i5 += 1
            arr5[i5], arr5[j5] = arr5[j5], arr5[i5]
    arr5[i5 + 1], arr5[high5] = arr5[high5], arr5[i5 + 1]
    return i5 + 1
lst5 = [5, 2, 9, 1, 7]
sort5(lst5, 0, len(lst5) - 1)
print("Sorted:", lst5)

#Question 6
print("\n#Question 6 – Heap Sort")
def heapify6(arr6, n6, i6):
    largest6 = i6
    left6 = 2 * i6 + 1
    right6 = 2 * i6 + 2
    if left6 < n6 and arr6[left6] > arr6[largest6]:
        largest6 = left6
    if right6 < n6 and arr6[right6] > arr6[largest6]:
        largest6 = right6
    if largest6 != i6:
        arr6[i6], arr6[largest6] = arr6[largest6], arr6[i6]
        heapify6(arr6, n6, largest6)
def sort6(arr6):
    n6 = len(arr6)
    for i6 in range(n6 // 2 - 1, -1, -1):
        heapify6(arr6, n6, i6)
    for end6 in range(n6 - 1, 0, -1):
        arr6[0], arr6[end6] = arr6[end6], arr6[0]
        heapify6(arr6, end6, 0)
lst6 = [5, 2, 9, 1, 7]
sort6(lst6)
print("Sorted:", lst6)

#Question 7
print("\n#Question 7 – Counting Sort")
def sort7(arr7):
    if not arr7:
        return arr7
    max7 = max(arr7) 
    count7 = [0] * (max7 + 1)
    for val7 in arr7:
        count7[val7] += 1
    i7 = 0
    for num7 in range(len(count7)):
        while count7[num7] > 0:
            arr7[i7] = num7
            i7 += 1
            count7[num7] -= 1
lst7 = [5, 2, 9, 1, 7]
sort7(lst7)
print("Sorted:", lst7)

#Question 8
print("\n#Question 8 – Radix Sort")
def sort8(arr8):
    if not arr8:
        return arr8
    max8 = max(arr8)
    place8 = 1
    while max8 // place8 > 0:
        count_sort8(arr8, place8)
        place8 *= 10
def count_sort8(arr8, place8):
    n8 = len(arr8)
    out8 = [0] * n8
    count8 = [0] * 10
    for i8 in range(n8):
        digit8 = (arr8[i8] // place8) % 10
        count8[digit8] += 1
    for i8 in range(1, 10):
        count8[i8] += count8[i8 - 1]
    for i8 in range(n8 - 1, -1, -1):
        digit8 = (arr8[i8] // place8) % 10
        out8[count8[digit8] - 1] = arr8[i8]
        count8[digit8] -= 1
    for i8 in range(n8):
        arr8[i8] = out8[i8]
lst8 = [170, 45, 75, 90, 802, 24, 2, 66]
sort8(lst8)
print("Sorted:", lst8)

#Question 9
def find9(lst9, tgt9):
     left9  = 0
     right9 = len(lst9) - 1
     while left9 <= right9:
         mid9 = (left9 + right9) // 2
         if lst9[mid9] == tgt9:
             return mid9
         elif lst9[mid9] < tgt9:
             left9 = mid9 + 1
         else:
             right9 = mid9 - 1
     return -1
sorted9 = [1, 2, 5, 7, 9, 12, 18]
print("List :", sorted9)
for t9 in [7, 12, 4]:
    pos9 = find9(sorted9, t9)
    if pos9 != -1:
        print(f"Target {t9} found at index", pos9)
    else:
        print(f"Target {t9} not found")

#Question 10
print("\n#Question 10 – Linear Search")

def find10(lst10, tgt10):
    for i10 in range(len(lst10)):
        if lst10[i10] == tgt10:
            return i10
    return -1

unsorted10 = [45, 12, 9, 2, 18, 1, 7, 5]
targets10 = [9, 7, 30]

print("List:", unsorted10)
for t10 in targets10:
    pos10 = find10(unsorted10, t10)
    if pos10 != -1:
        print(f"Target {t10} found at index", pos10)
    else:
        print(f"Target {t10} not found")

#Question 11
print("\n#Question 11 – Interpolation Search")

def find11(arr11, tgt11):
    left11, right11 = 0, len(arr11) - 1
    while left11 <= right11 and tgt11 >= arr11[left11] and tgt11 <= arr11[right11]:
        if arr11[left11] == arr11[right11]:
            return left11 if arr11[left11] == tgt11 else -1
        pos11 = left11 + (tgt11 - arr11[left11]) * (right11 - left11) // (arr11[right11] - arr11[left11])
        if arr11[pos11] == tgt11:
            return pos11
        if arr11[pos11] < tgt11:
            left11 = pos11 + 1
        else:
            right11 = pos11 - 1
    return -1

sorted11 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
targets11 = [70, 25, 10]

print("List:", sorted11)
for t11 in targets11:
    p11 = find11(sorted11, t11)
    if p11 != -1:
        print(f"Target {t11} found at index", p11)
    else:
        print(f"Target {t11} not found")

#Question 12
print("\n#Question 12 – Exponential Search")
def find12(arr12, tgt12):
    if not arr12:
        return -1
    if arr12[0] == tgt12:
        return 0
    i12 = 1
    while i12 < len(arr12) and arr12[i12] <= tgt12:
        i12 *= 2
    return bin12(arr12, i12 // 2, min(i12, len(arr12) - 1), tgt12)
def bin12(arr12, left12, right12, tgt12):
    while left12 <= right12:
        mid12 = (left12 + right12) // 2
        if arr12[mid12] == tgt12:
            return mid12
        elif arr12[mid12] < tgt12:
            left12 = mid12 + 1
        else:
            right12 = mid12 - 1
    return -1
sorted12 = [2, 4, 6, 8, 10, 14, 18, 22, 26, 30, 34, 38, 42]
targets12 = [22, 5, 2]
print("List:", sorted12)
for t12 in targets12:
    p12 = find12(sorted12, t12)
    if p12 != -1:
        print(f"Target {t12} found at index", p12)
    else:
        print(f"Target {t12} not found")

#Question 13
print("\n#Question 13 – Jump Search")
def find13(arr13, tgt13):
    n13 = len(arr13)
    step13 = int(n13 ** 0.5)
    prev13 = 0
    while prev13 < n13 and arr13[min(step13, n13) - 1] < tgt13:
        prev13 = step13
        step13 += int(n13 ** 0.5)
        if prev13 >= n13:
            return -1
    for i13 in range(prev13, min(step13, n13)):
        if arr13[i13] == tgt13:
            return i13
    return -1
sorted13 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targets13 = [15, 4, 1]
print("List:", sorted13)
for t13 in targets13:
    p13 = find13(sorted13, t13)
    if p13 != -1:
        print(f"Target {t13} found at index", p13)
    else:
        print(f"Target {t13} not found")


#Question 14
print("\n#Question 14 – Breadth-First Search (BFS)")

from collections import deque

def bfs14(graph14, start14):
    visited14 = set()
    queue14 = deque([start14])

    while queue14:
        node14 = queue14.popleft()
        if node14 not in visited14:
            print(node14, end=" ")
            visited14.add(node14)
            queue14.extend(graph14[node14])

graph14 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs14(graph14, 'A')

#Question 15
print("\n#Question 15 – Depth-First Search (DFS)")
def dfs15(graph15, node15, visited15=None):
    if visited15 is None:
        visited15 = set()
    if node15 not in visited15:
        print(node15, end=" ")
        visited15.add(node15)
        for nbr15 in graph15[node15]:
            dfs15(graph15, nbr15, visited15)
graph15 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs15(graph15, 'A')

#Question 16
print("\n#Question 16 – Dijkstra's Algorithm")
import heapq
def dijkstra16(graph16, start16):
    dist16 = {node: float('inf') for node in graph16}
    dist16[start16] = 0
    heap16 = [(0, start16)]
    while heap16:
        cost16, node16 = heapq.heappop(heap16)
        for nbr16, weight16 in graph16[node16]:
            new_cost16 = cost16 + weight16
            if new_cost16 < dist16[nbr16]:
                dist16[nbr16] = new_cost16
                heapq.heappush(heap16, (new_cost16, nbr16))
    return dist16
graph16 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('E', 3)],
    'D': [('F', 1)],
    'E': [('D', 2), ('F', 5)],
    'F': []
}
shortest16 = dijkstra16(graph16, 'A')
for k16 in sorted(shortest16):
    print(f"Shortest distance to {k16} is", shortest16[k16])

#Question 17
print("\n#Question 17 – Dynamic Programming Examples")
def fib17(n17, memo17={}):
    if n17 in memo17:
        return memo17[n17]
    if n17 <= 1:
        return n17
    memo17[n17] = fib17(n17 - 1, memo17) + fib17(n17 - 2, memo17)
    return memo17[n17]
print("Fibonacci(10):", fib17(10))
def knap17(wt17, val17, cap17, n17):
    dp17 = [[0] * (cap17 + 1) for _ in range(n17 + 1)]
    for i17 in range(1, n17 + 1):
        for w17 in range(1, cap17 + 1):
            if wt17[i17 - 1] <= w17:
                dp17[i17][w17] = max(val17[i17 - 1] + dp17[i17 - 1][w17 - wt17[i17 - 1]], dp17[i17 - 1][w17])
            else:
                dp17[i17][w17] = dp17[i17 - 1][w17]
    return dp17[n17][cap17]
weights17 = [1, 3, 4, 5]
values17 = [1, 4, 5, 7]
capacity17 = 7
n_items17 = len(weights17)
print("Max Knapsack Value:", knap17(weights17, values17, capacity17, n_items17))

#Question 18
print("\n#Question 18 – Greedy Algorithm Examples")
def coin18(coins18, amt18):
    coins18.sort(reverse=True)
    used18 = []
    for c18 in coins18:
        while amt18 >= c18:
            amt18 -= c18
            used18.append(c18)
    return used18 if amt18 == 0 else []
coins18 = [1, 2, 5, 10, 20, 50]
amount18 = 93
print("Coins used:", coin18(coins18, amount18))
def acts18(st18, end18):
    paired18 = sorted(zip(st18, end18), key=lambda x: x[1])
    res18 = [paired18[0]]
    last_end18 = paired18[0][1]
    for act18 in paired18[1:]:
        if act18[0] >= last_end18:
            res18.append(act18)
            last_end18 = act18[1]
    return res18
starts18 = [1, 3, 0, 5, 8, 5]
ends18 =   [2, 4, 6, 7, 9, 9]
print("Selected Activities:", acts18(starts18, ends18))

#Question 19
print("\n#Question 19 – Backtracking Examples")
def perm19(arr19, path19=[], used19=None):
    if used19 is None:
        used19 = [False] * len(arr19)
    if len(path19) == len(arr19):
        print("Permutation:", path19)
        return
    for i19 in range(len(arr19)):
        if not used19[i19]:
            used19[i19] = True
            perm19(arr19, path19 + [arr19[i19]], used19)
            used19[i19] = False
perm19([1, 2, 3])
def queens19(n19):
    board19 = [-1] * n19
    def safe19(r19, c19):
        for i19 in range(r19):
            if board19[i19] == c19 or abs(board19[i19] - c19) == abs(i19 - r19):
                return False
        return True
    def solve19(r19):
        if r19 == n19:
            print("Solution:", board19)
            return
        for c19 in range(n19):
            if safe19(r19, c19):
                board19[r19] = c19
                solve19(r19 + 1)
                board19[r19] = -1
    solve19(4)

#Question 20
def merge20(arr20):
    if len(arr20) <= 1:
        return arr20
    mid20 = len(arr20) // 2
    left20 = merge20(arr20[:mid20])
    right20 = merge20(arr20[mid20:])
    return join20(left20, right20)
def join20(left20, right20):
    res20 = []
    i20 = j20 = 0
    while i20 < len(left20) and j20 < len(right20):
        if left20[i20] < right20[j20]:
            res20.append(left20[i20])
            i20 += 1
        else:
            res20.append(right20[j20])
            j20 += 1
    res20.extend(left20[i20:])
    res20.extend(right20[j20:])
    return res20
lst20 = [38, 27, 43, 3, 9, 82, 10]
print("Sorted (Merge Sort):", merge20(lst20))
def bin20(arr20, tgt20, low20, high20):
    if low20 > high20:
        return -1
    mid20 = (low20 + high20) // 2
    if arr20[mid20] == tgt20:
        return mid20
    elif arr20[mid20] > tgt20:
        return bin20(arr20, tgt20, low20, mid20 - 1)
    else:
        return bin20(arr20, tgt20, mid20 + 1, high20)
sorted20 = [3, 9, 10, 27, 38, 43, 82]
for target20 in [10, 38, 1]:
    pos20 = bin20(sorted20, target20, 0, len(sorted20) - 1)
    if pos20 != -1:
        print(f"{target20} found at index", pos20)
    else:
        print(f"{target20} not found")

#Question 21
print("\n#Question 21 – Memoization Techniques")
def fib_slow21(n21):
    if n21 <= 1:
        return n21
    return fib_slow21(n21 - 1) + fib_slow21(n21 - 2)
def fib_fast21(n21, memo21={}):
    if n21 in memo21:
        return memo21[n21]
    if n21 <= 1:
        return n21
    memo21[n21] = fib_fast21(n21 - 1, memo21) + fib_fast21(n21 - 2, memo21)
    return memo21[n21]
print("Fibonacci (Slow) of 10:", fib_slow21(10))
print("Fibonacci (Fast with Memoization) of 35:", fib_fast21(35))
#Question 22
def fact22(n22):
    stack22 = [n22]
    res22 = 1
    while stack22:
        k22 = stack22.pop()
        if k22 > 1:
            res22 *= k22
            stack22.append(k22 - 1)
    return res22
print("Factorial(5):", fact22(5))

#Question 23
import time, tracemalloc
def analyze23(fun23, *args23):
    tracemalloc.start()
    t0_23 = time.perf_counter()
    fun23(*args23)
    t1_23 = time.perf_counter() - t0_23
    mem23 = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(f"Time {fun23.__name__}: {t1_23:.6f}s, Memory: {mem23} bytes")
analyze23(fact22, 100)

#Question 24
import random, time
def bubble24(arr24):
    n24 = len(arr24)
    for p24 in range(n24 - 1):
        for i24 in range(n24 - p24 - 1):
            if arr24[i24] > arr24[i24 + 1]:
                arr24[i24], arr24[i24 + 1] = arr24[i24 + 1], arr24[i24]
    return arr24
def merge24(a24):
    if len(a24) <= 1:
        return a24
    m24 = len(a24) // 2
    l24 = merge24(a24[:m24])
    r24 = merge24(a24[m24:])
    return join24(l24, r24)
def join24(l24, r24):
    o24 = []
    i24 = j24 = 0
    while i24 < len(l24) and j24 < len(r24):
        if l24[i24] < r24[j24]:
            o24.append(l24[i24])
            i24 += 1
        else:
            o24.append(r24[j24])
            j24 += 1
    o24.extend(l24[i24:])
    o24.extend(r24[j24:])
    return o24
def bench24(funcs24, data24):
    for f24 in funcs24:
        arr24 = data24.copy()
        t0_24 = time.perf_counter()
        f24(arr24) if f24 is bubble24 else f24(arr24)
        t1_24 = time.perf_counter() - t0_24
        print(f"{f24.__name__} time: {t1_24:.6f}s")
rand24 = random.sample(range(10000), 2000)
bench24([bubble24, merge24, sorted], rand24)

#Question 25
import time
import os

def show25(arr25, hi25=None, lo25=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i25, v25 in enumerate(arr25):
        bar25 = '#' * v25
        marker25 = '<--' if i25 == lo25 or i25 == hi25 else ''
        print(f"{v25:2} | {bar25} {marker25}")
    time.sleep(0.3)

def visual_bubble25(arr25):
    n25 = len(arr25)
    for p25 in range(n25 - 1):
        for i25 in range(n25 - p25 - 1):
            show25(arr25, i25, i25 + 1)
            if arr25[i25] > arr25[i25 + 1]:
                arr25[i25], arr25[i25 + 1] = arr25[i25 + 1], arr25[i25]
    show25(arr25)

data25 = [5, 3, 8, 1, 6]
visual_bubble25(data25)

#✅ Complex Data Structures
#🎯 Focus: Advanced structuring using lists, dicts, sets, and tuples
#Question 1
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def total_sum1(matrix1):
    total1 = 0
    for row1 in matrix1:
        for num1 in row1:
            total1 += num1
    return total1
def transpose1(matrix1):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    result1 = []
    for c1 in range(cols1):
        new_row1 = []
        for r1 in range(rows1):
            new_row1.append(matrix1[r1][c1])
        result1.append(new_row1)
    return result1
def row_sums1(matrix1):
    result1 = []
    for row1 in matrix1:
        row_sum1 = 0
        for num1 in row1:
            row_sum1 += num1
        result1.append(row_sum1)
    return result1
def column_sums1(matrix1):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    result1 = []
    for c1 in range(cols1):
        col_sum1 = 0
        for r1 in range(rows1):
            col_sum1 += matrix1[r1][c1]
        result1.append(col_sum1)
    return result1
print("Matrix:")
for row1 in matrix1:
    print(row1)
print("Total Sum of All Elements:", total_sum1(matrix1))
print("Transpose of Matrix:")
for row1 in transpose1(matrix1):
    print(row1)
print("Row Sums:", row_sums1(matrix1))
print("Column Sums:", column_sums1(matrix1))

#Question 2
categories2 = {
    "Electronics": {
        "Phones": {
            "Smartphones": {},
            "Landlines": {}
        },
        "Computers": {
            "Laptops": {},
            "Desktops": {}
        }
    },
    "Clothing": {
        "Men": {
            "Shirts": {},
            "Pants": {}
        },
        "Women": {
            "Dresses": {},
            "Tops": {}
        }
    }
}
def show_tree2(data2, level2=0):
    for key2 in data2:
        print("  " * level2 + "- " + key2)
        show_tree2(data2[key2], level2 + 1)
print("Category Tree:")
show_tree2(categories2)

#Question 3
graph3 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def print_graph3(g3):
    for node3 in g3:
        print(f"{node3} --> {', '.join(g3[node3])}")
print("Graph Structure:")
print_graph3(graph3)

#Question 4
class Node4:
    def __init__(self, data4):
        self.data4 = data4
        self.children4 = []

    def add_child4(self, child4):
        self.children4.append(child4)

    def print_tree4(self, level4=0):
        print("  " * level4 + "- " + self.data4)
        for child4 in self.children4:
            child4.print_tree4(level4 + 1)
root4 = Node4("Root")
child1_4 = Node4("Child1")
child2_4 = Node4("Child2")
grand1_4 = Node4("Grandchild1")
grand2_4 = Node4("Grandchild2")
child1_4.add_child4(grand1_4)
child1_4.add_child4(grand2_4)
root4.add_child4(child1_4)
root4.add_child4(child2_4)
root4.print_tree4()

#Question 5
class Stack5:
    def __init__(self):
        self.items5 = []

    def push(self, item5):
        self.items5.append(item5)

    def pop(self):
        if not self.is_empty():
            return self.items5.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items5[-1]
        return None

    def is_empty(self):
        return len(self.items5) == 0

    def size(self):
        return len(self.items5)

s5 = Stack5()
s5.push("A")
s5.push("B")
s5.push("C")
print("Top item:", s5.peek())      
print("Popped item:", s5.pop())    
print("Top after pop:", s5.peek()) 
print("Stack empty?", s5.is_empty())
print("Stack size:", s5.size())

#Question 6
from collections import deque

class Queue6:
    def __init__(self):
        self.q6 = deque()

    def enqueue(self, item6):
        self.q6.append(item6)

    def dequeue(self):
        if not self.is_empty():
            return self.q6.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.q6[0]
        return None

    def is_empty(self):
        return len(self.q6) == 0

    def size(self):
        return len(self.q6)
q6 = Queue6()
q6.enqueue("A")
q6.enqueue("B")
q6.enqueue("C")
print("Front item:", q6.peek())     
print("Removed:", q6.dequeue())   
print("Front after dequeue:", q6.peek()) 
print("Queue empty?", q6.is_empty())
print("Queue size:", q6.size())

#Question 7
import heapq
class PriorityQueue7:
 def __init__(self):
  self.tasks7=[]
 def add_task(self,priority7,task7):
  heapq.heappush(self.tasks7,(priority7,task7))
 def get_next_task(self):
  if not self.is_empty():
   return heapq.heappop(self.tasks7)
  return None
 def is_empty(self):
  return len(self.tasks7)==0
 def peek(self):
  if not self.is_empty():
   return self.tasks7[0]
  return None
 def size(self):
  return len(self.tasks7)
pq7=PriorityQueue7()
pq7.add_task(2,"Wash Dishes")
pq7.add_task(1,"Finish Homework")
pq7.add_task(3,"Play Games")
print("Next task:",pq7.get_next_task())
print("Next task:",pq7.get_next_task())
print("Remaining:",pq7.size())
print("Peek:",pq7.peek())

#Question 8
class Node8:
 def __init__(self,data8):
  self.data8=data8
  self.next8=None
class LinkedList8:
 def __init__(self):
  self.head8=None
 def insert_start(self,val8):
  new8=Node8(val8)
  new8.next8=self.head8
  self.head8=new8
 def insert_end(self,val8):
  new8=Node8(val8)
  if not self.head8:
   self.head8=new8
   return
  temp8=self.head8
  while temp8.next8:
   temp8=temp8.next8
  temp8.next8=new8
 def delete_value(self,val8):
  temp8=self.head8
  if temp8 and temp8.data8==val8:
   self.head8=temp8.next8
   return
  prev8=None
  while temp8 and temp8.data8!=val8:
   prev8=temp8
   temp8=temp8.next8
  if temp8:
   prev8.next8=temp8.next8
 def display(self):
  temp8=self.head8
  while temp8:
   print(temp8.data8,end=" -> ")
   temp8=temp8.next8
  print("None")
ll8=LinkedList8()
ll8.insert_end(10)
ll8.insert_end(20)
ll8.insert_start(5)
ll8.display()
ll8.delete_value(20)
ll8.display()

#Question 9
class Node9:
 def __init__(self,val9):
  self.val9=val9
  self.left9=None
  self.right9=None
def inorder9(root9):
 if root9:
  inorder9(root9.left9)
  print(root9.val9,end=" ")
  inorder9(root9.right9)
def preorder9(root9):
 if root9:
  print(root9.val9,end=" ")
  preorder9(root9.left9)
  preorder9(root9.right9)
def postorder9(root9):
 if root9:
  postorder9(root9.left9)
  postorder9(root9.right9)
  print(root9.val9,end=" ")
root9=Node9(1)
root9.left9=Node9(2)
root9.right9=Node9(3)
root9.left9.left9=Node9(4)
root9.left9.right9=Node9(5)
print("Inorder:")
inorder9(root9)
print("\nPreorder:")
preorder9(root9)
print("\nPostorder:")
postorder9(root9)

#Question 10
class HashMap10:
 def __init__(self,size10=10):
  self.size10=size10
  self.buckets10=[[] for _ in range(size10)]
 def _hash10(self,key10):
  return hash(key10)%self.size10
 def put(self,key10,val10):
  idx10=self._hash10(key10)
  for pair10 in self.buckets10[idx10]:
   if pair10[0]==key10:
    pair10[1]=val10
    return
  self.buckets10[idx10].append([key10,val10])
 def get(self,key10):
  idx10=self._hash10(key10)
  for k10,v10 in self.buckets10[idx10]:
   if k10==key10:
    return v10
  return None
 def remove(self,key10):
  idx10=self._hash10(key10)
  self.buckets10[idx10]=[p10 for p10 in self.buckets10[idx10] if p10[0]!=key10]
 def display(self):
  for i10,b10 in enumerate(self.buckets10):
   print(i10,b10)
hm10=HashMap10()
hm10.put("apple",1)
hm10.put("banana",2)
hm10.put("orange",3)
print("Get apple:",hm10.get("apple"))
hm10.remove("banana")
hm10.display()

#Question 11
class TrieNode11:
 def __init__(self):
  self.children11={}
  self.end11=False
class Trie11:
 def __init__(self):
  self.root11=TrieNode11()
 def insert(self,word11):
  node11=self.root11
  for ch11 in word11:
   if ch11 not in node11.children11:
    node11.children11[ch11]=TrieNode11()
   node11=node11.children11[ch11]
  node11.end11=True
 def search(self,word11):
  node11=self.root11
  for ch11 in word11:
   if ch11 not in node11.children11:
    return False
   node11=node11.children11[ch11]
  return node11.end11
 def startsWith(self,prefix11):
  node11=self.root11
  for ch11 in prefix11:
   if ch11 not in node11.children11:
    return False
   node11=node11.children11[ch11]
  return True
trie11=Trie11()
trie11.insert("apple")
trie11.insert("app")
print(trie11.search("apple"))
print(trie11.search("app"))
print(trie11.search("appl"))
print(trie11.startsWith("ap"))
print(trie11.startsWith("ba"))

#Question 12
import hashlib
class Bloom12:
 def __init__(self,size12=100):
  self.size12=size12
  self.bits12=[0]*size12
 def _hashes12(self,item12):
  h1=int(hashlib.md5(item12.encode()).hexdigest(),16)%self.size12
  h2=int(hashlib.sha1(item12.encode()).hexdigest(),16)%self.size12
  h3=int(hashlib.sha256(item12.encode()).hexdigest(),16)%self.size12
  return [h1,h2,h3]
 def add(self,item12):
  for h12 in self._hashes12(item12):
   self.bits12[h12]=1
 def check(self,item12):
  return all(self.bits12[h12]==1 for h12 in self._hashes12(item12))
 
bf12=Bloom12()
bf12.add("apple")
bf12.add("banana")

print(bf12.check("apple"))
print(bf12.check("banana"))
print(bf12.check("cherry"))

#Question 13
from collections import OrderedDict
class LRU13:
 def __init__(self,cap13):
  self.cap13=cap13
  self.cache13=OrderedDict()
 def get(self,key13):
  if key13 in self.cache13:
   self.cache13.move_to_end(key13)
   return self.cache13[key13]
  return -1
 def put(self,key13,val13):
  if key13 in self.cache13:
   self.cache13.move_to_end(key13)
  self.cache13[key13]=val13
  if len(self.cache13)>self.cap13:
   self.cache13.popitem(last=False)
lru13=LRU13(2)
lru13.put(1,100)
lru13.put(2,200)
print(lru13.get(1))
lru13.put(3,300)
print(lru13.get(2))
print(lru13.get(3))

#Question 14
class Ring14:
 def __init__(self,cap14):
  self.cap14=cap14
  self.buf14=[None]*cap14
  self.head14=0
  self.tail14=0
  self.full14=False
 def append(self,val14):
  self.buf14[self.tail14]=val14
  self.tail14=(self.tail14+1)%self.cap14
  if self.full14:
   self.head14=(self.head14+1)%self.cap14
  if self.tail14==self.head14:
   self.full14=True
 def get(self):
  if not self.full14 and self.head14==self.tail14:
   return []
  res14=[]
  i14=self.head14
  while True:
   res14.append(self.buf14[i14])
   if i14==self.tail14 and not self.full14:
    break
   i14=(i14+1)%self.cap14
   if i14==self.tail14 and self.full14:
    res14.append(self.buf14[i14])
    break
  return res14
rb14=Ring14(3)
rb14.append(1)
rb14.append(2)
rb14.append(3)
print(rb14.get())
rb14.append(4)
print(rb14.get())
rb14.append(5)
print(rb14.get())

#Question 15
class Sparse15:
 def __init__(self,rows15,cols15):
  self.rows15=rows15
  self.cols15=cols15
  self.data15={}
 def set(self,r15,c15,val15):
  if val15!=0:
   self.data15[(r15,c15)]=val15
  elif (r15,c15) in self.data15:
   del self.data15[(r15,c15)]
 def get(self,r15,c15):
  return self.data15.get((r15,c15),0)
 def display(self):
  for r15 in range(self.rows15):
   row15=[]
   for c15 in range(self.cols15):
    row15.append(self.get(r15,c15))
   print(row15)
sp15=Sparse15(3,3)
sp15.set(0,1,5)
sp15.set(1,2,8)
sp15.set(2,0,3)
sp15.display()


#Question 16
class Graph16:
 def __init__(self,vertices16):
  self.v16=vertices16
  self.adj_list16={i:[] for i in range(vertices16)}
  self.adj_matrix16=[[0]*vertices16 for _ in range(vertices16)]
 def add_edge(self,u16,v16):
  self.adj_list16[u16].append(v16)
  self.adj_list16[v16].append(u16)
  self.adj_matrix16[u16][v16]=1
  self.adj_matrix16[v16][u16]=1
 def show(self):
  print("Adjacency List:")
  for k16 in self.adj_list16:
   print(k16,":",self.adj_list16[k16])
  print("Adjacency Matrix:")
  for row16 in self.adj_matrix16:
   print(row16)
g16=Graph16(4)
g16.add_edge(0,1)
g16.add_edge(0,2)
g16.add_edge(1,3)
g16.show()

#Question 17
class DSU17:
 def __init__(self,n17):
  self.parent17=[i for i in range(n17)]
 def find(self,x17):
  if self.parent17[x17]!=x17:
   self.parent17[x17]=self.find(self.parent17[x17])
  return self.parent17[x17]
 def union(self,x17,y17):
  px17=self.find(x17)
  py17=self.find(y17)
  if px17!=py17:
   self.parent17[py17]=px17
 def has_cycle(self,edges17):
  for u17,v17 in edges17:
   if self.find(u17)==self.find(v17):
    return True
   self.union(u17,v17)
  return False
ds17=DSU17(5)
edges17=[(0,1),(1,2),(2,3),(3,4),(4,1)]
print(ds17.has_cycle(edges17))

#Question 18
import random
class Node18:
 def __init__(self,key18,level18):
  self.key18=key18
  self.forward18=[None]*(level18+1)
class SkipList18:
 def __init__(self,max_lvl18,p18):
  self.max_lvl18=max_lvl18
  self.p18=p18
  self.head18=Node18(-1,max_lvl18)
  self.level18=0
 def random_level(self):
  lvl18=0
  while random.random()<self.p18 and lvl18<self.max_lvl18:
   lvl18+=1
  return lvl18
 def insert(self,key18):
  update18=[None]*(self.max_lvl18+1)
  curr18=self.head18
  for i18 in reversed(range(self.level18+1)):
   while curr18.forward18[i18] and curr18.forward18[i18].key18<key18:
    curr18=curr18.forward18[i18]
   update18[i18]=curr18
  curr18=curr18.forward18[0]
  if curr18 is None or curr18.key18!=key18:
   rlevel18=self.random_level()
   if rlevel18>self.level18:
    for i18 in range(self.level18+1,rlevel18+1):
     update18[i18]=self.head18
    self.level18=rlevel18
   new_node18=Node18(key18,rlevel18)
   for i18 in range(rlevel18+1):
    new_node18.forward18[i18]=update18[i18].forward18[i18]
    update18[i18].forward18[i18]=new_node18
 def display(self):
  print("Skip List Levels:")
  for i18 in range(self.level18+1):
   node18=self.head18.forward18[i18]
   print("Level",i18,end=": ")
   while node18:
    print(node18.key18,end=" ")
    node18=node18.forward18[i18]
   print()
sl18=SkipList18(3,0.5)
for val18 in [3,6,7,9,12,19,17,26,21,25]:
 sl18.insert(val18)
sl18.display()

#Question 19
class BTreeNode19:
 def __init__(self,t19,leaf19):
  self.t19=t19
  self.leaf19=leaf19
  self.keys19=[]
  self.child19=[]
 def insert_nonfull(self,k19):
  i19=len(self.keys19)-1
  if self.leaf19:
   self.keys19.append(0)
   while i19>=0 and k19<self.keys19[i19]:
    self.keys19[i19+1]=self.keys19[i19]
    i19-=1
   self.keys19[i19+1]=k19
  else:
   while i19>=0 and k19<self.keys19[i19]:
    i19-=1
   i19+=1
   if len(self.child19[i19].keys19)==2*self.t19-1:
    self.split_child(i19)
    if k19>self.keys19[i19]:
     i19+=1
   self.child19[i19].insert_nonfull(k19)
 def split_child(self,i19):
  t19=self.t19
  y19=self.child19[i19]
  z19=BTreeNode19(t19,y19.leaf19)
  z19.keys19=y19.keys19[t19:]
  y19.keys19=y19.keys19[:t19-1]
  if not y19.leaf19:
   z19.child19=y19.child19[t19:]
   y19.child19=y19.child19[:t19]
  self.child19.insert(i19+1,z19)
  self.keys19.insert(i19,y19.keys19.pop())
class BTree19:
 def __init__(self,t19):
  self.root19=BTreeNode19(t19,True)
  self.t19=t19
 def insert(self,k19):
  root19=self.root19
  if len(root19.keys19)==2*self.t19-1:
   s19=BTreeNode19(self.t19,False)
   s19.child19.insert(0,root19)
   s19.split_child(0)
   i19=0
   if s19.keys19[0]<k19:
    i19+=1
   s19.child19[i19].insert_nonfull(k19)
   self.root19=s19
  else:
   root19.insert_nonfull(k19)
 def traverse(self):
  self._traverse(self.root19)
 def _traverse(self,node19):
  i19=0
  for i19 in range(len(node19.keys19)):
   if not node19.leaf19:
    self._traverse(node19.child19[i19])
   print(node19.keys19[i19],end=" ")
  if not node19.leaf19:
   self._traverse(node19.child19[i19+1])
bt19=BTree19(3)
for val19 in [10,20,5,6,12,30,7,17]:
 bt19.insert(val19)
bt19.traverse()

#Question 20
class Node20:
 def __init__(self,val20):
  self.val20=val20;self.color20='R';self.left20=self.right20=self.par20=None


class RB20:
 def __init__(self):
  self.N20=Node20(0);self.N20.color20='B';self.root20=self.N20
 def _left(self,x20):
  y20=x20.right20;x20.right20=y20.left20
  if y20.left20!=self.N20:y20.left20.par20=x20
  y20.par20=x20.par20
  if x20.par20 is None:self.root20=y20
  elif x20==x20.par20.left20:x20.par20.left20=y20
  else:x20.par20.right20=y20
  y20.left20=x20;x20.par20=y20
 def _right(self,x20):
  y20=x20.left20;x20.left20=y20.right20
  if y20.right20!=self.N20:y20.right20.par20=x20
  y20.par20=x20.par20
  if x20.par20 is None:self.root20=y20
  elif x20==x20.par20.right20:x20.par20.right20=y20
  else:x20.par20.left20=y20
  y20.right20=x20;x20.par20=y20
 def insert(self,val20):
  z20=Node20(val20);z20.left20=z20.right20=self.N20
  p20=None;c20=self.root20

  while c20!=self.N20:
   p20=c20;c20=c20.left20 if val20<c20.val20 else c20.right20
  z20.par20=p20
  if p20 is None:self.root20=z20
  elif val20<p20.val20:p20.left20=z20
  else:p20.right20=z20
  self._fix(z20)



 def _fix(self,k20):
  while k20!=self.root20 and k20.par20.color20=='R':
   if k20.par20==k20.par20.par20.left20:
    u20=k20.par20.par20.right20

    if u20.color20=='R':
     k20.par20.color20=u20.color20='B';k20.par20.par20.color20='R';k20=k20.par20.par20
    else:
     if k20==k20.par20.right20:k20=k20.par20;self._left(k20)
     k20.par20.color20='B';k20.par20.par20.color20='R';self._right(k20.par20.par20)
   else:
    u20=k20.par20.par20.left20
    if u20.color20=='R':
     k20.par20.color20=u20.color20='B';k20.par20.par20.color20='R';k20=k20.par20.par20
    else:
     if k20==k20.par20.left20:k20=k20.par20;self._right(k20)
     k20.par20.color20='B';k20.par20.par20.color20='R';self._left(k20.par20.par20)
  self.root20.color20='B'
 def inorder(self,n20):
  if n20!=self.N20:
   self.inorder(n20.left20);print(f"{n20.val20}({n20.color20})",end=' ');self.inorder(n20.right20)
rb20=RB20()
for v20 in[20,15,25,10,5,1,30]:rb20.insert(v20)
rb20.inorder(rb20.root20)