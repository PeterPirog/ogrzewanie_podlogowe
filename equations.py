from scipy import interpolate
import numpy as np


def wylicz_qN(QN, AF):
    # Książka wzór 4.76
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
    if su >= 0.01:
        return 100 * (0.045 - su)
    else:
        print("Nieprawidłowy wymiar su - grubość warstwy jastrychu nad rurami")
        return None


def wylicz_mD(D):
    if (D >= 0.008) and (D <= 0.03):
        return 250 * (D - 0.020)
    else:
        print("Nieprawidłowy wymiar D - zewnętrzna średnica rury")
        return None


def wylicz_delta_theta_H(theta_v, theta_r, theta_i):
    return (theta_v - theta_r) / np.log((theta_v - theta_i) / (theta_r - theta_i))


# Wyliczenia dla
def wylicz_BG(su, lambda_E, T):
    su_lambda_E = su / lambda_E

    # su_lambda_E = 0.4
    # print(f'T={T}')
    # print(f'su_lambda_E={su_lambda_E}')

    if su_lambda_E <= 0.0792:  # Tabela 4.14
        x = [0.01, 0.0208, 0.0292, 0.0375, 0.0458, 0.0542, 0.0625, 0.0708, 0.0792]  # su_lambda_E
        y = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]  # T
        z = [[85.0, 91.5, 96.8, 100, 100, 100, 100, 100, 100],
             [75.3, 83.5, 89.9, 96.3, 99.5, 100, 100, 100, 100],
             [66.0, 75.4, 82.9, 89.3, 95.5, 98.8, 100, 100, 100],
             [51.0, 61.1, 69.2, 76.3, 82.7, 87.5, 91.8, 95.1, 97.8],
             [38.5, 48.2, 56.2, 63.1, 69.1, 74.5, 81.3, 86.4, 90.0],
             [33.0, 42.5, 49.5, 56.5, 62.0, 67.5, 75.3, 81.6, 86.1],
             [20.5, 26.8, 31.6, 36.4, 41.5, 47.5, 57.5, 65.3, 72.4],
             [11.5, 13.7, 15.5, 18.2, 21.5, 27.5, 40.0, 49.1, 58.3]
             ]
        f = interpolate.interp2d(x, y, z, kind='cubic')
        return float(f(su_lambda_E, T))
    elif (su_lambda_E > 0.0792) and (su_lambda_E <= 0.75):  # Tabela 4.15
        x = [0.173, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]  # su_lambda_E
        y = [27.5, 40.0, 57.5, 69.5, 78.2, 84.4, 88.3, 91.6, 94.0, 96.3, 98.6, 99.8]  # BG

        f = interpolate.interp1d(x, y, kind='cubic')
        return f(su_lambda_E)
    else:
        return 100


class Rura:
    def __init__(self, D=0.0175, d_r=0.002, T=0.2, lambda_R=None, B=None):
        self.D = D  # średnica zewnętrzna rury
        self.d_r = d_r  # grubość rury
        self.T = T  # odległość między rurami
        self.dj = self.D - 2 * self.d_r  # średnica wewnętrzna rury

        self.lambda_R0 = 0.35  # normatywny współczynnik przewodzenia ciepła rury
        if lambda_R is None:
            self.lambda_R = lambda_R  # współczynnik przewodzenia ciepła rury
        else:
            self.lambda_R = self.lambda_R0

        self.B0 = 6.7  # nominalny współczynnik zależny od systemu ukłądania rur
        if B is None:
            self.B = self.B0  # współczynnik zależny od systemu ukłądania rur
        else:
            self.B = B


class PomieszczenieInstalacja():
    def __init__(self, AF, nazwa_pomieszczenia='Pomieszczenie1',
                 QN=None, d=0.01, R_l_B=0.15,  # BUDYNEK
                 lambda_E=1.2, su=0.048,  # JASTRYCH
                 D=0.0175, d_r=0.002, T=0.2, lambda_R=None, B=None,  # RURY
                 theta_i=20.0, theta_Fmax=29.0, theta_v=50.0, theta_r=40.0, sigma=10.0):  # TEMPERATURY

        # BUDYNEK
        self.nazwa = nazwa_pomieszczenia
        self.AF = AF  # powierzchnia płyty grzewczej
        if QN is None:
            print('Nie wprowadzono projektowanych strat ciepła w pomieszczeniu')
        self.QN = QN  # projektowane straty ciepła pomieszczenia
        # PODłOGA
        self.d = d  # grubość wykładziny podłogowej
        self.R_l_B = R_l_B  # opór cieplny wykładziny:
        # JASTRYCH
        self.lambda_E = lambda_E  # współczynnik przewodzenia ciepła jastrychu
        self.su = su  # grubość warstwy jastrychu nad rurami
        if (self.su / self.lambda_E <= 0.01) or (self.su / self.lambda_E >= 0.0792):
            print('Nieprawidłowa proporcja wartości: 0.01<= su/lambda_E<=0.0792')

        # RURY
        self.rura = Rura(D=D, d_r=d_r, T=T, lambda_R=lambda_R, B=B)
        # self.D = D  # średnica zewnętrzna rury
        # self.d_r = d_r  # grubość rury
        # self.T = T  # odległość między rurami
        # self.dj = self.D - 2 * self.d_r  # średnica wewnętrzna rury

        # TEMPERATURY
        self.theta_i = theta_i  # projektowa temperatura wewnętrzna
        self.theta_Fmax = theta_Fmax  # maksymalna temperatura powierzchni płyty grzewczej - wpływa też typ paneli
        self.theta_v = theta_v  # temperatura zasilania czynnika grzewczego
        self.theta_r = theta_r  # temperatura schłodzenia czynnika grzewczego
        self.sigma = sigma  # stopień schłodzenia czynnika grzewczego

        self.aktualizuj()

    def aktualizuj(self):
        # aB - współczynnik zależny od wykładziny podłogowej
        self.aB = wylicz_aB(self.R_l_B, self.lambda_E)

        # aT - współczynnik zależny od oporu cieplnego wykładziny podłogowej
        self.aT = wylicz_aT(self.R_l_B)

        # aD - współczynnik zależny od odległości pomiędzy rurami
        self.aD = wylicz_aD(self.R_l_B, self.rura.T)

        # aU - kolejny współczynnik zależny od odległości pomiędzy rurami
        self.aU = wylicz_aU(self.R_l_B, self.rura.T)

        self.mT = wylicz_mT(self.rura.T)
        self.mU = wylicz_mU(self.su)
        self.mD = wylicz_mD(self.rura.D)
        """
        print(f'D={self.D}')
        print(f'aB={self.aB}')
        print(f'aT={self.aT}')
        print(f'mT={self.mT}')
        print(f'aD={self.aD}')
        print(f'mD={self.mD}')
        print(f'aU={self.aU}')
        print(f'mU={self.mU}')
        """

        # KH - równoważny współczynnik przenikania ciepła
        self.KH = self.rura.B * self.aB * pow(self.aT, self.mT) * pow(self.aD, self.mD) * pow(self.aU, self.mU)

        # delta_theta_H - średnia logarytmiczna różnica temperatur czynnika grzewczego
        self.delta_theta_H = wylicz_delta_theta_H(self.theta_v, self.theta_r, self.theta_i)

        # q - gęstrość strumienia ciepła emitowana z powierzchni płyty grzewczej
        self.q = self.KH * self.delta_theta_H

        # Wyliczenia granicznej gęstości strumienia ciepła
        self.BG = wylicz_BG(self.su, self.lambda_E, self.rura.T)

    def podsumowanie(self):
        print('Podsumowanie')
        print(' \t Wprowadzone dane:')
        print(f'Nazwa pomieszczenia:{self.nazwa}')
        print(' \t DANE BUDYNKU')
        print(f'AF - powierzchnia płyty grzewczej: {self.AF} [m^2]')
        print(f'QN - projektowane straty ciepła pomieszczenia: {self.QN} [W]')
        print(' \n\t PODLOGA')
        print(f'd - grubość wykładziny podłogowej: {self.d} [m]')
        print(f'R_l_B - opór cieplny wykładziny: {self.R_l_B} [m^2*K/W]')
        print(' \n\t JASTRYCH')
        print(f'lambda_E- współczynnik przewodzenia ciepła jastrychu: {self.lambda_E} [W/(m*K)]')
        print(f'su - grubość warstwy jastrychu nad rurami: {self.su} [m]')
        print('\n\t RURY')
        print(f'D - średnica zewnętrzna rury: {self.rura.D} [m]')
        print(f'dj - średnica wewnętrzna rury: {self.rura.dj} [m]')
        print(f'd_r - grubość rury: {self.rura.d_r} [m]')
        print(f'T - odległość między rurami: {self.rura.T} [m]')
        print(f'lambda_R - współczynnik przewodzenia ciepła rury: {self.rura.lambda_R} [W/(m^2*K)]')
        print(f'B - współczynnik zależny od sposobu układania rur: {self.rura.B} [W/(m^2*K)]')

        print(' \n\t TEMPERATURA')
        print(f'theta_i - projektowa temperatura wewnętrzna: {self.theta_i} [C]')
        print(f'theta_Fmax - maksymalna temperatura powierzchni płyty grzewczej: {self.theta_Fmax} [C]')
        print(f'theta_v - temperatura zasilania czynnika grzewczego: {self.theta_v} [C]')
        print(f'theta_r - temperatura schłodzenia czynnika grzewczego: {self.theta_r} [C]')
        print(f'sigma - stopień schłodzenia czynnika grzewczego: {self.sigma} [W/(m^2*K)]')

        # WARTOŚCI WYLICZONE
        print(' \n WYLICZENIA')
        print(' \n\t WSPÓLCZYNNIKI')
        print(f'B - współczynnik zależny od systemu ukłądania rur: {self.rura.B} [C]')
        print(f'KH - równoważny współczynnik przenikania ciepła: {self.KH} [W/(m^2*K)]')
        print(f'delta_theta_H - średnia logarytmiczna różnica temperatur czynnika grzewczego: {self.delta_theta_H} [C]')
        print(f'q - gęstrość strumienia ciepła emitowana z powierzchni płyty grzewczej: {self.q} [C]\n')
        print(f'BG - współczynnik do wyliczenia granicznego strumienia ciepła: {self.BG} [-]')
