import torch

def test01():
    data1 = torch.zeros(2,3)
    print("data1-->",data1)
    data2 = torch.zeros_like(data1)
    print("data2-->",data2)

def test02():
    data3 = torch.ones(2,3,dtype=torch.int32)
    print("data3-->",data3)
    data4 = torch.ones_like(data3,dtype=torch.float16)
    print("data4-->",data4)

def test03():
    data5 = torch.full([2,3],10)
    print("data5-->",data5)
    data6 = torch.full_like(data5,20)
    print("data6-->",data6)

test01()
test02()
test03()