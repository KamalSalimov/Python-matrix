from random import randint

def create_matrix(n, m):
    A = []
    for i in range(n):
        A += [[0] * m]
        for j in range(m):
            A[i][j] = randint(10, 50)
    return A


def print_matrix(A):
    for row in A:
        for x in row:
            print(f"{x:4}", end="")
        print()


def saddle_tap(mat):
    setir_sayi = len(mat)
    sutun_sayi = len(mat[0])
    yoxla = 0


    for i in range(setir_sayi):
        en_boyuk = mat[i][0]
        sutun_no = 0
        for j in range(1, sutun_sayi):
            if mat[i][j] > en_boyuk:
                en_boyuk = mat[i][j]
                sutun_no = j

        seddle_var = True
        for k in range(setir_sayi):
            if mat[k][sutun_no] < en_boyuk:
                seddle_var = False
                break

        if seddle_var:
            print(f"Tapıldı: {en_boyuk}, Koordinat: [{i}][{sutun_no}]")
            yoxla = 1

    if yoxla == 0:
        print("heç bir nöqtə tapılmadı.")

setir, sutun = 4, 4
matris = create_matrix(setir, sutun)
print_matrix(matris)
saddle_tap(matris)
