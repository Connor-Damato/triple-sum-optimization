"""
Written by: Connor Damato
Date: 10/14/2021
Description: This program is designed to compare the time complexity of three different algorithms that solve the triple sum problem. 
The triple sum problem is defined as finding three values in an array that sum to zero.
"""

import random
import time
import matplotlib.pyplot as plt

num_steps = 0
show_brute_force = False
use_skewed_array = False

def optimized_triple_sum(array):
    global num_steps
    valid_groups = []
    # Remove any useable values from the ends of the array. This is done to reduce the number of iterations
    min_pos = 0
    max_pos = len(array) - 1
    max = array[max_pos] + array[max_pos - 1]
    min = array[0] + array[1]
    num_steps += 5 # Time complexity counter

    if abs(min) > max:
        num_steps += 1 # Time complexity counter
        min_pos = find_min_pos(array, -max)
    elif max > abs(min):
        num_steps += 2 # Time complexity counter
        max_pos = find_min_pos(array, -min)
    else:
        num_steps += 2 # Time complexity counter

    for i in range(min_pos, max_pos + 1):
        sum = array[i]
        num_steps += 1 # Time complexity counter
        for j in range(i + 1, max_pos):
        # if the value is not above the necessary minimum, skip
            sum += array[j]
            num_steps += 2 # Time complexity counter
            if not (-sum > array[max_pos] or -sum < array[min_pos]):
                find_zero = find_value(array[j+1:-1], -sum)
                num_steps += 1 # Time complexity counter
                if find_zero is not None:
                    valid_groups.append([array[i], array[j], array[find_zero + j + 1]])
                    num_steps +=1 # Time complexity counter
            sum -= array[j]
            num_steps += 1 # Time complexity counter
    return valid_groups

def search_skip_sum(array):
    global num_steps
    valid_groups = []
    for i in range(len(array)):
        sum = array[i]
        num_steps += 1 # Time complexity counter
        for j in range(i + 1, len(array)):
            sum += array[j]
            num_steps +=2 # Time complexity counter
            if not(-sum > array[-1] or -sum < array[0]):
                value = find_value(array[j+1:-1], -sum)
                num_steps += 1 # Time complexity counter
                if value is not None:
                    num_steps += 1 # Time complexity counter
                    valid_groups.append([array[i], array[j], array[value + j + 1]])
            sum -= array[j]
            num_steps += 1 # Time complexity counter
    return valid_groups

def default_three_sum(array):
    global num_steps
    valid_groups = []
    for i in range(0, len(array)):
        sum = array[i]
        num_steps += 1 # Time complexity counter
        for j in range(i + 1, len(array)):
        # if the value is not above the necessary minimum, skip
            sum += array[j]
            num_steps += 1 # Time complexity counter
            find_zero = find_value(array[j+1:-1], -sum)
            num_steps += 1 # Time complexity counter
            if find_zero is not None:
                valid_groups.append([array[i], array[j], array[find_zero + j + 1]])
                num_steps +=1 # Time complexity counter
            sum -= array[j]
            num_steps += 1 # Time complexity counter
    return valid_groups

def brute_force_three_sum(array):
    global num_steps
    valid_groups = []
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                num_steps += 1 # Time complexity counter
                if array[i] + array[j] + array[k] == 0:
                    num_steps += 1 # Time complexity counter
                    valid_groups.append([array[i], array[j], array[k]])
    return valid_groups

# Logarithmic search for position equal to or greater than the necessary minimum
def find_min_pos(array, min):
    global num_steps
    low = 0
    high = len(array) - 1
    num_steps += 2 # Time complexity counter
    while low < high:
        mid = (low + high) // 2
        num_steps += 1 # Time complexity counter
        if array[mid] < min:
            low = mid + 1
            num_steps += 2 # Time complexity counter
        elif array[mid] > min:
            high = mid
            num_steps += 3 # Time complexity counter
        else:
            num_steps += 2
            return mid
    return low


def find_value(array, value):
    global num_steps
    low = 0
    high = len(array) - 1
    num_steps += 2 # Time complexity counter
    while low < high:
        mid = (low + high) // 2
        num_steps += 1 # Time complexity counter
        if array[mid] < value:
            low = mid + 1
            num_steps += 2 # Time complexity counter
        elif array[mid] > value:
            high = mid
            num_steps += 3 # Time complexity counter
        else:
            num_steps += 2 # Time complexity counter
            return mid
    return None


def main():
    global num_steps, show_brute_force, use_skewed_array
    num_iterations = 10
    array = []
    optimized_triple_sum_time = 0
    search_skip_time = 0
    default_three_sum_time = 0
    if show_brute_force:
        brute_force_time = 0

    total_optimized_steps = 0
    total_search_skip_steps = 0
    total_default_steps = 0
    if show_brute_force:
        total_brute_force_steps = 0

    x = []
    times_y = [[],[],[],[]]
    steps_y = [[],[],[],[]]

    
    for j in range (10,200):
        array_size = j
        print("Starting Array Size: ", array_size)
        for i in range(1, num_iterations):
            # make random array of 50 integers
            if use_skewed_array:
                array = [random.randint(-100, 300) for k in range(j)]
            else:
                array = [random.randint(-200, 200) for k in range(j)]

            start = time.time()
            num_steps = 0
            solution1 = optimized_triple_sum(sorted(array))
            end = time.time()
            optimized_triple_sum_time += end-start
            total_optimized_steps += num_steps
            # print("\nOptimized Triple Sum: ", num_steps, "\nTime: ", end-start)
            # print("Solution: ", solution1)

            start = time.time()
            num_steps = 0
            solution2 = search_skip_sum(sorted(array))
            end = time.time()
            search_skip_time += end-start
            total_search_skip_steps += num_steps
            # print("\nSearch Skip Sum: ", num_steps, "\nTime: ", end-start)
            # print("Solution: ", solution2)

            start = time.time()
            num_steps = 0
            solution3 = default_three_sum(sorted(array))
            end = time.time()
            default_three_sum_time += end-start
            total_default_steps += num_steps
            # print("\nDefault Triple Sum: ", num_steps, "\nTime: ", end-start)
            # print("Solution: ", solution3)

            if show_brute_force:
                start = time.time()
                num_steps = 0
                solution4 = brute_force_three_sum(array)
                end = time.time()
                brute_force_time += end - start
                total_brute_force_steps += num_steps

            if solution1 != solution3 or solution2 != solution3 or (show_brute_force and solution3 != solution4):
                # throw error
                print("Error: Solutions do not match")

        print("\nOptimized Triple Sum Average Time: ", optimized_triple_sum_time/num_iterations)
        print("Search Skip Sum Average Time: ", search_skip_time/num_iterations)
        print("Default Triple Sum Average Time: ", default_three_sum_time/num_iterations)
        if show_brute_force:
            print("Default Brute Force Sum Average Time: ", brute_force_time/num_iterations)
        times_y[0].append(optimized_triple_sum_time/num_iterations)
        times_y[1].append(search_skip_time/num_iterations)
        times_y[2].append(default_three_sum_time/num_iterations)
        if show_brute_force:
            times_y[3].append(brute_force_time/num_iterations)

        print("\nOptimized Triple Sum Average Steps: ", total_optimized_steps/num_iterations)
        print("Search Skip Sum Average Steps: ", total_search_skip_steps/num_iterations)
        print("Default Triple Sum Average Steps: ", total_default_steps/num_iterations)
        if show_brute_force:
            print("Brute Force Triple Sum Average Steps: ", total_brute_force_steps/num_iterations)
        steps_y[0].append(total_optimized_steps/num_iterations)
        steps_y[1].append(total_search_skip_steps/num_iterations)
        steps_y[2].append(total_default_steps/num_iterations)
        if show_brute_force:
            steps_y[3].append(total_brute_force_steps/num_iterations)

        total_optimized_steps = 0
        total_search_skip_steps = 0
        total_default_steps = 0
        if show_brute_force:
            total_brute_force_steps = 0

        optimized_triple_sum_time = 0
        search_skip_time = 0
        default_three_sum_time = 0
        if show_brute_force:
            brute_force_time = 0

        x.append(array_size)

    # Plotting
    plt.plot(x, times_y[0], label = "Optimized Triple Sum")
    plt.plot(x, times_y[1], label = "Search Skip Sum")
    plt.plot(x, times_y[2], label = "Default Triple Sum")
    if show_brute_force:
        plt.plot(x, times_y[3], label = "Brute Force Triple Sum")
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Triple Sum Algorithms Time Complexity')
    plt.legend()
    plt.show()

    plt.plot(x, steps_y[0], label = "Optimized Triple Sum")
    plt.plot(x, steps_y[1], label = "Search Skip Sum")
    plt.plot(x, steps_y[2], label = "Default Triple Sum")
    if show_brute_force:
        plt.plot(x, steps_y[3], label = "Brute Force Triple Sum")
    plt.xlabel('Array Size')
    plt.ylabel('Steps')
    plt.title('Triple Sum Algorithms Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()