'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    int_list = []
    for i in range(len(nums) - k + 1):
        tmp_max = -999
        for j in range(i, i + k):
            if nums[j] > tmp_max:
                tmp_max = nums[j]
        int_list.append(tmp_max)
    return int_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
