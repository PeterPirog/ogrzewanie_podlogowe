from scipy import interpolate


def wylicz_qN(QN, AF):
    return QN / AF


def wylicz_aB(R_l_B, lambda_E):
    # Ksiązka tabela 4.1
    x = [0, 0.05, 0.1, 0.15]  # R_l_B
    y = [2.0, 1.5, 1.2, 1.0]  # lambda_E
    z = [[1.196, 0.833, 0.640, 0.519],
         [1.122, 0.797, 0.618, 0.505],
         [1.058, 0.764, 0.598, 0.491],
         [1.00, 0.734, 0.579, 0.478]]
    f = interpolate.interp2d(x, y, z, kind='cubic')
    return float(f(R_l_B, lambda_E))


def wylicz_aT(R_l_B):
    # Ksiązka tabela 4.2
    x = [0, 0.05, 0.1, 0.15]  # R_l_B
    y = [1.23, 1.188, 1.156, 1.134]  # lambda_E

    f = interpolate.interp1d(x, y, kind='cubic')
    return f(R_l_B)


def wylicz_aD(R_l_B, T):
    x = [0, 0.05, 0.1, 0.15]  # R_l_B
    y = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]  # T
    z = [[1.013, 1.013, 1.012, 1.011],
         [1.021, 1.019, 1.016, 1.014],
         [1.029, 1.025, 1.022, 1.018],
         [1.040, 1.034, 1.029, 1.024],
         [1.046, 1.040, 1.035, 1.030],
         [1.049, 1.043, 1.038, 1.033],
         [1.053, 1.049, 1.044, 1.039],
         [1.056, 1.051, 1.046, 1.042]]
    f = interpolate.interp2d(x, y, z, kind='cubic')
    return float(f(R_l_B, T))


def wylicz_aU(R_l_B, T):
    x = [0, 0.05, 0.1, 0.15]  # R_l_B
    y = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]  # T
    z = [[1.069, 1.056, 1.043, 1.037],
         [1.066, 1.053, 1.041, 1.035],
         [1.063, 1.05, 1.039, 1.0335],
         [1.057, 1.046, 1.035, 1.0305],
         [1.051, 1.041, 1.0315, 1.0275],
         [1.048, 1.038, 1.0295, 1.026],
         [1.0395, 1.031, 1.024, 1.021],
         [1.03, 1.0221, 1.0181, 1.015]
         ]
    f = interpolate.interp2d(x, y, z, kind='cubic')
    return float(f(R_l_B, T))


def wylicz_mT(T):
    if (T >= 0.05) and (T <= 0.375):
        return 1 - T / 0.075
    else:
        print("Nieprawidłowy wymiar T - odległość pomiędzy rurami")
        return None

def wylicz_mU(su):
    if su>=0.01:
        return 100*(0.045-su)
    else:
        print("Nieprawidłowy wymiar su - grubość warstwy jastrychu nad rurami")
        return None

def wylicz_mD(D):
    if (D >= 0.03) and (D <= 0.08):
        return 250*(D-0.020)
    else:
        print("Nieprawidłowy wymiar D - zewnętrzna średnica rury")
        return None


class PomieszczenieInstalacja():
    def __init__(self,AF,nazwa_pomieszczenia='Pomieszczenie1',QN=None):
        self.nazwa=nazwa_pomieszczenia
        self.AF=AF
        if QN is None:
            print('Nie wprowadzono projektowanych strat ciepła w pomieszczeniu')
        self.QN=QN

        self.__aktualizuj__()
    def __aktualizuj__(self):
        pass

    def podsumowanie(self):
        print('Podsumowanie')
        print(' \t Wprowadzone dane:')
        print(f'Nazwa pomieszczenia:{self.nazwa}')
        print(' \t DANE BUDYNKU')
        print(f'AF - powierzchnia płyty grzewczej: {self.AF} [m^2]')
        print(f'QN - projektowane straty ciepła pomieszczenia: {self.QN} [W]')


"""

    #
    # PODLOGA
    # d - grubość podłogi [m]
    # R_l_B - opór cieplny wykładziny [m^2*K/W]
    #
    # JASTRYCH
    # lambda_E- współczynnik przewodzenia ciepła jastrychu [W/(m*K)]
    # su - grubość warstwy jastrychu nad rurami
    #
    # RURY
    # D - średnica zewnętrzna rury
    # su - grubość rury
    # T - odległość między rurami
    #
    # TEMPERATURY
    # theta_i - projektowa temperatura wewnętrzna [C]
    # theta_Fmax - maksymalna temperatura powierzchni płyty grzewczej
    # theta_v - temperatura zasilania czynnika grzewczego
    # theta_i - temperatura schłodzenia czynnika grzewczego
    # sigma - stopień schłodzenia czynnika grzewczego

    #BUDYNEK
    AF =20.0
    QN = 1200
    # PODLOGA
    d = 0.01
    R_l_B = 0.15
    # JASTRYCH
    lambda_E = 1.2
    su = 0.048
    # RURY
    D = 0.017
    T = 0.2
    # TEMPERATURY
    theta_i = 20
    theta_Fmax = 29.0
    theta_v = 50.0
    theta_i = 40.0
    sigma=10.0
"""