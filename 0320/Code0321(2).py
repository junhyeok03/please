num1 = input("첫 번째 수를 입력하세요:")
sel1 = int(input("첫 번째 수의 진수를 입력하세요: "))
num2 = input("두 번째 수를 입력하세요:")
sel2 = int(input("두 번째 수의 진수를 입력하세요:"))

if sel1 == 16:
    ans1 = int(num1,16)
if sel1 == 10:
    ans1 = int(num1,10)
if sel1 == 8:
    ans1 = int(num1,8)
if sel1 == 2:
    ans1 = int(num1,2)



if sel2 == 16:
    ans2 = int(num2, 16)
if sel2 == 10:
    ans2 = int(num2, 10)
if sel2 == 8:
    ans2 = int(num2, 8)
if sel2 == 2:
    ans2 = int(num2, 2)

sum = ans1 + ans2

print("(2진수) {} + {} = {}".format(bin(ans1), bin(ans2), bin(sum)))
print("(8진수) {} + {} = {}".format(oct(ans1), oct(ans2), oct(sum)))
print("(10진수) {} + {} = {}".format(ans1,ans2,sum))
print("(16진수) {} + {} = {}".format(hex(ans1), hex(ans2), hex(sum)))

