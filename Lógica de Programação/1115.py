while True:
    X, Y = map(int, input().split())
    if X * Y > 0:
        print(f"primeiro" if X > 0 else "terceiro")
    elif X * Y < 0:
        print(f"quarto" if X > 0 else "segundo")
    else:
        break