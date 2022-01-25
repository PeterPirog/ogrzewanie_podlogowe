from equations import PomieszczenieInstalacja

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # BUDYNEK
    AF = 20.0  # - powierzchnia płyty grzewczej [m^2]
    QN = 1200  # - projektowe straty ciepła pomieszczenia [W]

    # WYKLADZINA PODLOGOWA
    d = 0.01  # - grubość podłogi [m]
    R_l_B = 0.15  # - opór cieplny wykładziny [m^2*K/W]

    # JASTRYCH
    lambda_E = 1.2 #1.2  # lambda_E- współczynnik przewodzenia ciepła jastrychu [W/(m*K)]
    su = 0.048  # - grubość warstwy jastrychu nad rurami [m]

    # RURY
    D = 0.0175  # - średnica zewnętrzna rury [m]
    SR = 0.002  # - grubość rury [m]
    T = 0.2  # - odległość między rurami [m]

    # TEMPERATURY
    theta_i = 20  # - projektowa temperatura wewnętrzna [C]
    theta_Fmax = 29.0  # - maksymalna temperatura powierzchni płyty grzewczej
    theta_v = 50.0  # - temperatura zasilania czynnika grzewczego
    theta_r = 40.0  # - temperatura schłodzenia czynnika grzewczego
    sigma = 10.0  # sigma - stopień schłodzenia czynnika grzewczego

    inst1 = PomieszczenieInstalacja(AF=AF, nazwa_pomieszczenia='Pomieszczenie1',
                                    QN=QN, d=d, R_l_B=R_l_B,  # BUDYNEK
                                    lambda_E=lambda_E, su=su,  # JASTRYCH
                                    D=D, SR=SR, T=T, lambda_R=None, B=None,  # RURY
                                    theta_i=theta_i, theta_Fmax=theta_Fmax, theta_v=theta_v, theta_r=theta_r,
                                    sigma=sigma)  # Temperatury

    inst1.podsumowanie()
