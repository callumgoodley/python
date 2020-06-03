# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


def find_index(six_index, indices_list):
    index = []
    for i in indices_list:
        if i > six_index:
            index.append(i)
    return index[0]


def fetch_numbers(nums):

    nums_list = []
    six_indices = [i for i, x in enumerate(nums) if x == 6]
    seven_indices = [i for i, x in enumerate(nums) if x == 7]

    if 6 in nums:

        for i in range(0, nums.index(6)):
            nums_list.append(nums[i])
        for j in range(find_index(nums.index(6), seven_indices) + 1, len(nums)):
            nums_list.append(nums[j])
    else:
        for n in nums:
            nums_list.append(n)
    return nums_list


def sum67(nums):

    nums_list = fetch_numbers(nums)

    if 6 in nums_list:
        return sum67(nums_list)
    else:
        return sum(nums_list)
