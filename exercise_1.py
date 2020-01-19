from sys import argv


def calc_pay(hours, payment_for_hour, bonus):
    return int(hours) * int(payment_for_hour) + int(bonus)


n, h, pfh, b = argv
print(n)
print(calc_pay(h, pfh, b))