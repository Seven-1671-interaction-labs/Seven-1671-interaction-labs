def get__net__pirce(price, tax=0.07, discount=0.05):
final_price = price * (1 + tax - discount)
print(f"For the intinal")