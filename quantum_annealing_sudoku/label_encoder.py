"""
Provides encode/decode functionality for easier embedding of the sudoku 
board on a quantum annealer. 

Credits: 
"""
# for exmaple: relabel binary 
# variable x_i_j_k-> x_1_1_1 should equal x_1 x_1_1_2 = x_2 and so forth..
def encode_var_labels(i,j,k,N=9):
    #return (i-1)*N*N+(j-1)*N+k
    counter=0
    for a in range(i):
        for b in range(j):
            for c in range(k):
                pass
    return (a*N*N)+(b*N)+c+1 
    
def decode_var_labels(index, N=9):
    for i in range (N):
        for j in range(N):
            for k in range(N):
                if (i*N*N)+(j*N)+k+1 == index:
                    return[i+1,j+1,k+1]
