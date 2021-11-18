import numpy as np

#  funcao que multiplica a matriz A com a matriz B
def multiplicador_matriz(A, B):
    # obtendo parametros das matrizes
    qntd_linhas_A   = len(A)
    qntd_colunas_A  = len(A[0])
    qntd_linhas_B   = len(B)
    qntd_colunas_B  = len(B[0])

    # verifica se é possivel fazer a multiplicacao
    if qntd_colunas_A == qntd_linhas_B:

        C = np.zeros((qntd_linhas_A,qntd_colunas_B))
        for linha in range(qntd_linhas_A):
            for coluna in range(qntd_colunas_B):
                for k in range(qntd_colunas_A):
                    C[linha][coluna] += A[linha][k] * B[k][coluna]
        
        return C
    else:
        resposta = """Não é possível fazer multiplicação de matriz quando N for 
                        diferente de P na multiplcacao de Amxn * Bpxq."""
        return resposta

############################################################################################################
#  pergunto ao usuario o tamanho das matrizes
qntd_linhas_A   = int(input("\nInsira a quantidade de linhas da matriz A: "))
qntd_colunas_A  = int(input("\nInsira a quantidade de colunas da matriz A: "))
qntd_linhas_B   = int(input("\nInsira a quantidade de linhas da matriz B: "))
qntd_colunas_B  = int(input("\nInsira a quantidade de colunas da matriz B: "))

# crio as matrizes de zeros
A = np.zeros((qntd_linhas_A,qntd_colunas_A))
B = np.zeros((qntd_linhas_B,qntd_colunas_B))
C = np.zeros((qntd_linhas_A,qntd_colunas_B))

# pergunto os elementos da matriz A
for linha in range(qntd_linhas_A):
    for coluna in range(qntd_colunas_A):
        A[linha][coluna] = float(input(f"Digite o elemento A[{linha}][{coluna}]: "))

print()
# pergunto os elementos da matriz B
for linha in range(qntd_linhas_B):
    for coluna in range(qntd_colunas_B):                
        B[linha][coluna] = float(input(f"Digite o elemento B[{linha}][{coluna}]: "))

# realiza o calculo
print(f"\n\nO resultado da função é:\n{multiplicador_matriz(A, B)}")
print(f"\nO gabarito é:\n{A.dot(B)}")


