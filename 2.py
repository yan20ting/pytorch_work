import torch

def test01():
    data1 = torch.arange(0,10,2)
    print("data1-->",data1)

    data2 = torch.linspace(0,9,10)
    print("data2-->",data2)
    data3 = torch.logspace(0,9,10, base=2)
    print("data3-->",data3)

def test02():
    data4 = torch.randn(2,3)
    print("data4-->",data4)
    print("随机数种子是：",torch.random.initial_seed())
    torch.random.manual_seed(100)
    data5 = torch.randn(2,3)
    print("data5-->",data5)
    print("随机数种子是：",torch.random.initial_seed())

test01()
test02()

