def avg():
    a = float(input("Enter a dividend"))
    c = float(input("Enter a dividend"))
    assert (c) != 0, "the dividend cannot be zero"
    result = a / c
    return a, c, result

a, c, result = avg()
print(f"{a:0f} / {c:0f}", "-", result)