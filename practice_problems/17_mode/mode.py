def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    count_dict = {num: nums.count(num) for num in set(nums)}
    mode_num = 0
    mode_count = 0

    for (k,v) in count_dict.items():
        if v > mode_count:
            mode_num = k
            mode_count = v

    return mode_num
