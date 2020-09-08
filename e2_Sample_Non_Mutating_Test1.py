from organization_hierarchy import Employee, Leader, merge
from typing import List
from e1_Sample_Non_Mutating_Test import increasing,increasing_salary,no_duplicate,increasing_eid
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
L84 = Leader(84, 'l84', 'L84-F', 4367, 29, 'F')
L85 = Leader(85, 'l85', 'L85-G', 4597, 29, 'G')
L86 = Leader(86, 'l86', 'L86-H', 2567, 31, 'H')
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

e7 = Employee(7, "e7", 'E7', 4374, 27)
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

def test_get_department_name():
    assert L58.get_department_name()=='C'
    for item in [L81,e48,e38]:
        assert item.get_department_name()=='B'
    for item in [e3,e23,e88,e41,e42,e43,e51,e61,e7,L30]:
        assert item.get_department_name()=='corp'
    for item in [e4,e5,e6,L80]:
        assert item.get_department_name()=='J'
    assert L77.get_department_name()=='I'
    assert L78.get_department_name()=="IB"
    assert L82.get_department_name()=='A'
    assert L83.get_department_name()=="D"
    assert L84.get_department_name()=="F"
    assert L85.get_department_name()=="G"
    assert L86.get_department_name()=="H"
    assert L39.get_department_name()=="E"
    assert single_l.get_department_name()=='No one cares'
    assert single_e.get_department_name()==''
def test_get_position_in_hierachy():
    #more
    assert L58.get_position_in_hierarchy()=='L58-C, C, B, corp'
    assert e38.get_position_in_hierarchy()=='E38, B, corp'
    assert e48.get_position_in_hierarchy() == 'E48, B, corp'
    assert L81.get_position_in_hierarchy() == 'L81-B, B, corp'
    assert e23.get_position_in_hierarchy() == 'E23, corp'
    assert e3.get_position_in_hierarchy() == 'E3, corp'
    assert L80.get_position_in_hierarchy() == 'L80-J, J, corp'
    assert e4.get_position_in_hierarchy() == 'E4, J, corp'
    assert e5.get_position_in_hierarchy() == 'E5, J, corp'
    assert e6.get_position_in_hierarchy() == 'E6, J, corp'
    assert L82.get_position_in_hierarchy() == 'L82-A, A, corp'
    assert L83.get_position_in_hierarchy() == 'L83-D, D, A, corp'
    assert L39.get_position_in_hierarchy() == 'L39-E, E, A, corp'
    assert L84.get_position_in_hierarchy() == 'L84-F, F, D, A, corp'
    assert L85.get_position_in_hierarchy() == 'L85-G, G, D, A, corp'
    assert L86.get_position_in_hierarchy() == 'L86-H, H, D, A, corp'
    assert e7.get_position_in_hierarchy() == 'E7, corp'
    assert L77.get_position_in_hierarchy() == 'L77-I, I, corp'
    assert L78.get_position_in_hierarchy() == 'L78-IB, IB, corp'
    assert e88.get_position_in_hierarchy() == 'E88, corp'
    assert e41.get_position_in_hierarchy() == 'E41, corp'
    assert e42.get_position_in_hierarchy() == 'E42, corp'
    assert e43.get_position_in_hierarchy() == 'E43, corp'
    assert e51.get_position_in_hierarchy() == 'E51, corp'
    assert e61.get_position_in_hierarchy() == 'E61, corp'
    assert L30.get_position_in_hierarchy() =="L30-corp, corp"
    assert single_l.get_position_in_hierarchy() == 'single_pos, No one cares'
    assert single_e.get_position_in_hierarchy() == 'single_pos'
def test_get_department_employee():
    assert single_l.get_department_employees()==[single_l]
    assert increasing_eid(L30.get_department_employees())
    assert L30.get_department_employees()==[e3, e4, e5, e6, e7, e23,L30 ,e38, L39, e41, e42, e43, e48, e51, L58, e61, L77, L78, L80, L81,
                 L82, L83, L84, L85, L86,e88]
    assert increasing_eid(L81.get_department_employees())
    assert L81.get_department_employees() == [e38,e48,L58,L81]
    assert increasing_eid(L58.get_department_employees())
    assert L58.get_department_employees() == [L58]
    assert increasing_eid(L80.get_department_employees())
    assert L80.get_department_employees() == [e4,e5,e6,L80]
    assert increasing_eid(L82.get_department_employees())
    assert L82.get_department_employees() ==[L39,L82,L83,L84,L85,L86]
    assert increasing_eid(L83.get_department_employees())
    assert L83.get_department_employees() == [L83, L84, L85, L86]
    assert increasing_eid(L84.get_department_employees())
    assert L84.get_department_employees() == [L84]
    assert increasing_eid(L85.get_department_employees())
    assert L85.get_department_employees() == [L85]
    assert increasing_eid(L86.get_department_employees())
    assert L86.get_department_employees() == [L86]
    assert increasing_eid(L77.get_department_employees())
    assert L77.get_department_employees()==[L77]
    assert increasing_eid(L78.get_department_employees())
    assert L78.get_department_employees() == [L78]

if __name__ == '__main__':
    import pytest

    pytest.main(['e2_Sample_Non_Mutating_Test1.py'])
