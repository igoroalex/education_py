def bubble_sort(nums: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


lst = [13, 45, 33, 7, 4, 2, 7, 6, 35, 9, 42]
bubble_sort(lst)
print(lst)
