def convert_temperature(t, unit):
    if unit == 'C':
        c = t
        f = c * 1.8 + 32
        k = c + 273.15
        return c, f, k # 자동으로 튜플이 됨 
    elif unit == 'F':
        f = t
        c = (f - 32) / 1.8
        k = c + 273.15
    elif unit == 'K':
        k = t
        c = k - 273.15
        f = c * 1.8 + 32
    else:
        c, F, k = -1, -1, -1

    return c,f,k
# 함수 실행
t = 25.5
t_expr = convert_temperature(t, 'C')
print(t_expr)


t = 25.5
t_expr = convert_temperature(t, 'F')
print(t_expr)


t = 25.5
t_expr = convert_temperature(t, 'K')
print(t_expr)


