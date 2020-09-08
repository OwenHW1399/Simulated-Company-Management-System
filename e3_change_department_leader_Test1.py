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

def test_Leader():
    for item in ['l30','l82','l83','l84','l85','l86','l39','l81','l58','l80','l77','l78']:
        dictt=generate()
        head=dictt[item].change_department_leader()
        """
        for item in dictt:
            if item != 'single_e' and item != 'single_l':
                assert dictt[item].get_organization_head() is dictt['l30']
            else:
                assert dictt[item].change_department_leader() is dictt[item]
        """

        assert head.get_organization_head() is dictt['l30']

        assert dictt['single_e'].get_direct_subordinates() == []
        assert dictt['single_l'].get_direct_subordinates() == []
        assert dictt['single_e'].change_department_leader() is dictt['single_e']
        assert dictt['single_l'].change_department_leader() is dictt['single_l']
        assert dictt['single_e'].get_direct_subordinates() == []
        assert dictt['single_l'].get_direct_subordinates() == []
        assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'], dictt['e88']]

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

        assert dictt['l80'].get_direct_subordinates() == [dictt['e4'], dictt['e5'],dictt['e6']]
        for item in [dictt['e4'], dictt['e5'], dictt['e6']]:
            assert item.get_direct_subordinates() == []

        assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
        for item in [dictt['l77'], dictt['l78']]:
            assert item.get_direct_subordinates() == []
def test_e48():
    dictt = generate()
    assert not isinstance(dictt['e48'],Leader)
    assert  isinstance(dictt['l81'], Leader)
    head = dictt['e48'].change_department_leader()
    assert head==dictt['l30']
    for item in dictt:
        if item != 'single_e' and item != 'single_l':
            pass
        else:
            assert dictt[item].change_department_leader() is dictt[item]
    assert dictt['single_e'].get_direct_subordinates() == []
    assert dictt['single_l'].get_direct_subordinates() == []
    dictt['l48']=head.get_employee(48)
    dictt['e81']=head.get_employee(81)
    assert not isinstance(dictt['e81'], Leader)
    assert isinstance(dictt['l48'], Leader)
    assert dictt['e48'].get_superior() is None and dictt['e48'].get_all_subordinates()==[]
    assert dictt['l81'].get_superior() is None and dictt['l81'].get_all_subordinates() == []
    assert dictt['l48'].name==dictt['e48'].name
    assert dictt['l48'].salary==dictt['e48'].salary
    assert dictt['l48'].eid==48
    assert dictt['l48'].position==dictt['e48'].position
    assert dictt['l48'].rating==dictt['e48'].rating
    assert dictt['l48']._department_name==dictt['l81']._department_name
    assert dictt['e48'] not in head.get_all_subordinates()
    assert dictt['l48'] in head.get_all_subordinates()
    assert dictt['e81'].name == dictt['l81'].name
    assert dictt['e81'].salary == dictt['l81'].salary
    assert dictt['e81'].eid == 81
    assert dictt['e81'].position == dictt['l81'].position
    assert dictt['e81'].rating == dictt['l81'].rating
    assert dictt['l81'] not in head.get_all_subordinates()
    assert dictt['e81']  in head.get_all_subordinates()

    assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                      dictt['e88']]
    assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l48']]
    assert dictt['l81'].get_direct_subordinates() == []
    assert dictt['l48'].get_direct_subordinates() == [dictt['e81']]
    for item in [ dictt['e48'], dictt['l58'], dictt['e23']]:
        assert item.get_direct_subordinates() == []
    assert dictt['e81'].get_direct_subordinates()==[dictt['e38'],dictt['l58']]
def test_e23():
    dictt = generate()
    assert not isinstance(dictt['e23'], Leader)
    assert isinstance(dictt['l30'], Leader)
    head = dictt['e23'].change_department_leader()
    dictt['l23'] = head.get_employee(23)
    dictt['e30'] = head.get_employee(30)
    assert head == dictt['l23']
    for item in dictt:
        if item != 'single_e' and item != 'single_l':
            pass
        else:
            assert dictt[item].change_department_leader() is dictt[item]
    assert dictt['single_e'].get_direct_subordinates() == []
    assert dictt['single_l'].get_direct_subordinates() == []
    assert not isinstance(dictt['e30'], Leader)
    assert isinstance(dictt['l23'], Leader)
    assert dictt['l23'].name == dictt['e23'].name
    assert dictt['l23'].salary == dictt['e23'].salary
    assert dictt['l23'].eid == 23
    assert dictt['l23'].position == dictt['e23'].position
    assert dictt['l23'].rating == dictt['e23'].rating
    assert dictt['l23']._department_name == dictt['l30']._department_name
    assert dictt['e23'] not in head.get_all_subordinates()
    assert dictt['l23'] in head.get_all_subordinates() or dictt['l23'] is head
    assert dictt['e30'].name == dictt['l30'].name
    assert dictt['e30'].salary == dictt['l30'].salary
    assert dictt['e30'].eid == 30
    assert dictt['e30'].position == dictt['l30'].position
    assert dictt['e30'].rating == dictt['l30'].rating
    assert dictt['l30'] not in head.get_all_subordinates()
    assert dictt['e30'] in head.get_all_subordinates()

    assert dictt['e30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                      dictt['e88']]
    assert dictt['e30'].get_superior()==dictt['l23']
    assert dictt['l23'].get_direct_subordinates()==[dictt['e30']]

    assert dictt['e23'].get_superior() is None and dictt['e23'].get_all_subordinates() == []
    assert dictt['l30'].get_superior() is None and dictt['l30'].get_all_subordinates() == []

    assert dictt['e3'].get_direct_subordinates() == [dictt['l81']]

def test_e3():
    dictt = generate()
    assert not isinstance(dictt['e3'], Leader)
    assert isinstance(dictt['l30'], Leader)
    head = dictt['e3'].change_department_leader()
    dictt['l3'] = head.get_employee(3)
    dictt['e30'] = head.get_employee(30)
    assert head == dictt['l3']
    for item in dictt:
        if item != 'single_e' and item != 'single_l':
            pass
        else:
            assert dictt[item].change_department_leader() is dictt[item]
    assert dictt['single_e'].get_direct_subordinates() == []
    assert dictt['single_l'].get_direct_subordinates() == []
    assert not isinstance(dictt['e30'], Leader)
    assert isinstance(dictt['l3'], Leader)
    assert dictt['l3'].name == dictt['e3'].name
    assert dictt['l3'].salary == dictt['e3'].salary
    assert dictt['l3'].eid == 3
    assert dictt['l3'].position == dictt['e3'].position
    assert dictt['l3'].rating == dictt['e3'].rating
    assert dictt['l3']._department_name == dictt['l30']._department_name
    assert dictt['e3'] not in head.get_all_subordinates()
    assert dictt['l3'] in head.get_all_subordinates() or dictt['l3'] is head
    assert dictt['e30'].name == dictt['l30'].name
    assert dictt['e30'].salary == dictt['l30'].salary
    assert dictt['e30'].eid == 30
    assert dictt['e30'].position == dictt['l30'].position
    assert dictt['e30'].rating == dictt['l30'].rating
    assert dictt['l30'] not in head.get_all_subordinates()
    assert dictt['e30'] in head.get_all_subordinates()
    assert dictt['e3'].get_superior() is None and dictt['e3'].get_all_subordinates() == []
    assert dictt['l30'].get_superior() is None and dictt['l30'].get_all_subordinates() == []

    assert dictt['e30'].get_direct_subordinates() == [dictt['e7'], dictt['l80'], dictt['l82'],
                                                      dictt['e88']]
    assert dictt['l3'].get_direct_subordinates() == [ dictt['e23'],dictt['e30'],dictt['l81']]

def test_4_5_6():
    for item in ['e4','e5','e6']:
        dictt=generate()
        if item == 'e4':
            item2='e5'
            item3='e6'
        elif item == 'e5':
            item2='e4'
            item3='e6'
        else:
            item2='e4'
            item3='e5'
        assert not isinstance(dictt[item], Leader)
        assert isinstance(dictt['l30'], Leader)
        head = dictt[item].change_department_leader()
        new_name='l' + str(dictt[item].eid)

        if item==dictt['e4']:
            assert new_name not in dictt and new_name=='l4'
        elif item==dictt['e5']:
            assert new_name not in dictt and new_name=='l5'
        elif item==dictt['e6']:
            assert new_name not in dictt and new_name=='l6'

        dictt[new_name] = head.get_employee(dictt[item].eid)
        dictt['e80'] = head.get_employee(80)
        assert head == dictt['l30']
        for item7 in dictt:
            if item7 != 'single_e' and item7 != 'single_l':
                pass
            else:
                assert dictt[item7].change_department_leader() is dictt[item7]
        assert dictt['single_e'].get_direct_subordinates() == []
        assert dictt['single_e'].get_all_subordinates() == []
        assert dictt['single_e'].get_superior() == None
        assert dictt['single_l'].get_superior() == None
        assert dictt['single_l'].get_direct_subordinates() == []
        assert dictt['single_l'].get_all_subordinates() == []
        assert not isinstance(dictt['e80'], Leader)
        assert isinstance(dictt[new_name], Leader)
        l=dictt[new_name]
        l1=item
        assert dictt[new_name].name == dictt[item].name
        assert dictt[new_name].salary == dictt[item].salary
        assert dictt[new_name].eid == dictt[item].eid
        assert dictt[new_name].position == dictt[item].position
        assert dictt[new_name].rating == dictt[item].rating
        assert dictt[new_name]._department_name == dictt['l80']._department_name
        assert item not in head.get_all_subordinates()
        assert dictt['l80'].get_direct_subordinates()==[] and dictt['l80'].get_all_subordinates()==[] and dictt['l80'].get_superior() is None
        assert dictt[item].get_direct_subordinates() == [] and dictt[item].get_all_subordinates() == [] and dictt[item].get_superior() is None
        assert dictt[new_name] in head.get_all_subordinates() or dictt[new_name] is head
        assert dictt['e80'].name == dictt['l80'].name
        assert dictt['e80'].salary == dictt['l80'].salary
        assert dictt['e80'].eid == 80
        assert dictt['e80'].position == dictt['l80'].position
        assert dictt['e80'].rating == dictt['l80'].rating
        assert dictt['l80'] not in head.get_all_subordinates()
        assert dictt['e80'] in head.get_all_subordinates()

        assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt[new_name],dictt['e7'], dictt['l82'], dictt['e88']]

        assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l81']]
        assert dictt['l81'].get_direct_subordinates() == [dictt['e38'], dictt['e48'], dictt['l58']]
        for itemm in [dictt['e38'], dictt['e48'], dictt['l58'], dictt['e23']]:
            assert itemm.get_direct_subordinates() == []

        assert dictt['l82'].get_direct_subordinates() == [dictt['l39'], dictt['l83']]
        assert dictt['l83'].get_direct_subordinates() == [dictt['l84'], dictt['l85'], dictt['l86']]
        for itemm in [dictt['l39'], dictt['l84'], dictt['l85'], dictt['l86']]:
            assert itemm.get_direct_subordinates() == []

        assert dictt['e88'].get_direct_subordinates() == [dictt['e41'], dictt['e42'], dictt['e43']]
        assert dictt['e41'].get_direct_subordinates() == [dictt['e51'], dictt['e61']]
        for itemm in [dictt['e51'], dictt['e61'], dictt['e42'], dictt['e43']]:
            assert itemm.get_direct_subordinates() == []

        assert dictt[new_name].get_direct_subordinates() == [dictt['e80']]
        assert dictt[new_name].get_superior() is dictt['l30']
        for item4 in [item2,item3]:
            assert dictt[item4].get_direct_subordinates() == []
            assert dictt[item4].get_all_subordinates()==[]
            assert dictt[item4].get_superior() is dictt['e80']
        assert dictt['e80'].get_direct_subordinates()==[dictt[item2],dictt[item3]]
        assert dictt['e80'].get_superior() is dictt[new_name]

        assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
        for itemm in [dictt['l77'], dictt['l78']]:
            assert itemm.get_direct_subordinates() == []






if __name__ == '__main__':
    import pytest

    pytest.main(['e3_change_department_leader_Test1.py'])
