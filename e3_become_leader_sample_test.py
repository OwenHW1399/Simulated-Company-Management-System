from organization_hierarchy import Employee, Leader, merge
from typing import List
from e1_Sample_Non_Mutating_Test import increasing,increasing_salary,no_duplicate
def generate():
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
    L77 = Leader(77, 'l77', 'L77-I', 4567, 73, 'I')
    L78 = Leader(78, 'l78', 'L78-IB', 4557, 78, 'IB')
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

    dictt={}
    lst=[L30]
    lst.extend(L30.get_all_subordinates())
    for item in lst:
        dictt[item.name]=item
    dictt["single_e"]=single_e
    dictt["single_l"]=single_l
    return dictt
def test():
    for item in ['single_e','single_l']:
        dictt2 = generate()
        if item=='single_e':
            assert not isinstance(dictt2[item],Leader)
        else:
            assert isinstance(dictt2[item],Leader)
        id = dictt2[item].eid
        name = dictt2[item].name
        salary = dictt2[item].salary
        position = dictt2[item].position
        rating = dictt2[item].rating
        new_leader=dictt2[item].become_leader('new')
        assert isinstance(new_leader,Leader)
        assert new_leader.get_direct_subordinates()==[] and new_leader.get_all_subordinates()==[] and new_leader.get_superior() is None
        assert new_leader._department_name=='new'
        assert new_leader.name == name
        assert new_leader.salary == salary
        assert new_leader.eid == id
        assert new_leader.position == position
        assert new_leader.rating == rating

    for item in ['e3', 'e4', 'e5', 'e6', 'e7', 'e23', 'l30','e38', 'l39', 'e41', 'e42', 'e43', 'e48', 'e51', 'l58', 'e61','l77',
                 'l78', 'l80', 'l81',
                 'l82', 'l83', 'l84', 'l85', 'l86', 'e88']:

        if item in ['l30', 'l82', 'l83', 'l84', 'l85', 'l86', 'l39', 'l81', 'l58', 'l80', 'l77', 'l78']:
            dictt = generate()
            id=dictt[item].eid
            name=dictt[item].name
            salary=dictt[item].salary
            position=dictt[item].position
            rating=dictt[item].rating
            if item  in ['l82', 'l83', 'l81',  'l80']:
                assert dictt[item].get_direct_subordinates() != [] and dictt[item].get_superior() is not None
            elif item=='l30':
                assert dictt[item].get_direct_subordinates() != [] and dictt[item].get_superior() is None
            else:
                assert dictt[item].get_direct_subordinates() == [] and dictt[item].get_superior() is not None
            sub,sup=dictt[item].get_direct_subordinates(),dictt[item].get_superior()
            new_leader = dictt[item].become_leader("new_dep")
            if item !='l30':
                assert new_leader.name == name
                assert new_leader.salary == salary
                assert new_leader.eid == id
                assert new_leader.position == position
                assert new_leader.rating == rating
                assert dictt[item] in dictt['l30'].get_all_subordinates()
                assert no_duplicate(dictt['l30'].get_all_subordinates())
                assert new_leader in dictt['l30'].get_all_subordinates()
                assert new_leader.get_department_name()=='new_dep'
                assert new_leader is dictt[item]
                assert new_leader.get_superior()==sup
                assert new_leader.get_direct_subordinates()==sub
            else:
                assert new_leader is dictt['l30']
                assert new_leader.name == name
                assert new_leader.salary == salary
                assert new_leader.eid == id
                assert new_leader.position == position
                assert new_leader.rating == rating
                assert new_leader.get_department_name() == 'new_dep'

            assert new_leader.get_direct_subordinates()==sub and new_leader.get_superior()==sup
            assert dictt[item].get_direct_subordinates()==sub and dictt[item].get_superior() ==sup
            if item !='l30':
                assert dictt['l30'].get_employee(id) is dictt[item] and dictt['l30'].get_employee(id) is new_leader
            else:
                assert dictt['l30'] is new_leader

            assert dictt[item]._department_name=='new_dep'

            assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                              dictt['e88']]

            assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l81']]
            assert dictt['l81'].get_direct_subordinates() == [dictt['e38'], dictt['e48'], dictt['l58']]
            for item in [dictt['e38'], dictt['e48'], dictt['l58'], dictt['e23']]:
                assert item.get_direct_subordinates() == []

            assert dictt['l82'].get_direct_subordinates() == [dictt['l39'], dictt['l83']]
            assert dictt['l83'].get_direct_subordinates() == [dictt['l84'], dictt['l85'], dictt['l86']]
            for item in [dictt['l39'], dictt['l84'], dictt['l85'], dictt['l86']]:
                assert item.get_direct_subordinates() == []

            assert dictt['e88'].get_direct_subordinates() == [dictt['e41'], dictt['e42'], dictt['e43']]
            assert dictt['e41'].get_direct_subordinates() == [dictt['e51'], dictt['e61']]
            for item in [dictt['e51'], dictt['e61'], dictt['e42'], dictt['e43']]:
                assert item.get_direct_subordinates() == []

            assert dictt['l80'].get_direct_subordinates() == [dictt['e4'], dictt['e5'], dictt['e6']]
            for item in [dictt['e4'], dictt['e5'], dictt['e6']]:
                assert item.get_direct_subordinates() == []

            assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
            for item in [dictt['l77'], dictt['l78']]:
                assert item.get_direct_subordinates() == []
        else:
            dictt = generate()
            id=dictt[item].eid
            name=dictt[item].name
            salary=dictt[item].salary
            position=dictt[item].position
            rating=dictt[item].rating
            if item in ['e3', 'e88', 'e7','e41']:
                assert dictt[item].get_direct_subordinates() != [] and dictt[item].get_superior() is not None
            else:
                assert dictt[item].get_direct_subordinates() == [] and dictt[item].get_superior() is not None
            sub, sup = dictt[item].get_direct_subordinates(), dictt[item].get_superior()
            new_leader = dictt[item].become_leader("new_dep")
            assert new_leader.name == name
            assert new_leader.salary == salary
            assert new_leader.eid == id
            assert new_leader.position == position
            assert new_leader.rating == rating
            assert dictt[item] not in dictt['l30'].get_all_subordinates()
            assert dictt[item] is not new_leader
            assert new_leader in dictt['l30'].get_all_subordinates()
            assert new_leader.get_direct_subordinates() == sub and new_leader.get_superior() == sup
            assert dictt[item].get_direct_subordinates() == [] and dictt[item].get_superior() is None and dictt[item].get_all_subordinates()==[]
            assert dictt['l30'].get_employee(id) is not dictt[item] and dictt['l30'].get_employee(id) is new_leader
            assert isinstance(new_leader,Leader)
            assert new_leader._department_name=='new_dep'
            dictt[item]=dictt['l30'].get_employee(id)
            assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                              dictt['e88']]

            assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l81']]
            assert dictt['l81'].get_direct_subordinates() == [dictt['e38'], dictt['e48'],dictt['l58']]
            for item2 in [dictt['e38'], dictt['e48'], dictt['l58'], dictt['e23']]:
                assert item2.get_direct_subordinates() == []

            assert dictt['l82'].get_direct_subordinates() == [dictt['l39'], dictt['l83']]
            assert dictt['l83'].get_direct_subordinates() == [dictt['l84'], dictt['l85'], dictt['l86']]
            for item2 in [dictt['l39'], dictt['l84'], dictt['l85'], dictt['l86']]:
                assert item2.get_direct_subordinates() == []

            assert dictt['e88'].get_direct_subordinates() == [dictt['e41'], dictt['e42'], dictt['e43']]
            assert dictt['e41'].get_direct_subordinates() == [dictt['e51'], dictt['e61']]
            for item2 in [dictt['e51'], dictt['e61'], dictt['e42'], dictt['e43']]:
                assert item2.get_direct_subordinates() == []

            assert dictt['l80'].get_direct_subordinates() == [dictt['e4'], dictt['e5'], dictt['e6']]
            for item2 in [dictt['e4'], dictt['e5'], dictt['e6']]:
                assert item2.get_direct_subordinates() == []

            assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
            for item2 in [dictt['l77'], dictt['l78']]:
                assert item2.get_direct_subordinates() == []
if __name__ == '__main__':
    import pytest

    pytest.main(['e3_become_leader_sample_test.py'])
