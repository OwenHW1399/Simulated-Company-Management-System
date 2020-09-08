from organization_hierarchy import Employee, Leader, merge
from typing import List
from e1_Sample_Non_Mutating_Test import increasing, increasing_salary, no_duplicate


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

    dictt = {}
    lst = [L30]
    lst.extend(L30.get_all_subordinates())
    for item in lst:
        dictt[item.name] = item
    dictt["single_e"] = single_e
    dictt["single_l"] = single_l
    return dictt

def test_single_node():
    dictt=generate()
    assert dictt["single_e"].swap_up()==dictt['single_e']
    assert dictt['single_l'].swap_up()==dictt['single_l']
def test_swap():
    for item in ['e3', 'e4', 'e5', 'e6', 'e7', 'e23', 'e38', 'l39', 'e41', 'e42', 'e43', 'e48', 'e51', 'l58',
                 'e61', 'l77',
                 'l78', 'l80', 'l81',
                  'l82', 'l83', 'l84', 'l85', 'l86', 'e88']:
    #not gonna test l30 since precondition of swap_up
    #more check single node
        dictt = generate()
        if isinstance(dictt[item], Leader) and isinstance(dictt[item].get_superior(), Leader):
            old_sup = dictt[item].get_superior()
            old_sub = dictt[item]
            old_sub_sub = dictt[item].get_direct_subordinates()
            old_sub_sub2 = dictt[item].get_all_subordinates()
            old_sup_sub = old_sup.get_direct_subordinates()
            old_sup_sub2 = old_sup.get_all_subordinates()
            old_sub_name = dictt[item].name
            old_sup_name = dictt[item].get_superior().name
            old_sub_id = dictt[item].eid
            old_sup_id = dictt[item].get_superior().eid
            new_sup = dictt[item].swap_up()
            assert isinstance(new_sup, Leader)
            new_sub = new_sup.get_organization_head().get_employee(old_sup_id)
            assert new_sub in new_sup.get_direct_subordinates()
            assert new_sub.get_superior() is new_sup
            assert  isinstance(new_sub, Leader)
            assert (new_sup is not old_sub) and (old_sup is not new_sup)
            assert old_sub.get_all_subordinates() == [] and old_sub.get_direct_subordinates() == []
            assert old_sub.get_superior() is None
            assert old_sup.get_all_subordinates() == [] and old_sup.get_direct_subordinates() == []
            assert old_sup.get_superior() is None
            assert old_sup._department_name == new_sup.get_department_name()
            assert old_sup.position == new_sup.position
            assert old_sup.salary == new_sup.salary
            assert old_sup.eid == new_sub.eid
            assert old_sup.name == new_sub.name
            assert old_sup.rating == new_sub.rating
            assert old_sub._department_name == new_sub.get_department_name()
            assert old_sub.position == new_sub.position
            assert old_sub.salary == new_sub.salary
            assert old_sub.eid == new_sup.eid
            assert old_sub.name == new_sup.name
            assert old_sub.rating == new_sup.rating
            dictt[old_sub_name]=new_sub   #more did a little something here, write more clear tests
            dictt[old_sup_name]=new_sup
            new_sub.eid=old_sub_id
            new_sup.eid=old_sup_id

        elif (not isinstance(dictt[item],Leader)) and isinstance(dictt[item].get_superior(), Leader):
            old_sup = dictt[item].get_superior()
            old_sub = dictt[item]
            old_sub_sub = dictt[item].get_direct_subordinates()
            old_sub_sub2 = dictt[item].get_all_subordinates()
            old_sup_sub = old_sup.get_direct_subordinates()
            old_sup_sub2 = old_sup.get_all_subordinates()
            old_sub_name = dictt[item].name
            old_sup_name = dictt[item].get_superior().name
            old_sub_id = dictt[item].eid
            old_sup_id = dictt[item].get_superior().eid
            new_sup = dictt[item].swap_up()
            assert  isinstance(new_sup, Leader)
            new_sub = new_sup.get_organization_head().get_employee(old_sup_id)
            assert new_sub in new_sup.get_direct_subordinates()
            assert new_sub.get_superior() is new_sup
            assert not isinstance(new_sub, Leader)
            assert (new_sup is not old_sub) and (old_sup is not new_sub)
            assert old_sub.get_all_subordinates() == [] and old_sub.get_direct_subordinates() == []
            assert old_sub.get_superior() is None
            # more check get_all_sub() in T1 to T3 where you checked get_dirct
            assert old_sup.get_all_subordinates() == [] and old_sup.get_direct_subordinates() == []
            assert old_sup.get_superior() is None
            assert old_sup._department_name == new_sup.get_department_name()
            assert old_sup.position == new_sup.position
            assert old_sup.salary == new_sup.salary
            assert old_sup.eid == new_sub.eid
            assert old_sup.name == new_sub.name
            assert old_sup.rating == new_sub.rating
            assert old_sub.position == new_sub.position
            assert old_sub.salary == new_sub.salary
            assert old_sub.eid == new_sup.eid
            assert old_sub.name == new_sup.name
            assert old_sub.rating == new_sup.rating
            dictt[old_sub_name] = new_sub
            dictt[old_sup_name] = new_sup
            new_sub.eid = old_sub_id
            new_sup.eid = old_sup_id

        elif (isinstance(dictt[item], Leader)) and (not isinstance(dictt[item].get_superior(), Leader)):
            old_sup = dictt[item].get_superior()
            old_sub = dictt[item]
            old_sub_sub = dictt[item].get_direct_subordinates()
            old_sub_sub2 = dictt[item].get_all_subordinates()
            old_sup_sub = old_sup.get_direct_subordinates()
            old_sup_sub2 = old_sup.get_all_subordinates()
            old_sub_name = dictt[item].name
            old_sup_name = dictt[item].get_superior().name
            old_sub_id = dictt[item].eid
            old_sup_id = dictt[item].get_superior().eid
            new_sup = dictt[item].swap_up()
            assert not isinstance(new_sup, Leader)
            new_sub = new_sup.get_organization_head().get_employee(old_sup_id)
            assert new_sub in new_sup.get_direct_subordinates()
            assert new_sub.get_superior() is new_sup
            assert  isinstance(new_sub, Leader)
            assert (new_sup is not old_sub) and (old_sup is not new_sub)
            assert old_sub.get_all_subordinates() == [] and old_sub.get_direct_subordinates() == []
            assert old_sub.get_superior() is None
            # more check get_all_sub() in T1 to T3 where you checked get_dirct
            assert old_sup.get_all_subordinates() == [] and old_sup.get_direct_subordinates() == []
            assert old_sup.get_superior() is None
            assert old_sub._department_name == new_sub.get_department_name()
            assert old_sup.position == new_sup.position
            assert old_sup.salary == new_sup.salary
            assert old_sup.eid == new_sub.eid
            assert old_sup.name == new_sub.name
            assert old_sup.rating == new_sub.rating
            assert old_sub.position == new_sub.position
            assert old_sub.salary == new_sub.salary
            assert old_sub.eid == new_sup.eid
            assert old_sub.name == new_sup.name
            assert old_sub.rating == new_sup.rating
            dictt[old_sub_name] = new_sub
            dictt[old_sup_name] = new_sup
            new_sub.eid = old_sub_id
            new_sup.eid = old_sup_id
        else:
            old_sup = dictt[item].get_superior()
            old_sub = dictt[item]
            old_sub_sub = dictt[item].get_direct_subordinates()
            old_sub_sub2 = dictt[item].get_all_subordinates()
            old_sup_sub = old_sup.get_direct_subordinates()
            old_sup_sub2 = old_sup.get_all_subordinates()
            old_sub_name = dictt[item].name
            old_sup_name = dictt[item].get_superior().name
            old_sub_id = dictt[item].eid
            old_sup_id = dictt[item].get_superior().eid
            new_sup = dictt[item].swap_up()
            assert not isinstance(new_sup, Leader)
            new_sub = new_sup.get_organization_head().get_employee(old_sup_id)
            assert new_sub in new_sup.get_direct_subordinates()
            assert new_sub.get_superior() is new_sup
            assert not  isinstance(new_sub, Leader)
            assert (new_sup is not old_sub) and (old_sup is not new_sub)
            assert old_sub.get_all_subordinates() == [] and old_sub.get_direct_subordinates() == []
            assert old_sub.get_superior() is None
            # more check get_all_sub() in T1 to T3 where you checked get_dirct
            assert old_sup.get_all_subordinates() == [] and old_sup.get_direct_subordinates() == []
            assert old_sup.get_superior() is None
            #assert old_sub._department_name == new_sub.get_department_name()
            assert old_sup.position == new_sup.position
            assert old_sup.salary == new_sup.salary
            assert old_sup.eid == new_sub.eid
            assert old_sup.name == new_sub.name
            assert old_sup.rating == new_sub.rating
            assert old_sub.position == new_sub.position
            assert old_sub.salary == new_sub.salary
            assert old_sub.eid == new_sup.eid
            assert old_sub.name == new_sup.name
            assert old_sub.rating == new_sup.rating
            dictt[old_sub_name] = new_sub
            dictt[old_sup_name] = new_sup
            new_sub.eid = old_sub_id
            new_sup.eid = old_sup_id
        assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                              dictt['e88']]

        assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l81']]
        assert dictt['l81'].get_direct_subordinates() == [dictt['e38'], dictt['e48'], dictt['l58']]
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
def test_38_48():
    for item in ['e38','e48']:
        dictt=generate()
        sub=dictt[item]
        assert dictt[item].get_superior()==dictt['l81']
        sup=dictt['l81']
        name_sup=sup.name
        rating_sup=sup.rating
        department=sup.get_department_name()
        salary_sup=sup.salary
        position_sup=sup.position
        name_sub = sub.name
        rating_sub = sub.rating
        salary_sub = sub.salary
        position_sub = sub.position
        new_sup=sub.swap_up()
        new_sub=None
        for item2 in new_sup.get_direct_subordinates():
            if item2.eid==81:
                new_sub=item2
                break
        assert new_sub is not None
        assert not isinstance(new_sub,Leader)
        assert new_sup.get_organization_head().get_employee(81) is new_sub
        assert isinstance(new_sup,Leader)
        assert sub.get_direct_subordinates()==[] and sub.get_all_subordinates()==[] and sub.get_superior() is  None
        assert sup.get_direct_subordinates() == [] and sup.get_all_subordinates() == [] and sup.get_superior() is None
        assert new_sup.salary==sup.salary
        assert new_sub.salary==sub.salary
        assert new_sup.position == sup.position
        assert new_sub.position == sub.position
        for i in [(sub,new_sup),(sup,new_sub)]:
            assert i[0].name==i[1].name
            assert i[0].eid==i[1].eid
            assert i[0].rating==i[1].rating
        assert new_sup.get_department_name()=='B'

        assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], dictt['l82'],
                                                          dictt['e88']]

        assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], new_sup]
        if item=='e38':
            assert new_sup.get_direct_subordinates() == [ dictt['e48'], dictt['l58'],new_sub]
            for item2 in [dictt['e48'], dictt['l58'], dictt['e23'],new_sub]:
                assert item2.get_direct_subordinates() == []
        else:
            assert new_sup.get_direct_subordinates() == [dictt['e38'], dictt['l58'], new_sub]
            for item2 in [dictt['e38'], dictt['l58'], dictt['e23'], new_sub]:
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
def test_e51_e61():
    for item in ['e51','e61']:
        dictt=generate()
        sub=dictt[item]
        assert dictt[item].get_superior()==dictt['e41']
        sup=dictt['e41']
        name_sup=sup.name
        rating_sup=sup.rating
        department=sup.get_department_name()
        salary_sup=sup.salary
        position_sup=sup.position
        name_sub = sub.name
        rating_sub = sub.rating
        salary_sub = sub.salary
        position_sub = sub.position
        new_sup=sub.swap_up()
        new_sub=None
        for item2 in new_sup.get_direct_subordinates():
            if item2.eid==41:
                new_sub=item2
                break
        assert new_sub is not None
        assert not isinstance(new_sub,Leader)
        assert new_sup.get_organization_head().get_employee(41) is new_sub
        assert not isinstance(new_sup,Leader)
        assert sub.get_direct_subordinates()==[] and sub.get_all_subordinates()==[] and sub.get_superior() is  None
        assert sup.get_direct_subordinates() == [] and sup.get_all_subordinates() == [] and sup.get_superior() is None
        assert new_sup.salary==sup.salary
        assert new_sub.salary==sub.salary
        assert new_sup.position == sup.position
        assert new_sub.position == sub.position
        for i in [(sub,new_sup),(sup,new_sub)]:
            assert i[0].name==i[1].name
            assert i[0].eid==i[1].eid

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

        assert dictt['e88'].get_direct_subordinates() == [dictt['e42'], dictt['e43'],new_sup]
        if new_sup.eid==51:
            assert new_sup.get_direct_subordinates() == [new_sub, dictt['e61']]
            for item in [new_sub, dictt['e61'], dictt['e42'], dictt['e43']]:
                assert item.get_direct_subordinates() == []
        else:
            assert new_sup.eid==61
            assert new_sup.get_direct_subordinates() == [new_sub, dictt['e51']]
            for item in [new_sub, dictt['e51'], dictt['e42'], dictt['e43']]:
                assert item.get_direct_subordinates() == []

        assert dictt['l80'].get_direct_subordinates() == [dictt['e4'], dictt['e5'], dictt['e6']]
        for item in [dictt['e4'], dictt['e5'], dictt['e6']]:
            assert item.get_direct_subordinates() == []

        assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
        for item in [dictt['l77'], dictt['l78']]:
            assert item.get_direct_subordinates() == []
def test_L81():
    dictt = generate()
    sub = dictt['l81']
    assert dictt['l81'].get_superior() == dictt['e3']
    sup = dictt['e3']
    name_sup = sup.name
    rating_sup = sup.rating
    department = sup.get_department_name()
    salary_sup = sup.salary
    position_sup = sup.position
    name_sub = sub.name
    rating_sub = sub.rating
    salary_sub = sub.salary
    position_sub = sub.position
    new_sup = sub.swap_up()
    new_sub = None
    for item2 in new_sup.get_direct_subordinates():
        if item2.eid == 3:
            new_sub = item2
            break
    assert new_sub is not None
    assert isinstance(new_sub, Leader)
    assert not isinstance(new_sup,Leader)
    assert new_sup.get_organization_head().get_employee(3) is new_sub
    assert sub.get_direct_subordinates() == [] and sub.get_all_subordinates() == [] and sub.get_superior() is None
    assert sup.get_direct_subordinates() == [] and sup.get_all_subordinates() == [] and sup.get_superior() is None
    assert new_sup.salary == sup.salary
    assert new_sub.salary == sub.salary
    assert new_sup.position == sup.position
    assert new_sub.position == sub.position
    assert new_sup.eid==81
    assert new_sub.eid==3
    assert new_sub._department_name=='B'
    for i in [(sub, new_sup), (sup, new_sub)]:
        assert i[0].name == i[1].name
        assert i[0].eid == i[1].eid
    assert dictt['l30'].get_direct_subordinates() == [ dictt['e7'], dictt['l80'],new_sup,dictt['l82'],
                                                      dictt['e88']]

    assert new_sup.get_direct_subordinates() == [new_sub,dictt['e23']]
    assert new_sub.get_direct_subordinates() == [dictt['e38'], dictt['e48'], dictt['l58']]
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
def test_L83():
    dictt = generate()
    sub = dictt['l83']
    assert dictt['l83'].get_superior() == dictt['l82']
    sup = dictt['l82']
    name_sup = sup.name
    rating_sup = sup.rating
    department = sup.get_department_name()
    salary_sup = sup.salary
    position_sup = sup.position
    name_sub = sub.name
    rating_sub = sub.rating
    salary_sub = sub.salary
    position_sub = sub.position
    new_sup = sub.swap_up()
    new_sub = None
    for item2 in new_sup.get_direct_subordinates():
        if item2.eid == 82:
            new_sub = item2
            break
    assert new_sub is not None
    assert isinstance(new_sub, Leader)
    assert isinstance(new_sup, Leader)
    assert new_sup.get_organization_head().get_employee(82) is new_sub
    assert sub.get_direct_subordinates() == [] and sub.get_all_subordinates() == [] and sub.get_superior() is None
    assert sup.get_direct_subordinates() == [] and sup.get_all_subordinates() == [] and sup.get_superior() is None
    assert new_sup.salary == sup.salary
    assert new_sub.salary == sub.salary
    assert new_sup.position == sup.position
    assert new_sub.position == sub.position
    assert new_sup.eid == 83
    assert new_sub.eid == 82
    assert new_sub._department_name == 'D'
    assert new_sup._department_name == 'A'
    for i in [(sub, new_sup), (sup, new_sub)]:
        assert i[0].name == i[1].name
        assert i[0].eid == i[1].eid
    assert dictt['l30'].get_direct_subordinates() == [dictt['e3'], dictt['e7'], dictt['l80'], new_sup,
                                                      dictt['e88']]

    assert dictt['e3'].get_direct_subordinates() == [dictt['e23'], dictt['l81']]
    assert dictt['l81'].get_direct_subordinates() == [dictt['e38'], dictt['e48'], dictt['l58']]
    for item in [dictt['e38'], dictt['e48'], dictt['l58'], dictt['e23']]:
        assert item.get_direct_subordinates() == []

    assert new_sup.get_direct_subordinates() == [dictt['l39'],new_sub]
    assert new_sub.get_direct_subordinates() == [dictt['l84'], dictt['l85'], dictt['l86']]
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
if __name__ == '__main__':
    import pytest

    pytest.main(['e4_swap_sample_test.py'])
