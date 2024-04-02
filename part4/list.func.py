#list func
# sort()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort()
print(nums)

# sort(reverse=True)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort(reverse=True)
print(nums)


# .reverse()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.reverse()
print(nums)


# .remover(v) value
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.remove(11)
print(nums)


# .index(v)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
idx = nums.index(11)
print(idx)


nums1 = [33, 22, 11, 77]
nums2 = [55, 66, 99, 88]
nums1.extend(nums2)
print(nums1)

nums3 = nums1 + nums2
print(nums3)


# .count(v)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(nums.count(11))
print(nums)

# .pop(i) .pop()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
num = nums.pop(0) 
print(num)

# len()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(len(nums))


# sorted(v), sorted(v, reverse=True)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(sorted(nums))
print(nums)




























