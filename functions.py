import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def make_matrix(N):
    steps = N**2

    A = np.zeros((steps,steps))
    I = np.zeros(steps)

    Arows = []
    Acols = []
    Adata = []

    for k in range(N):
        for i in range(N):
            # bottom edge
            Adiag = N*k+i
            if k == 0: # row number
                if i == 0:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(1)

                    Arows.append(Adiag)
                    Acols.append(Adiag+N)
                    Adata.append(-1)
                elif i == N - 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(1)

                    Arows.append(Adiag)
                    Acols.append(Adiag+N)
                    Adata.append(-1)    
                elif i % 2 == 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag + 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1)
                elif i % 2 == 0: 
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag + 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1) 
            # top edge
            elif k == N - 1:
                if i % 2 == 0:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag + 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1) 
                elif i % 2 == 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag - 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)
            # odd row number
            elif k % 2 == 1:
                if i % 2 == 0:             
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(3)

                    Arows.append(Adiag)
                    Acols.append(Adiag + 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1)               

                elif i % 2 == 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(3)

                    Arows.append(Adiag)
                    Acols.append(Adiag - 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1) 
            # even row number
            elif k % 2 == 0:
                if i == 0:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag - 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)
                elif i == N - 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(2)

                    Arows.append(Adiag)
                    Acols.append(Adiag - 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)
                elif i % 2 == 1:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(3)

                    Arows.append(Adiag)
                    Acols.append(Adiag + 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1) 
                elif i % 2 == 0:
                    Arows.append(Adiag)
                    Acols.append(Adiag)
                    Adata.append(3)

                    Arows.append(Adiag)
                    Acols.append(Adiag - 1)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag - N)
                    Adata.append(-1)

                    Arows.append(Adiag)
                    Acols.append(Adiag + N)
                    Adata.append(-1)
    Adata_coo=coo_matrix((Adata, (Arows, Acols)), shape=(steps, steps))
    Adata_csr = Adata_coo.tocsr() 
    return Adata_csr
        
