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


# Task 1

def increasing(lst: List[Employee]) -> bool:
    counter = 0
    flag = True
    while counter + 1 < len(lst):
        if lst[counter] > lst[counter + 1]:
            flag = False
            return False
        counter += 1
    return flag

def increasing_eid(lst: List[Employee]) -> bool:
    counter = 0
    flag = True
    while counter + 1 < len(lst):
        if lst[counter].eid > lst[counter + 1].eid:
            flag = False
            return False
        counter += 1
    return flag

def increasing_salary(lst) -> bool:
    counter = 0
    flag = True
    while counter + 1 < len(lst):
        if lst[counter].salary > lst[counter + 1].salary:
            flag = False
        counter += 1
    return flag


def no_duplicate(lst2) -> bool:
    flag = True
    counter = 0
    while counter < len(lst2):
        temp = lst2[0:counter]
        temp.extend(lst2[counter + 1:])
        if lst2[counter] in temp:
            flag = False
        counter += 1
    return flag


def test_get_direct_sub():
    assert single_e.get_direct_subordinates() == []
    assert single_l.get_direct_subordinates() == []
    assert L30.get_direct_subordinates() == [e3, e7, L80, L82, e88]
    assert increasing_eid(L30.get_direct_subordinates())

    assert e3.get_direct_subordinates() == [e23, L81]
    assert increasing_eid(e3.get_direct_subordinates())
    assert L81.get_direct_subordinates() == [e38, e48, L58]
    assert increasing_eid(L81.get_direct_subordinates())
    for item in [e38, e48, L58, e23]:
        assert item.get_direct_subordinates() == []

    assert L82.get_direct_subordinates() == [L39, L83]
    assert L83.get_direct_subordinates() == [L84, L85, L86]
    assert increasing_eid(L82.get_direct_subordinates())
    assert increasing_eid(L83.get_direct_subordinates())
    for item in [L39, L84, L85, L86]:
        assert item.get_direct_subordinates() == []

    assert e88.get_direct_subordinates() == [e41, e42, e43]
    assert e41.get_direct_subordinates() == [e51, e61]
    assert increasing_eid(e88.get_direct_subordinates())
    assert increasing_eid(e41.get_direct_subordinates())
    for item in [e51, e61, e42, e43]:
        assert item.get_direct_subordinates() == []

    assert L80.get_direct_subordinates() == [e4, e5, e6]
    assert increasing_eid(L80.get_direct_subordinates())
    for item in [e4, e5, e6]:
        assert item.get_direct_subordinates() == []

    assert e7.get_direct_subordinates() == [L77, L78]
    assert increasing_eid(e7.get_direct_subordinates())
    for item in [L77, L78]:
        assert item.get_direct_subordinates() == []


def test_get_all_subodinates():
    assert single_e.get_all_subordinates() == []
    assert single_l.get_all_subordinates() == []
    assert L30.get_all_subordinates() == [e3, e4, e5, e6, e7, e23, e38, L39, e41, e42, e43, e48, e51, L58, e61, L77,
                                          L78, L80, L81,
                                          L82, L83, L84, L85, L86, e88]
    assert  increasing_eid(L30.get_all_subordinates())

    assert e3.get_all_subordinates() == [e23, e38, e48, L58, L81]
    assert L81.get_all_subordinates() == [e38, e48, L58]
    assert increasing_eid(e3.get_all_subordinates())
    assert increasing_eid(L81.get_all_subordinates())
    for item in [e38, e48, L58, e23]:
        assert item.get_all_subordinates() == []

    assert L82.get_all_subordinates() == [L39, L83, L84, L85, L86]
    assert L83.get_all_subordinates() == [L84, L85, L86]
    assert increasing_eid(L82.get_all_subordinates())
    assert increasing_eid(L83.get_all_subordinates())
    for item in [L39, L84, L85, L86]:
        assert item.get_all_subordinates() == []

    assert e88.get_all_subordinates() == [e41, e42, e43, e51, e61]
    assert e41.get_all_subordinates() == [e51, e61]
    assert increasing_eid(e88.get_all_subordinates())
    assert increasing_eid(e41.get_all_subordinates())
    for item in [e51, e61, e42, e43]:
        assert item.get_all_subordinates() == []

    assert L80.get_all_subordinates() == [e4, e5, e6]
    assert increasing_eid(L80.get_all_subordinates())
    for item in [e4, e5, e6]:
        assert item.get_all_subordinates() == []

    assert e7.get_all_subordinates() == [L77, L78]
    assert increasing_eid(e7.get_all_subordinates())
    for item in [L77, L78]:
        assert item.get_all_subordinates() == []
    lst = L30.get_all_subordinates()
    lst.append(L30)
    for item in lst:
        assert increasing(item.get_all_subordinates())


def test_get_organization_head():
    assert single_e.get_organization_head() == single_e
    assert single_l.get_organization_head() == single_l
    for item in [L30, e3, e4, e5, e6, e7, e23, e38, L39, e41, e42, e43, e48, e51, L58, e61, L77, L78, L80, L81,
                 L82, L83, L84, L85, L86, e88]:
        assert  item.get_organization_head() == L30


def test_get_superior():
    assert single_l.get_superior() is None
    assert single_e.get_superior() is None
    assert L30.get_superior() is None

    assert e3.get_superior() == L30
    assert L81.get_superior() == e3
    for item in [e38, e48, L58]:
        assert item.get_superior() == L81
    assert e23.get_superior() == e3

    assert L82.get_superior() == L30
    assert L83.get_superior() == L82
    assert L39.get_superior() == L82
    for item in [L84, L85, L86]:
        assert item.get_superior() == L83

    assert e88.get_superior() == L30
    assert e41.get_superior() == e88
    for item in [e41, e42, e43]:
        assert item.get_superior() == e88
    for item in [e51, e61]:
        assert item.get_superior() == e41

    assert L80.get_superior() == L30
    for item in [e4, e5, e6]:
        assert item.get_superior() == L80

    assert e7.get_superior() == L30
    for item in [L77, L78]:
        assert item.get_superior() == e7


def test_get_employee():
    # more:write some real output to check
    for i in range(0, 100):
        if i == single_e.eid:
            assert single_e.get_employee(i) == single_e
        else:
            assert single_e.get_employee(i) is None

    for i in range(0, 100):
        if i == single_l.eid:
            assert single_l.get_employee(i) == single_l
        else:
            assert single_l.get_employee(i) is None

    lst = L30.get_all_subordinates()
    lst.append(L30)
    for item in lst:
        lst2 = []
        for item2 in item.get_all_subordinates():
            lst2.append(item2.eid)
        lst2.append(item.eid)
        counter = 0
        while counter < len(lst2):
            temp = lst2[0:counter]
            temp.extend(lst2[counter + 1:])
            assert lst2[counter] not in temp
            counter += 1
        for i in range(0, 100):
            if i in lst2:
                assert item.get_employee(i).eid == i
            else:
                assert item.get_employee(i) is None
    for i in range(0,101):
        if i==30:
            assert L30.get_employee(i)==L30
        elif i==3:
            assert L30.get_employee(i)==e3
        elif i==81:
            assert L30.get_employee(i)==L81
        elif i==23:
            assert L30.get_employee(i)==e23
        elif i ==58:
            assert L30.get_employee(i) ==L58
        elif i==38:
            assert L30.get_employee(i)==e38
        elif i==48:
            assert L30.get_employee(i)==e48
        elif i==80:
            assert L30.get_employee(i)==L80
        elif i==4:
            assert L30.get_employee(i)==e4
        elif i==5:
            assert L30.get_employee(i)==e5
        elif i==6:
            assert L30.get_employee(i)==e6
        elif i==82:
            assert L30.get_employee(i)==L82
        elif i==83:
            assert L30.get_employee(i)==L83
        elif i==39:
            assert L30.get_employee(i)==L39
        elif i==84:
            assert L30.get_employee(i)==L84
        elif i ==85:
            assert L30.get_employee(i) ==L85
        elif i ==86:
            assert L30.get_employee(i) ==L86
        elif i ==7:
            assert L30.get_employee(i) ==e7
        elif i ==77:
            assert L30.get_employee(i) ==L77
        elif i ==78:
            assert L30.get_employee(i) ==L78
        elif i ==88:
            assert L30.get_employee(i) ==e88
        elif i ==41:
            assert L30.get_employee(i) ==e41
        elif i ==42:
            assert L30.get_employee(i) ==e42
        elif i ==43:
            assert L30.get_employee(i) ==e43
        elif i ==51:
            assert L30.get_employee(i) ==e51
        elif i ==61:
            assert L30.get_employee(i) ==e61
        else:
            assert L30.get_employee(i) is None


def test_get_employee_paid_more_than():
    # more:write some real output to check
    for i in range(0, 100000):
        if i in range(0, int(single_e.salary)):
            assert single_e.get_employees_paid_more_than(i) == [single_e]
        else:
            assert single_e.get_employees_paid_more_than(i) == []

    for i in range(0, 100000):
        if i in range(0, int(single_l.salary)):
            assert single_l.get_employees_paid_more_than(i) == [single_l]
        else:
            assert single_l.get_employees_paid_more_than(i) == []

    lst = L30.get_all_subordinates()
    lst.append(L30)
    lst_salary = []
    for item in lst:
        if item.salary not in lst_salary:
            lst_salary = merge(lst_salary, [item.salary])
    assert len(lst_salary) == 23
    assert increasing(lst_salary) is True
    i = 0
    while i + 1 < len(lst_salary):
        if i == 0:
            for t in range(0, lst_salary[0]):
                for item in lst:
                    lsst = merge(item.get_all_subordinates(), [item])
                    assert increasing(lsst) is True
                    assert no_duplicate(lsst) is True
                    assert item.get_employees_paid_more_than(t) == lsst
                    assert increasing_eid(lsst)

        else:
            for t in range(lst_salary[i], lst_salary[i + 1]):
                for item in lst:
                    lsst = merge(item.get_all_subordinates(), [item])
                    lsst2 = []
                    for item2 in lsst:
                        lsst2.append(item2)
                    assert lsst2 == lsst
                    assert increasing(lsst) is True
                    assert increasing(lsst2) is True
                    assert no_duplicate(lsst) is True
                    assert no_duplicate(lsst2) is True
                    for item2 in lsst:
                        if item2.salary <= lst_salary[i]:
                            lsst2.remove(item2)
                    assert increasing(lsst2) is True
                    assert no_duplicate(lsst2) is True
                    assert item.get_employees_paid_more_than(t) == lsst2
                    assert increasing_eid(item.get_employees_paid_more_than(t))
        i += 1
def test_get_employee_paid_more2():
    for i in range(0,1999):
        assert L30.get_employees_paid_more_than(i)==[e3, e4, e5, e6, e7, e23,L30 ,e38, L39, e41, e42, e43, e48, e51, L58, e61, L77, L78, L80, L81,
                 L82, L83, L84, L85, L86, e88]
    for i in range(1999,2562):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e38, L39, e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, L86, e88]
    for i in range(2562,2567):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e38,  e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85,L86, e88]
    for i in range(2567,2699):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e48, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    for i in range(2699,2799):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e51,
                                                       L58, e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    for i in range(2799,3299):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e38,e41, e42, e43, e51,
                                                        e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    for i in range(3299,3399):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7,L30, e41, e42, e43, e51,
                                                        e61, L77, L78, L80, L81,
                                                       L82, L83, L84, L85, e88]
    for i in range(3399, 3999):
        assert L30.get_employees_paid_more_than(i) == [e3, e4, e5, e6, e7, L30, e41, e42, e43, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    for i in range(3999, 4104):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7, L30, e41, e42, e43, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    for i in range(4104, 4234):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7, L30, e41, e42,  e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    for i in range(4234, 4278):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7, L30, e42,  e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    for i in range(4278,4334):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7,  e42, e51,
                                                       e61, L77, L78, L80,
                                                       L82, L83, L84, L85, e88]
    for i in range(4334,4367):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7,  e42, e51,
                                                       e61, L77, L78,
                                                       L82, L83, L84, L85, e88]
    for i in range(4367,4372):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7,  e42, e51,e61,
                                                        L77, L78,
                                                       L82, L83, L85, e88]
    for i in range(4372,4374):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e7,  e42, e51,
                                                        L77, L78,
                                                       L82, L83,  L85, e88]
    for i in range(4374,4444):
        assert L30.get_employees_paid_more_than(i) == [e4, e5, e6, e42, e51,
                                                        L77, L78,
                                                       L82, L83,  L85]
    for i in range(4444,4454):
        assert L30.get_employees_paid_more_than(i) == [e5, e6, e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    for i in range(4454, 4464):
        assert L30.get_employees_paid_more_than(i) == [e6, e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    for i in range(4464, 4557):
        assert L30.get_employees_paid_more_than(i) == [ e42, e51,
                                                       L77, L78,
                                                       L82, L83, L85]
    for i in range(4557, 4567):
        assert L30.get_employees_paid_more_than(i) == [ e42, e51,
                                                       L77,
                                                       L82,L85]
    for i in range(4567, 4568):
        assert L30.get_employees_paid_more_than(i) == [ e42, e51,  L85]
    for i in range(4568, 4594):
        assert L30.get_employees_paid_more_than(i) == [e42,  L85]
    for i in range(4594, 4597):
        assert L30.get_employees_paid_more_than(i) == [  L85]
    for i in range(4597,100000):
        assert L30.get_employees_paid_more_than(i) == []
def test_get_higher_paid_employee():
    # more:write some real output to check
    assert single_e.get_higher_paid_employees() == [] and \
           single_l.get_higher_paid_employees() == []
    lst = L30.get_all_subordinates()
    lst.append(L30)
    lst.sort(key=lambda x: x.salary)
    assert increasing_salary(lst) is True
    counter = 0
    while counter + 1 < len(lst):
        if lst[counter].salary < lst[counter + 1].salary:
            ll = lst[counter].get_higher_paid_employees()
            assert len(ll) == len(lst[counter + 1:])
            for item in ll:
                assert item in lst[counter + 1:]
            assert no_duplicate(ll)
            assert increasing_eid(ll)

        elif lst[counter].salary == lst[counter + 1].salary:
            ll = lst[counter].get_higher_paid_employees()
            ll2 = lst[counter + 1].get_higher_paid_employees()
            assert ll == ll2
            assert len(ll) == len(lst[counter + 2:])
            assert len(ll2) == len(lst[counter + 2:])
            for item in ll:
                assert item in lst[counter + 2:]
                assert item in ll2
            for item in ll2:
                assert item in lst[counter + 2:]
            assert no_duplicate(ll)
            assert increasing_eid(ll)
            assert no_duplicate(ll2)
            assert increasing_eid(ll2)
        counter += 1


def test_get_closet_common_superior():
    lst = L30.get_all_subordinates()
    lst.append(L30)
    assert no_duplicate(lst)
    full_list = [30, 3, 4, 5, 6, 7, 23, 38, 39, 41, 42, 43, 48, 51, 58, 61, 77, 78, 80, 81, 82, 83, 84, 85, 86, 88]
    for item in lst:
        assert item.get_closest_common_superior(item.eid) == item
    for i in range(0, 101):
        if i == 55:
            assert single_l.get_closest_common_superior(i) == single_l
            assert single_e.get_closest_common_superior(i) == single_e
        else:
            assert single_l.get_closest_common_superior(i) ==single_l
            assert single_e.get_closest_common_superior(i) ==single_e

        if i in full_list:
            assert L30.get_closest_common_superior(i) == L30
        else:
            assert L30.get_closest_common_superior(i) ==L30

        if i in [3, 23, 38, 48, 58, 81]:
            assert e3.get_closest_common_superior(i) == e3
        elif i in full_list:
            assert e3.get_closest_common_superior(i) == L30
        else:
            assert e3.get_closest_common_superior(i) == e3

        if i in [38, 48, 58, 81]:
            assert L81.get_closest_common_superior(i) == L81
        elif i == 23 or i == 3:
            assert L81.get_closest_common_superior(i) == e3
        elif i in full_list:
            assert L81.get_closest_common_superior(i) == L30
        else:
            assert L81.get_closest_common_superior(i) ==L81

        if i in [38, 48, 58, 81, 3]:
            assert e23.get_closest_common_superior(i) == e3
        elif i == 23:
            assert e23.get_closest_common_superior(i) == e23
        elif i in full_list:
            assert e23.get_closest_common_superior(i) == L30
        else:
            assert e23.get_closest_common_superior(i) ==e23

        if i == 81:
            assert L58.get_closest_common_superior(i) == L81
            assert e48.get_closest_common_superior(i) == L81
            assert e38.get_closest_common_superior(i) == L81
        elif i == 23 or i == 3:
            assert L58.get_closest_common_superior(i) == e3
            assert e48.get_closest_common_superior(i) == e3
            assert e38.get_closest_common_superior(i) == e3
        elif i == 58:
            assert e48.get_closest_common_superior(i) == L81
            assert e38.get_closest_common_superior(i) == L81
            assert L58.get_closest_common_superior(i) == L58
        elif i == 48:
            assert L58.get_closest_common_superior(i) == L81
            assert e48.get_closest_common_superior(i) == e48
            assert e38.get_closest_common_superior(i) == L81
        elif i == 38:
            assert L58.get_closest_common_superior(i) == L81
            assert e48.get_closest_common_superior(i) == L81
            assert e38.get_closest_common_superior(i) == e38
        elif i in full_list:
            assert L58.get_closest_common_superior(i) == L30
            assert e48.get_closest_common_superior(i) == L30
            assert e38.get_closest_common_superior(i) == L30
        else:
            assert L58.get_closest_common_superior(i) ==L58
            assert e48.get_closest_common_superior(i) ==e48
            assert e38.get_closest_common_superior(i) ==e38

        if i in [82, 83, 84, 85, 86, 39]:
            assert L82.get_closest_common_superior(i) == L82
        elif i in full_list:
            assert L82.get_closest_common_superior(i) == L30
        else:
            assert L82.get_closest_common_superior(i) ==L82

        if i in [83, 84, 85, 86]:
            assert L83.get_closest_common_superior(i) == L83
        elif i == 82 or i == 39:
            assert L83.get_closest_common_superior(i) == L82
        elif i in full_list:
            assert L83.get_closest_common_superior(i) == L30
        else:
            assert L83.get_closest_common_superior(i) ==L83

        if i in [82, 83, 84, 85, 86]:
            assert L39.get_closest_common_superior(i) == L82
        elif i == 39:
            assert L39.get_closest_common_superior(i) == L39
        elif i in full_list:
            assert L39.get_closest_common_superior(i) == L30
        else:
            assert L39.get_closest_common_superior(i) ==L39

        if i == 83:
            assert L84.get_closest_common_superior(i) == L83
            assert L85.get_closest_common_superior(i) == L83
            assert L86.get_closest_common_superior(i) == L83
        elif i == 39 or i == 82:
            assert L86.get_closest_common_superior(i) == L82
            assert L84.get_closest_common_superior(i) == L82
            assert L85.get_closest_common_superior(i) == L82
        elif i == 84:
            assert L84.get_closest_common_superior(i) == L84
            assert L85.get_closest_common_superior(i) == L83
            assert L86.get_closest_common_superior(i) == L83
        elif i == 85:
            assert L84.get_closest_common_superior(i) == L83
            assert L85.get_closest_common_superior(i) == L85
            assert L86.get_closest_common_superior(i) == L83
        elif i == 86:
            assert L84.get_closest_common_superior(i) == L83
            assert L85.get_closest_common_superior(i) == L83
            assert L86.get_closest_common_superior(i) == L86
        elif i in full_list:
            assert L84.get_closest_common_superior(i) == L30
            assert L85.get_closest_common_superior(i) == L30
            assert L86.get_closest_common_superior(i) == L30
        else:
            assert L84.get_closest_common_superior(i) ==L84
            assert L85.get_closest_common_superior(i) ==L85
            assert L86.get_closest_common_superior(i) ==L86

        if i in [88, 41, 42, 43, 51, 61]:
            assert e88.get_closest_common_superior(i) == e88
        elif i in full_list:
            assert e88.get_closest_common_superior(i) == L30

        if i in [88, 42, 43]:
            assert e41.get_closest_common_superior(i) == e88
        elif i in [41, 51, 61]:
            assert e41.get_closest_common_superior(i) == e41
        elif i in full_list:
            assert e41.get_closest_common_superior(i) == L30
        else:
            assert e41.get_closest_common_superior(i) ==e41
        if i in [41,51,61,88]:
            assert e42.get_closest_common_superior(i)==e88
            assert e43.get_closest_common_superior(i)==e88
        elif i == 42:
            assert e42.get_closest_common_superior(i)==e42
            assert e43.get_closest_common_superior(i)==e88
        elif i==43:
            assert e42.get_closest_common_superior(i) == e88
            assert e43.get_closest_common_superior(i) == e43
        elif i in full_list:
            assert e42.get_closest_common_superior(i) == L30
            assert e43.get_closest_common_superior(i) == L30
        else:
            assert e42.get_closest_common_superior(i) == e42
            assert e43.get_closest_common_superior(i) == e43
        if i == 41:
            assert e51.get_closest_common_superior(i) == e41
            assert e61.get_closest_common_superior(i) == e41
        elif i == 61:
            assert e61.get_closest_common_superior(i) == e61
            assert e51.get_closest_common_superior(i) == e41
        elif i == 51:
            assert e61.get_closest_common_superior(i) == e41
            assert e51.get_closest_common_superior(i) == e51
        elif i == 42 or i == 43 or i == 88:
            assert e61.get_closest_common_superior(i) == e88
            assert e51.get_closest_common_superior(i) == e88
        elif i in full_list:
            assert e61.get_closest_common_superior(i) == L30
            assert e51.get_closest_common_superior(i) == L30
        else:
            assert e61.get_closest_common_superior(i) ==e61
            assert e51.get_closest_common_superior(i) ==e51

        if i in [4, 5, 6, 80]:
            assert L80.get_closest_common_superior(i) == L80
        elif i in full_list:
            assert L80.get_closest_common_superior(i) == L30
        else:
            assert L80.get_closest_common_superior(i) ==L80

        if i == 4:
            assert e4.get_closest_common_superior(i) == e4
            assert e5.get_closest_common_superior(i) == L80
            assert e6.get_closest_common_superior(i) == L80
        elif i == 5:
            assert e4.get_closest_common_superior(i) == L80
            assert e5.get_closest_common_superior(i) == e5
            assert e6.get_closest_common_superior(i) == L80
        elif i == 6:
            assert e4.get_closest_common_superior(i) == L80
            assert e5.get_closest_common_superior(i) == L80
            assert e6.get_closest_common_superior(i) == e6
        elif i == 80:
            assert e4.get_closest_common_superior(i) == L80
            assert e5.get_closest_common_superior(i) == L80
            assert e6.get_closest_common_superior(i) == L80
        elif i in full_list:
            assert e4.get_closest_common_superior(i) == L30
            assert e5.get_closest_common_superior(i) == L30
            assert e6.get_closest_common_superior(i) == L30
        else:
            assert e4.get_closest_common_superior(i) == e4
            assert e5.get_closest_common_superior(i) == e5
            assert e6.get_closest_common_superior(i) ==e6

        if i in [7, 77, 78]:
            assert e7.get_closest_common_superior(i) == e7
        elif i in full_list:
            assert e7.get_closest_common_superior(i) == L30
        else:
            assert e7.get_closest_common_superior(i) == e7

        if i == 78:
            assert L78.get_closest_common_superior(i) == L78
            assert L77.get_closest_common_superior(i) == e7
        elif i == 77:
            assert L78.get_closest_common_superior(i) == e7
            assert L77.get_closest_common_superior(i) == L77
        elif i == 7:
            assert L78.get_closest_common_superior(i) == e7
            assert L77.get_closest_common_superior(i) == e7
        elif i in full_list:
            assert L78.get_closest_common_superior(i) == L30
            assert L77.get_closest_common_superior(i) == L30
        else:
            assert L78.get_closest_common_superior(i) == L78
            assert L77.get_closest_common_superior(i) == L77


if __name__ == '__main__':
    import pytest

    pytest.main(['e1_Sample_Non_Mutating_Test.py'])
