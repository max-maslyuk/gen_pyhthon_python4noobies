num = int(input())
num1 = (num % 10000) // 100
num2 = (num % 100) // 10
num3 = num % 10
num_max = min(num1, num2, num3)
num_min = max(num1, num2, num3)
srednee = (num1 + num2 + num3) - max(num1, num2, num3) - min(num1, num2, num3)
if srednee == max(num1, num2, num3) - min(num1, num2, num3):
    print("Число интересное")
else:
    print("Число неинтересное")
