from itertools import combinations

n = int(input("This program returns all possible pythagorean triplets upto a number\nEnter the number: "))
nums = [x + 1 for x in range(n)]
possible_combs = combinations(nums, 3)

res_combs = [triplet for triplet in possible_combs if triplet[0]**2 + triplet[1]**2 == triplet[2]**2]
print("The triplets are:", res_combs if len(res_combs)>0 else "None")


