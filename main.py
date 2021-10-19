# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from equations import wylicz_qN, wylicz_aB,wylicz_aT,wylicz_aD,wylicz_aU,wylicz_mT,wylicz_mU

from equations import PomieszczenieInstalacja


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # BUDYNEK
    # AF - powierzchnia płyty grzewczej
    # QN - projektowane straty ciepła pomieszczenia [W]
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

    # WYLICZENIA
    #
    # qN - projektowane straty ciepła pomieszczenia [W/m^2]

    # KROK 1
    # Wyliczeni strumienia ciepła emitowanego z płyty grzewczej
    qN=wylicz_qN(QN,AF)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    print(f"qN={qN}")
    aB=wylicz_aB(R_l_B,lambda_E)
    print(f"aB={aB}")
    aT=wylicz_aT(R_l_B)
    print(f"aT={aT}")

    aD=wylicz_aD(R_l_B,T)
    print(f"aD={aD}")

    aU=wylicz_aU(R_l_B,T)
    print(f"aU={aU}")

    mT=wylicz_mT(T)
    print(f"mT={mT}")

    mU=wylicz_mU(su)
    print(f"mU={mU}")

    inst1=PomieszczenieInstalacja(AF=20,nazwa_pomieszczenia='Kuchnia')

    inst1.podsumowanie()
