def torre_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        return [(origen, destino)]
    else:
        movimientos = []

        # Mover n-1 discos de la torre origen a la torre auxiliar usando destino como auxiliar
        movimientos.extend(torre_hanoi(n-1, origen, destino, auxiliar))

        # Mover el disco más grande de origen a destino
        movimientos.append((origen, destino))

        # Mover los n-1 discos restantes de la torre auxiliar a la torre destino usando origen como auxiliar
        movimientos.extend(torre_hanoi(n-1, auxiliar, origen, destino))

        return movimientos

def dibujar_torres(movimientos, n):
    torres = [[], [], []]
    for i in range(n, 0, -1): #LLENO LAS TORRES
        torres[0].append(i)

    for i, (origen, destino) in enumerate(movimientos):
        torres[destino].append(torres[origen].pop())

        print(f"Estado de las torres después del movimiento {i + 1}:")
        for j in range(n-1, -1, -1): #VALOR FINAL
            for k in range(3):
                disco = torres[k][j] if j < len(torres[k]) else 0
                print(f"[{disco}]", end=" ")
            print()
        print()

n = int(input("Ingrese el número de discos: "))
movimientos = torre_hanoi(n, 0, 1, 2)
dibujar_torres(movimientos, n)