tot_compra =[]
res = input("has hecho alguna compra? S/n ")
if res.lower() == "s":
    while True:
        compra = float(input("Valor del producto: "))
        tot_compra.append(compra)
        print(sum(tot_compra),"€ de compra")

        res = input("has hecho alguna compra más? S/n")
        if res.lower() != "s":
            break
precio_fin = sum(tot_compra)*0.85
print("el precio final es de ", precio_fin, "€")