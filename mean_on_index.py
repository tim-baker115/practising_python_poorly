nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def test(nums, position):
    average = []
    total = 0
    if position == 0:
        print("position is 0")
        average.append(nums[position])
    elif position > 9:
        print(str(sum(nums[position -10:position])))
        total += sum(nums[position -10:position])/position
        average.append(total)
    else:
        total += sum(nums[0:position])/position
        average.append(total)
    print(sum(average))

print(test(nums, 8))