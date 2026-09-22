nums = [ 2, 7, 11, 15, 2, 8, 3, 21, 6, 18, -50, -2, -19 ]

def two_sums(nums):
    target = 20
    print("We're trying to reach " + str(target) + " using 2 numbers.")
    seen = []
    nums2 = list(set(nums.copy()))
    for position in range(len(nums2)):
        for position1 in range(position +1, len(nums2)):
            total = nums2[position] + nums2[position1]
            if total == target:
                seen.append(nums2[position])
                seen.append(nums2[position1])
                return seen
    return seen

def three_sums(nums):
    target = 6
    print("We're trying to reach " + str(target) + " using 3 numbers.")
    seen = []
    nums2 = list(set(nums.copy()))
    for position in range(len(nums2)):
        for position1 in range(position +1, len(nums2)):
            total = nums2[position] + nums2[position1]
            if total == target:
                seen.append(nums2[position])
                seen.append(nums2[position1])
                return seen
            for position2 in range(position1 +1, len(nums2)):
                total = nums2[position] + nums2[position1] + nums2[position2]
                if total == target:
                    seen.append(nums2[position])
                    seen.append(nums2[position1])
                    seen.append(nums2[position2])
                    return seen
    return seen

def high_sums(nums):
    print("We're trying to reach the highest value we can with 3 numbers.")
    target = 0
    seen = []
    nums2 = list(set(nums.copy()))
    for position in range(len(nums2)):
        for position1 in range(position +1, len(nums2)):
            total = nums2[position] + nums2[position1]
            for position2 in range(position1 +1, len(nums2)):
                total = nums2[position] + nums2[position1] + nums2[position2]
                if total > target:
                    target = total
                    seen.clear()
                    seen.append(nums2[position])
                    seen.append(nums2[position1])
                    seen.append(nums2[position2])
    return seen
print(two_sums(nums))
print(three_sums(nums))
print(high_sums(nums))