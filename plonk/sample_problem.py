from .copy_constraint import find_permutation
from .constraint import add_mul_constarint, add_add_constarint, add_constant_constraint


def gen_witness(x, y):
    a = [x * x, -1]
    b = [y * y, -1]
    c = [a + b, -1]
    d = [c - a - b, 0]

    return (a, b, c, d)


def is_satisfied_witness(a, b, c):
    assert a[0] * b[0] == c[0]
    assert a[1] * b[1] == c[1]
    assert a[2] + b[2] == c[2]
    assert a[3] * b[3] == c[3]
    assert a[4] * b[4] == c[4]
    assert a[5] + b[5] == c[5]


def gen_constraints():
    # Prove that I know an X such that X*x*x + x +5 == 35

    # init constraints
    Ql = []
    Qr = []
    Qm = []
    Qo = []
    Qc = []

    # set constraints
    Ql, Qr, Qm, Qo, Qc = add_mul_constarint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_mul_constarint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_mul_constarint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_add_constarint(Ql, Qr, Qm, Qo, Qc)
    Ql, Qr, Qm, Qo, Qc = add_constant_constraint(Ql, Qr, Qm, Qo, Qc, 0)
    return (Ql, Qr, Qm, Qo, Qc)


def gen_copy_constraints():
    copy_constraints = [8, 12, 13, 3, 4, 14, 0, 6, 7, 15, 17, 9, 1, 2, 5, 11, 10, 16]

    eval_domain = range(0, len(copy_constraints))

    x_a_prime = find_permutation(copy_constraints[0:6], eval_domain[0:6])
    x_b_prime = find_permutation(copy_constraints[6:12], eval_domain[6:12])
    x_c_prime = find_permutation(copy_constraints[12:18], eval_domain[12:18])

    return (x_a_prime, x_b_prime, x_c_prime, copy_constraints)


def setup():
    Ql, Qr, Qm, Qo, Qc = gen_constraints()
    perm_x, perm_y, perm_z, copy_constraints = gen_copy_constraints()

    return (Ql, Qr, Qm, Qo, Qc, perm_x, perm_y, perm_z, copy_constraints)
