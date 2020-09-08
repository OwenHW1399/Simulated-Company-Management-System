from organization_hierarchy import Employee, Leader, merge
from typing import List

# ==Task1==#
e3 = Employee(3, 'e3', 'E3', 3999, 27)
L81 = Leader(81, 'l81', 'L81-B', 3399, 58, 'B')
e23 = Employee(23, 'e23', 'E23', 1999, 32)
L58 = Leader(58, 'l58', 'L58-C', 2799, 85, 'C')
e48 = Employee(48, 'e48', 'E48', 2699, 84)
e38 = Employee(38, 'e38', 'E38', 3299, 38)
L81.become_subordinate(e3)
e23.become_subordinate(e3)
L58.become_subordinate(L81)
e48.become_subordinate(L81)
e38.become_subordinate(L81)

L82 = Leader(82, 'l82', 'L82-A', 4567, 80, 'A')
L83 = Leader(83, 'l83', 'L83-D', 4557, 90, 'D')
L84 = Leader(84, 'l84', 'L82-F', 4367, 29, 'F')
L85 = Leader(85, 'l85', 'L82-G', 4597, 29, 'G')
L86 = Leader(86, 'l86', 'L82-H', 2567, 31, 'H')
L39 = Leader(39, 'l39', 'L39-E', 2562, 98, 'E')
L83.become_subordinate(L82)
L39.become_subordinate(L82)
L84.become_subordinate(L83)
L86.become_subordinate(L83)
L85.become_subordinate(L83)

e88 = Employee(88, "e88", 'E88', 4374, 88)
e41 = Employee(41, "e41", 'E41', 4234, 41)
e42 = Employee(42, "e42", 'E42', 4594, 42)
e43 = Employee(43, "e43", 'E43', 4104, 43)
e51 = Employee(51, "e51", 'E51', 4568, 51)
e61 = Employee(61, "e61", 'E61', 4372, 51)
e61.become_subordinate(e41)
e51.become_subordinate(e41)
e42.become_subordinate(e88)
e41.become_subordinate(e88)
e43.become_subordinate(e88)

L80 = Leader(80, "l80", 'L80-J', 4334, 88, 'J')
e4 = Employee(4, 'e4', 'E4', 4444, 34)
e5 = Employee(5, 'e5', 'E5', 4454, 35)
e6 = Employee(6, 'e6', 'E6', 4464, 27)
e5.become_subordinate(L80)
e6.become_subordinate(L80)
e4.become_subordinate(L80)

e7 = Employee(7, "e7", 'E88', 4374, 27)
L77 = Leader(77, 'L77', 'L77-I', 4567, 73, 'I')
L78 = Leader(78, 'L78', 'L78-IB', 4557, 78, 'IB')
L77.become_subordinate(e7)
L78.become_subordinate(e7)

L30 = Leader(30, 'l30', "L30-corp", 4278, 28, "corp")
# e30=Leader(30,'l30',"L30-corp",4278,28)
e3.become_subordinate(L30)
L82.become_subordinate(L30)
e88.become_subordinate(L30)
L80.become_subordinate(L30)
e7.become_subordinate(L30)

single_e = Employee(55, "single", 'single_pos', 4, 7)
single_l = Leader(55, "single", 'single_pos', 4, 7, 'No one cares')

def test_get_higher_paid_employee():

    # for i in range(1999,2562):
        assert e23.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e38, L39, e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, L86, e88]
    # for i in range(2562,2567):
        assert L39.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e38,  e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85,L86, e88]
    # for i in range(2567,2699):
        assert L86.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    # for i in range(2699,2799):
        assert e48.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    # for i in range(2799,3299):
        assert L58.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e51,
                                                        e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    # for i in range(3299,3399):
        assert e38.get_higher_paid_employees() == [e3, e4, e5, e6, e7,L30, e41, e42, e43, e51,
                                                        e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    # for i in range(3399, 3999):
        assert L81.get_higher_paid_employees() == [e3, e4, e5, e6, e7, L30, e41, e42, e43, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    # for i in range(3999, 4104):
        assert e3.get_higher_paid_employees() == [e4, e5, e6, e7, L30, e41, e42, e43, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    # for i in range(4104, 4234):
        assert e43.get_higher_paid_employees() == [e4, e5, e6, e7, L30, e41, e42,  e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    # for i in range(4234, 4278):
        assert e41.get_higher_paid_employees() == [e4, e5, e6, e7, L30, e42,  e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    # for i in range(4278,4334):
        assert L30.get_higher_paid_employees() == [e4, e5, e6, e7,  e42, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    # for i in range(4334,4367):
        assert L80.get_higher_paid_employees() == [e4, e5, e6, e7,  e42, e51,
                                                       e61, L77, L78,
                                                       L82, L83, L84, L85, e88]
    # for i in range(4367,4372):
        assert L84.get_higher_paid_employees() == [e4, e5, e6, e7,  e42, e51,e61,
                                                        L77, L78,
                                                       L82, L83, L85, e88]
    # for i in range(4372,4374):
        assert e61.get_higher_paid_employees() == [e4, e5, e6, e7,  e42, e51,
                                                        L77, L78,
                                                       L82, L83,  L85, e88]
    # for i in range(4374,4444):
        assert e88.get_higher_paid_employees() == [e4, e5, e6, e42, e51,
                                                        L77, L78,
                                                       L82, L83,  L85]
        assert e7.get_higher_paid_employees() == [e4, e5, e6, e42, e51,
                                                   L77, L78,
                                                   L82, L83, L85]
    # for i in range(4444,4454):
        assert e4.get_higher_paid_employees() == [e5, e6, e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    # for i in range(4454, 4464):
        assert e5.get_higher_paid_employees() == [e6, e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    # for i in range(4464, 4557):
        assert e6.get_higher_paid_employees() == [ e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    # for i in range(4557, 4567):
        assert L83.get_higher_paid_employees() == [ e42, e51,
                                                       L77,
                                                       L82,L85]
        assert L78.get_higher_paid_employees() == [e42, e51,
                                                   L77,
                                                   L82, L85]
    # for i in range(4567, 4568):
        assert L77.get_higher_paid_employees() == [ e42, e51,  L85]
        assert L82.get_higher_paid_employees() == [e42, e51, L85]
    # for i in range(4568, 4594):
        assert e51.get_higher_paid_employees() == [e42,  L85]
    # for i in range(4594, 4597):
        assert e42.get_higher_paid_employees() == [  L85]
    # for i in range(4597,100000):
        assert L85.get_higher_paid_employees() == []

if __name__ == '__main__':
    import pytest

    pytest.main(['e1_Sample_Non_Mutating_Teat.py'])