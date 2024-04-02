num1 = input("첫 번째 수를 입력하세요: ")
binary1 = int(input("첫 번째 수의 진수를 입력하세요: "))
num2 = input("두 번째 수를 입력하세요: ")
binary2 = int(input("두 번째 수의 진수를 입력하세요: "))

def decimal(num, binary):
    if binary == 2:
        return int(num, 2)
    elif binary == 8:
        return int(num, 8)
    elif binary == 10:
        return int(num, 10)
    elif binary == 16:
        return int(num, 16)
    else:
        return None

end1 = decimal(num1, binary1)
end2 = decimal(num2, binary2)
result = end1 + end2

print()
print("(2진수) {} + {} = {}".format(bin(end1), bin(end2), bin(result)))
print("(8진수) {} + {} = {}".format(oct(end1), oct(end2), oct(result)))
print("(10진수) {} + {} = {}".format(end1, end2, result))
print("(16진수) {} + {} = {}".format(hex(end1), hex(end2), hex(result)))