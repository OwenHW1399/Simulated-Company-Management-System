from organization_hierarchy import Employee, Leader,merge
#==Task1==#
#def __init__(self, eid: int, name: str, position: str, salary: float, rating: int) -> None:
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

def test_add_employee():
    lst=[]
    lst2=[]
    lst3=[1,23,56,77]
    lst4=[1,23,56,78]
    lst44=[13,24,55,74]
    lst5=[1,2,2,3,3,4]
    lst6=[1,4,4,5,7]
    assert merge(lst,lst2)==[]
    assert merge(lst2, lst) == []
    assert merge(lst,lst3)==[1,23,56,77]
    assert merge(lst3, lst) == [1, 23, 56, 77]
    assert merge(lst,lst5)==[1,2,2,3,3,4]
    assert merge(lst5, lst) == [1, 2, 2, 3, 3, 4]
    assert merge(lst3,lst3)==[1,1,23,23,56,56,77,77]
    assert merge(lst3, lst3) == [1, 1, 23, 23, 56, 56, 77, 77]
    assert merge(lst3,lst4)==[1,1,23,23,56,56,77,78]
    assert merge(lst4, lst3) == [1, 1, 23, 23, 56, 56, 77, 78]
    assert merge(lst3,lst44)==[1,13,23,24,55,56,74,77]
    assert merge(lst44, lst3) == [1, 13, 23, 24, 55, 56, 74, 77]
    assert merge(lst3,lst5)==[1,1,2,2,3,3,4,23,56,77]
    assert merge(lst5, lst3) == [1, 1, 2, 2, 3, 3, 4, 23, 56, 77]
    assert merge(lst, lst5) == [1, 2, 2, 3, 3, 4]
    assert merge(lst5,lst)==[1,2,2,3,3,4]
    assert merge(lst5,lst5)==[1,1,2,2,2,2,3,3,3,3,4,4]
    assert merge(lst5,lst6)==[1,1,2,2,3,3,4,4,4,5,7]
    assert merge(lst6, lst5) == [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 7]






if __name__ == '__main__':
    import pytest

    pytest.main(['e1_add_employee_sample_test.py'])