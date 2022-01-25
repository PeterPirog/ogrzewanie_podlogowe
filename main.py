
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
    # SR - grubość rury
    # T - odległość między rurami
    #
    # TEMPERATURY
    # theta_i - projektowa temperatura wewnętrzna [C]
    # theta_Fmax - maksymalna temperatura powierzchni płyty grzewczej
    # theta_v - temperatura zasilania czynnika grzewczego
    # theta_i - temperatura schłodzenia czynnika grzewczego
    # sigma - stopień schłodzenia czynnika grzewczego

    # BUDYNEK
    AF = 20.0
    QN = 1200
    # WYKLADZINA
    d = 0.01
    R_l_B = 0.15
    # JASTRYCH
    lambda_E = 1.2
    su = 0.048
    # RURY
    D = 0.017
    SR = 0.002
    T = 0.2
    # TEMPERATURY
    theta_i = 20
    theta_Fmax = 29.0
    theta_v = 50.0
    theta_r = 40.0
    sigma = 10.0

    inst1 = PomieszczenieInstalacja(AF=AF, nazwa_pomieszczenia='Pomieszczenie1',
                                    QN=QN, d=d, R_l_B=R_l_B,  # BUDYNEK
                                    lambda_E=lambda_E, su=su,  # JASTRYCH
                                    D=D, SR=0.002, T=T, lambda_R=None, B=None,  # RURY
                                    theta_i=theta_i, theta_Fmax=theta_Fmax, theta_v=theta_v, theta_r=theta_r,
                                    sigma=sigma)  #Temperatury

    inst1.podsumowanie()
