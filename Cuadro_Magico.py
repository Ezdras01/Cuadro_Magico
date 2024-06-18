def create_magic_square(n):
    if n % 2 == 0:
        raise ValueError("El orden del cuadrado mágico debe ser impar")

    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2

    while num <= n**2:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square

def print_magic_square(magic_square):
    n = len(magic_square)
    for i in range(n):
        for j in range(n):
            print(f"{magic_square[i][j]:2d}", end=" ")
        print()

# Ejemplo de uso:
n = 5  # Orden del cuadrado mágico (debe ser impar)
magic_square = create_magic_square(n)
print(f"Cuadrado mágico de orden {n}:")
print_magic_square(magic_square)
