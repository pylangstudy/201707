import decimal
decimal.getcontext().prec = 36
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
