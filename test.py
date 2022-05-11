import random
nums = [i for i in range(10000001)]
goal = random.randint(0, 10000001)
print(goal)
counter = 0

first_idx = 0
last_idx = len(nums) - 1
mid_idx = (first_idx + last_idx) // 2

while first_idx <= last_idx:
    counter += 1
    if goal == nums[mid_idx]:
        print(f"число {goal} нашлось на индексе {mid_idx} за {counter} попыток")
        break
    elif goal > nums[mid_idx]:
        first_idx = mid_idx + 1
        mid_idx = (first_idx + last_idx) // 2
    elif goal < nums[mid_idx]:
        last_idx = mid_idx - 1
        mid_idx = (first_idx + last_idx) // 2
    else:
        print(f"{goal} is not found")
