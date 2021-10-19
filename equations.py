from scipy import interpolate


def wylicz_qN(QN,AF):
    return QN/AF

def wylicz_aB(R_l_B,lambda_E):

    # Ksiązka tabela 4.1
    x = [0, 0.05, 0.1,0.15] #R_l_B
    y = [2.0, 1.5,1.2,1.0] #lambda_E
    z = [[1.196,0.833,0.640,0.519],
         [1.122,0.797,0.618,0.505],
         [1.058,0.764,0.598,0.491],
         [1.00, 0.734,0.579,0.478]]
    f = interpolate.interp2d(x, y, z, kind='cubic')
    return float(f(R_l_B, lambda_E))

def wylicz_aT(R_l_B):
    # Ksiązka tabela 4.2
    x = [0, 0.05, 0.1,0.15] #R_l_B
    y = [1.23,1.188,1.156,1.134] #lambda_E

    f = interpolate.interp1d(x, y, kind='cubic')
    return f(R_l_B)

def wylicz_aD(R_l_B,T):
    x = [0, 0.05, 0.1,0.15] #R_l_B
    y = [0.05,0.075,0.1,0,15,0.2,0.225,0.3,0.375] #T
    z = [[1.013,1.013,1.012,1.011],
         [1.021,1.019,1.016,1.014],
         [1.029,1.025,1.022,1.018],
         [1.04,1.034,1.029,1.024],
         [1.046,1.04,1.035,1.03],
         [1.049,1.043,1.038,1.033],
         [1.053,1.049,1.044,1.039],
         [1.056,1.051,1.046,1.042]]
    f = interpolate.interp2d(x, y, z, kind='cubic')
    return float(f(R_l_B, T))