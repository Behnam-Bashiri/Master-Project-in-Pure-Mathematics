# difine data in problem
import sympy as sp
import math
import numpy as np

u1_1 = sp.Symbol("u1_1")
u1_2 = sp.Symbol("u1_2")
u1_3 = sp.Symbol("u1_3")
u1_4 = sp.Symbol("u1_4")
u1_5 = sp.Symbol("u1_5")
u1_6 = sp.Symbol("u1_6")
u1_7 = sp.Symbol("u1_7")
########################
u2_1 = sp.Symbol("u2_1")
u2_2 = sp.Symbol("u2_2")
u2_3 = sp.Symbol("u2_3")
u2_4 = sp.Symbol("u2_4")
u2_5 = sp.Symbol("u2_5")
u2_6 = sp.Symbol("u2_6")
u2_7 = sp.Symbol("u2_7")
#######################
u3_1 = sp.Symbol("u3_1")
u3_2 = sp.Symbol("u3_2")
u3_3 = sp.Symbol("u3_3")
u3_4 = sp.Symbol("u3_4")
u3_5 = sp.Symbol("u3_5")
u3_6 = sp.Symbol("u3_6")
u3_7 = sp.Symbol("u3_7")
#######################
landa1 = sp.Symbol("landa1")
landa2 = sp.Symbol("landa2")
landa3 = sp.Symbol("landa3")
########################
landa_x = sp.Symbol("x")

data = {
    "alp1": 0.1, "alp2": 0.2, "alp3": 0.3,
    "y1": 0.9, "y2": 0.8, "y3": 0.7,
    "roddown": 0.45, "rodup": 0.8,
    "e": 25,
    "ro1": 0.9, "ro2": 0.9, "ro3": 0.9,
    "pi1": 1,
    "pi2": 0.6, "pi3": 0.4,
    "pi4": 0.3, "pi5": 0.25, "pi6": 0.25, "pi7": 0.1,
    "pi8": 0.05, "pi9": 0.15, "pi10": 0.05, "pi11": 0.15, "pi12": 0.05, "pi13": 0.15, "pi14": 0.025, "pi15": 0.025,
    "tao1": 0,
    "tao2": 0.05, "tao3": 0.05,
    "tao4": 0.1, "tao5": 0.05, "tao6": 0.05, "tao7": 0.05,
    "tao8": 0.05, "tao9": 0.15, "tao10": 0.05, "tao11": 0.15, "tao12": 0.05, "tao13": 0.15, "tao14": 0.25,
    "tao54": 0.25,
    "u1_1": u1_1, "u1_2": u1_2, "u1_3": u1_3, 'u1_4': u1_4, "u1_5": u1_5, "u1_6": u1_6, "u1_7": u1_7,
    "u2_1": u2_1, "u2_2": u2_2, "u2_3": u2_3, "u2_4": u2_4, "u2_5": u2_5, "u2_6": u2_6, "u2_7": u2_7,
    "u3_1": u3_1, "u3_2": u3_2, "u3_3": u3_3, "u3_4": u3_4, "u3_5": u3_5, "u3_6": u3_6, "u3_7": u3_7,
}
# show data for user

# dictionary for res calcuator fuctions
data_res = {}

data_diff = {}


def D(n, j):
    selector = "alp" + "{}".format(j)
    s_alp = data[selector]
    sq1 = s_alp
    sq2 = X(n) * X(n)
    return sq1 * sq2


def D_X(j):
    selector = "alp" + "{}".format(j)
    s_alp = data[selector]
    sq1 = s_alp
    sq2 = landa_x * landa_x
    return sq1 * sq2


def C(n, j):
    if j == 1:
        selector_u1 = "u1_" + "{}".format(n)
        u = data[selector_u1]
        selector = "y" + "{}".format(j)
        s_y = data[selector]
    elif j == 2:
        selector_u2 = "u2_" + "{}".format(n)
        u = data[selector_u2]
        selector = "y" + "{}".format(j)
        s_y = data[selector]
    elif j == 3:
        selector_u3 = "u3_" + "{}".format(n)
        u = data[selector_u3]
        selector = "y" + "{}".format(j)
        s_y = data[selector]
    else:
        return "invalid j !"
    e = data["e"]
    sq1 = s_y / 2
    sq2 = (u - e) ** 2
    return sq1 * sq2


def sum_U(n):
    find_last_node = math.floor(n / 2)
    selector_u1 = "u1_" + "{}".format(find_last_node)
    selector_u2 = "u2_" + "{}".format(find_last_node)
    selector_u3 = "u3_" + "{}".format(find_last_node)
    return data[selector_u1] + data[selector_u2] + data[selector_u3]


def X(n):
    param = float()
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            param = 0.45
        elif n % 2 == 1:
            param = 0.8
        res = (1 - param) * (X(math.floor(n / 2))) + sum_U(n)
        return res


def small_phi(n, j):
    res1 = C(n, j)
    res2 = D(n, j)
    return res1 + res2


def small_phi_X(n, j):
    res1 = C(n, j)
    res2 = D_X(j)
    return res1 + res2


def big_phi(n, j):
    res1 = D(n, j)
    return res1


def big_phi_X(n, j):
    res1 = D_X(j)
    return res1


def v(n, j):
    if n < 8:
        TWOnP1 = 2 * n + 1
        TWOn = 2 * n
        selector_pi = "pi" + "{}".format(n)
        s_pi = data[selector_pi]
        ##########
        selector_pi_TWOnP1 = "pi" + "{}".format(TWOnP1)
        s_pi_TWOnP1 = data[selector_pi_TWOnP1]
        ##########
        selector_pi_TWOn = "pi" + "{}".format(TWOn)
        s_pi_TWOn = data[selector_pi_TWOn]
        ##########
        selector_landa_TWOn = "landa" + "{}".format(TWOn)
        s_lanada_TWOn = data_res[selector_landa_TWOn]
        #########
        selector_landa_TWOnP1 = "landa" + "{}".format(TWOnP1)
        s_lanada_TWOnP1 = data_res[selector_landa_TWOnP1]
        #########
        sq1 = ((s_pi_TWOn / s_pi) * s_lanada_TWOn * X(n))
        sq2 = ((s_pi_TWOnP1 / s_pi) * s_lanada_TWOnP1 * X(n))
        selector_ro = "ro" + "{}".format(j)
        res_ro = data[selector_ro]
        return res_ro * (sq1 + sq2)

    else:
        return 0


def v_X(n, j):
    TWOnP1 = 2 * n + 1
    TWOn = 2 * n
    selector_pi = "pi" + "{}".format(n)
    s_pi = data[selector_pi]
    ##########
    selector_pi_TWOnP1 = "pi" + "{}".format(TWOnP1)
    s_pi_TWOnP1 = data[selector_pi_TWOnP1]
    ##########
    selector_pi_TWOn = "pi" + "{}".format(TWOn)
    s_pi_TWOn = data[selector_pi_TWOn]
    ##########
    selector_landa_TWOn = "landa" + "{}".format(TWOn)
    s_lanada_TWOn = data_res[selector_landa_TWOn]
    #########
    selector_landa_TWOnP1 = "landa" + "{}".format(TWOnP1)
    s_lanada_TWOnP1 = data_res[selector_landa_TWOnP1]
    #########
    sq1 = ((s_pi_TWOn / s_pi) * s_lanada_TWOn * landa_x)
    sq2 = ((s_pi_TWOnP1 / s_pi) * s_lanada_TWOnP1 * landa_x)
    selector_ro = "ro" + "{}".format(j)
    res_ro = data[selector_ro]
    return res_ro * (sq1 + sq2)


def find_landa_for_last_node(n, j):
    selector = "alp" + "{}".format(j)
    s_alp = data[selector]
    str_gnr = "landa{}".format(n)
    data_res[str_gnr] = s_alp * 2 * X(n)


def find_landa_for_middle_node(n):
    str_gnr = "landa{}".format(n)
    return data_res[str_gnr]


def Hemiltoni(n, j):
    if 7 < n:
        gnr_str = "Hamiltoni{0}_{1}".format(j, n)
        res_hamiltoni_last_node = big_phi(n, j)
        data_res[str(gnr_str)] = res_hamiltoni_last_node
        find_landa_for_last_node(n, j)
    elif 1 < n < 8:
        selector_pi = "pi" + "{}".format(n)
        s_pi = data[selector_pi]
        selector_tao = "tao" + "{}".format(n)
        s_tao = data[selector_tao]
        sq1 = (s_pi - s_tao) / s_pi
        sq2 = small_phi_X(n, j)
        sq3 = (s_tao / s_pi)
        sq4 = big_phi_X(n, j)
        sq5 = v_X(n, j)
        result = (sq1 * sq2) + (sq3 * sq4) + sq5
        # change landa_x to X(n)
        res_landa_find = sp.diff(result, landa_x)
        result = result.subs({landa_x: X(n)})
        res_landa_find = res_landa_find.subs(landa_x, X(n))
        str_gnr = "landa{0}".format(n)
        data_res[str_gnr] = res_landa_find
        str_gnr = "Hamiltoni{0}_{1}".format(j, n)
        data_res[str_gnr] = result
    elif n == 1:
        selector_pi = "pi" + "{}".format(n)
        s_pi = data[selector_pi]
        selector_tao = "tao" + "{}".format(n)
        s_tao = data[selector_tao]
        sq1 = (s_pi - s_tao) / s_pi
        sq2 = small_phi_X(n, j)
        sq3 = (s_tao / s_pi)
        sq4 = big_phi_X(n, j)
        sq5 = v_X(n, j)
        result = (sq1 * sq2) + (sq3 * sq4) + sq5
        # change landa_x to X(n)
        result = result.subs({landa_x: X(n)})
        str_gnr = "Hamiltoni{0}_{1}".format(j, n)
        data_res[str_gnr] = result


def calcuator():
    H1_2 = data_res["Hamiltoni1_2"]
    H2_2 = data_res["Hamiltoni2_2"]
    H3_2 = data_res["Hamiltoni3_2"]
    H1_3 = data_res["Hamiltoni1_3"]
    H2_3 = data_res["Hamiltoni2_3"]
    H3_3 = data_res["Hamiltoni3_3"]
    U1_2 = data["u1_2"]
    U2_2 = data["u2_2"]
    U3_2 = data["u3_2"]
    U1_3 = data["u1_3"]
    U2_3 = data["u2_3"]
    U3_3 = data["u3_3"]

    res1_2 = sp.diff(H1_2, U1_2)
    res2_2 = sp.diff(H2_2, U2_2)
    res3_2 = sp.diff(H3_2, U3_2)
    res1_3 = sp.diff(H1_3, U1_3)
    res2_3 = sp.diff(H2_3, U2_3)
    res3_3 = sp.diff(H3_3, U3_3)

    print("##############Result################")
    print(res1_2, "\n", res2_2, "\n", res3_2, "\n", res1_3, "\n", res2_3, "\n", res3_3)


for n in range(8, 16):
    for j in range(1, 4):
        Hemiltoni(n, j)

for n in range(4, 8):
    for j in range(1, 4):
        Hemiltoni(n, j)

for n in range(2, 4):
    for j in range(1, 4):
        Hemiltoni(n, j)

for n in range(1, 2):
    for j in range(1, 4):
        Hemiltoni(n, j)

for key, value in data_res.items():
    print(key, ' \n ', value, "\n***********************************************************************************")

calcuator()
