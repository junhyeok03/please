# 쇼핑물 할인율 --> 구매가격
def purchase_price(price, sale_per):
    new_price = price * (100 - sale_per) /100 # 20000 * (100 - 50) /100
    new_price = int(new_price)

    print(f"구매 가격은 {new_price} 입니다.")

    return new_price

p1 = purchase_price(20000, 50)
p2 = purchase_price(20000, 50)
print(p1, p2) # None None
print(p1 + p2)



