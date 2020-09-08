from organization_hierarchy import Employee, Leader, merge
from typing import List
from e1_Sample_Non_Mutating_Test import increasing, increasing_salary, no_duplicate
#######

#this tree changes a liite bit
# changed rating of L82
# changed ratinf of e3
# changed rating of L39
# find change comment

#######
def generate():
    e3 = Employee(3, 'e3', 'E3', 3999, 89) #change
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

    L82 = Leader(82, 'l82', 'L82-A', 4567, 90, 'A') #change
    L83 = Leader(83, 'l83', 'L83-D', 4557, 90, 'D')
    L84 = Leader(84, 'l84', 'L82-F', 4367, 29, 'F')
    L85 = Leader(85, 'l85', 'L82-G', 4597, 29, 'G')
    L86 = Leader(86, 'l86', 'L82-H', 2567, 31, 'H')
    L39 = Leader(39, 'l39', 'L39-E', 2562, 77, 'E')#change
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
def test():
    dictt=generate()
    #more test examples, be careful we change the standard tree here see header comment
    # more test if the result is the same for different order in the same subodinate list
    assert dictt['e4'].obtain_subordinates([30,3,82,83,41])==dictt['l80']
    assert dictt['l80'].get_direct_subordinates()==[dictt['e4'],dictt['e5'],dictt['e6'],dictt['e7'],dictt['e23'],dictt['l39'],dictt['l81'],
                                                    dictt['l84'],dictt['l85'],dictt['l86'],dictt['e88']]
    for item in dictt['l80'].get_direct_subordinates():
        assert item.get_superior()==item.get_organization_head()==dictt['l80']
    assert dictt['l80'].get_superior() is None
    assert dictt['e4'].get_direct_subordinates()==[dictt['e3'],dictt['l30'],dictt['e41'],dictt['l82'],dictt['l83']]
    for item in [dictt['e3'],dictt['l30'],dictt['e41'],dictt['l82'],dictt['l83']]:
        assert item.get_superior() is dictt['e4']
        assert item.get_organization_head() is dictt['l80']
        #more the 2 test below is lacking in some other test files
        #find them
        assert item.get_direct_subordinates()==[]
        assert item.get_all_subordinates()==[]
    for item in [dictt['e5'],dictt['e6'],dictt['e23'],dictt['l84'],dictt['l85'],dictt['l86'],dictt['l39']]:
        assert item.get_all_subordinates() ==[]
        assert item.get_direct_subordinates()==[]
        assert item.get_superior()==dictt['l80']
    assert dictt['l81'].get_direct_subordinates()==[dictt['e38'],dictt['e48'],dictt['l58']]
    for item in [dictt['e38'],dictt['e48'],dictt['l58']]:
        assert item.get_all_subordinates() == []
        assert item.get_direct_subordinates() == []
        assert item.get_superior() == dictt['l81']
        assert item.get_organization_head()==dictt['l80']
    assert dictt['e88'].get_direct_subordinates() == [dictt['e42'], dictt['e43'], dictt['e51'],dictt['e61']]
    for item in [dictt['e42'], dictt['e43'], dictt['e51'],dictt['e61']]:
        assert item.get_all_subordinates() == []
        assert item.get_direct_subordinates() == []
        assert item.get_superior() == dictt['e88']
        assert item.get_organization_head() == dictt['l80']
    assert dictt['e7'].get_direct_subordinates() == [dictt['l77'], dictt['l78']]
    for item in [dictt['l77'], dictt['l78']]:
        assert item.get_all_subordinates() == []
        assert item.get_direct_subordinates() == []
        assert item.get_superior() == dictt['e7']
        assert item.get_organization_head() == dictt['l80']
def test_single_node():
    #single_e = Employee(55, "single", 'single_pos', 4, 7)
    #single_l = Leader(55, "single", 'single_pos', 4, 7, 'No one cares')
    lst_id = []
    lst_id2 = []
    for i in range(1,55):
        lst_id.append(i)
    for ii in range(56,101):
        lst_id2.append(ii)
    for item in [lst_id2,lst_id]:
        dictt=generate()
        headl=dictt['single_l'].obtain_subordinates(item)
        heade = dictt['single_e'].obtain_subordinates(item)
        assert headl is dictt['single_l']
        assert heade is dictt['single_e']
        assert headl.get_direct_subordinates()==[] and headl.get_all_subordinates()==[] and headl.get_superior() is None
        assert heade.get_direct_subordinates() == [] and heade.get_all_subordinates() == [] and heade.get_superior() is None
        assert headl.eid==55 and headl.name=='single' and headl.position=='single_pos' and headl.salary==4 and headl.rating==7 and headl.get_department_name()=='No one cares'
        assert heade.eid == 55 and heade.name == 'single' and heade.position == 'single_pos' and heade.salary == 4 and heade.rating == 7
    #dictt['single_l'].obtain_subordinates()
def test_order_simpler_tree():
    L1 = Leader(1, 'l82', 'L82-A', 4567, 1, 'A')  # change
    L2 = Leader(2, 'l83', 'L83-D', 4557, 2, 'D')
    L3 = Leader(3, 'l84', 'L82-F', 4367, 2, 'F')
    L4 = Leader(4, 'l85', 'L82-G', 4597, 1, 'G')
    L5 = Leader(5, 'l86', 'L82-H', 2567, 7, 'H')
    L6 = Leader(6, 'l39', 'L39-E', 2562, 7, 'E')# change
    L10 = Leader(10, 'l39', 'L39-E', 2562, 1, 'E')# change
    for item in [L2,L3,L4]:
        item.become_subordinate(L1)
    L10.become_subordinate(L2)
    for item in [L5,L6]:
        item.become_subordinate(L3)
    #L10.obtain_subordinates([1,99,98,90,3])
    L10.obtain_subordinates([1,3])
    for item in [L6,L2,L3,L4,L5,L1,L10]:
        assert item.get_organization_head()==L2
        if item in [L1,L3]:
            assert item.get_superior()==L10
        elif item==L2:
            assert item.get_superior() is None
        else:
            assert item.get_superior()==L2
        if item in [L4,L5,L6,L1,L3]:
            assert item.get_direct_subordinates()==[]
            assert item.get_all_subordinates()==[]
        elif item==L2:
            assert item.get_direct_subordinates()==[L4,L5,L6,L10]
            assert item.get_all_subordinates()==[L1,L3,L4,L5,L6,L10]
        else:
            assert item is L10
            assert item.get_all_subordinates()==item.get_direct_subordinates()==[L1,L3]
def test_order_simpler_tree2():
    L1 = Leader(1, 'l82', 'L82-A', 4567, 1, 'A')  # change
    L2 = Leader(2, 'l83', 'L83-D', 4557, 2, 'D')
    L3 = Leader(3, 'l84', 'L82-F', 4367, 2, 'F')
    L4 = Leader(4, 'l85', 'L82-G', 4597, 1, 'G')
    L5 = Leader(5, 'l86', 'L82-H', 2567, 7, 'H')
    L6 = Leader(6, 'l39', 'L39-E', 2562, 7, 'E')# change
    L10 = Leader(10, 'l39', 'L39-E', 2562, 1, 'E')# change
    for item in [L2,L3,L4]:
        item.become_subordinate(L1)
    L10.become_subordinate(L2)
    for item in [L5,L6]:
        item.become_subordinate(L3)
    #L10.obtain_subordinates([3,99,98,90,1])
    L10.obtain_subordinates([3,1])
    for item in [L6,L2,L3,L4,L5,L1,L10]:
        head=item.get_organization_head()
        assert item.get_organization_head() is L5
        if item in [L1,L3]:
            assert item.get_superior() is L10
        elif item is L5:
            assert item.get_superior() is None
        elif item is L10:
            assert item.get_superior() is L2
        else:
            assert item.get_superior() is L5
        if item in [L4,L6,L1,L3]:
            assert item.get_direct_subordinates()==[]
            assert item.get_all_subordinates()==[]
        elif item is L5 :
            assert item.get_direct_subordinates()==[L2,L4,L6]
            assert item.get_all_subordinates()==[L1,L2,L3,L4,L6,L10]
        elif item is L2:
            assert item.get_direct_subordinates() == [L10]
            assert item.get_all_subordinates() == [L1,L3, L10]
        else:
            assert item is L10
            assert item.get_all_subordinates()==item.get_direct_subordinates()==[L1,L3]


if __name__ == '__main__':
    import pytest

    pytest.main(['e4_obtain_employee_test.py'])
