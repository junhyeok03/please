# list slice -> Non0destructive
nums = [33,22,11,77,55,66,99,88]

print(nums[2:6])
print(nums[-2:-6])
print(nums[-6:-2])

# 앞(0) 뒷(맨마지막) 생략 

print(nums[:6])
print(nums[2:])

# step
print(nums[2:7])


# adv slice


# 삽입 
user1 = ['Spencer', '200']
user2 = ['Mussg','50']
user1.insert(1,100)
print(user1)
user1.insert(3, 150)



# list와 str의 차이 -sequence

text = 'abcde'
chars = ['a', 'b', 'c', 'd', 'e']

# index 
print(chars[0])
print(text[0])
print(chars[-1])
print(text[-1])


# index - 수정 -> 문자열 불가능 


# 삭제 -del 
#del chars[0]
#del text[0]

# 문자열 -> 리스트
text = 'abcde'
chars = list(text)
print(text, chars)

# 리스트 -> 문자열 






