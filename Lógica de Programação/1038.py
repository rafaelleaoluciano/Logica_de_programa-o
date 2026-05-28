Item, Quantidade = map(float, input().split())
if (Item ==  1):
    PreçoTotal = 4.00 * Quantidade
elif (Item == 2):
    PreçoTotal = 4.50 * Quantidade
elif (Item == 3):
    PreçoTotal = 5.00 * Quantidade
elif (Item == 4):
    PreçoTotal = 2.00 * Quantidade
elif (Item == 5):
    PreçoTotal = 1.50 * Quantidade

print(f"Total: R$ {PreçoTotal:.2f}")