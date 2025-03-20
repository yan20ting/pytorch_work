import torch

def test01():
    data1 = torch.full([2,3],10)
    print("data1-->",data1)
    print(data1.dtype)
    data2 = (data1.type(dtype=torch.DoubleTensor))
    print("data2-->",data2)
    print(data2.dtype)
    data3 = data1.double()
    print("data3-->",data3)
    print(data3.dtype)

test01()











