import torch
import numpy as np


def test01():
    data1 = torch.tensor(10)
    print("=======data1=======")
    print(data1)
    print(type(data1))
    print(data1.type())

    data = np.random.randn(2, 3)
    print("numpy数组类型：", data.dtype)
    data2 = torch.tensor(data)
    print("========data2======")
    print(data2)
    print(data2.type())
    print(data2.dtype)
    data = [[1., 2., 3., ], [4., 5., 6., ]]
    data3 = torch.tensor(data)
    print("========data3=======")
    print(data3)
    print(data3.type())
    print(data3.dtype)


def test02():
    data4 = torch.Tensor(2, 3)
    print("========data4======")
    print(data4)
    print(data4.type())
    print(data4.dtype)
    data5 = torch.Tensor([10])
    print("========data5======")
    print(data5)
    print(data5.type())
    print(data5.dtype)



def test03():
    data6 = torch.IntTensor(2,3)
    print("======data6=====")
    print(data6)
    print(data6.type())
    print(data6.dtype)

    data7 = torch.IntTensor([2.5,3.3])
    print("======data7=====")
    print(data7)
    print(data7.type())
    print(data7.dtype)

    data = torch.ShortTensor()
    print(data)
    data = torch.LongTensor()
    print(data)
    data = torch.HalfTensor()
    print(data)
    #data = torch.FloatType()
    #print(data)
    data = torch.DoubleTensor()
    print(data)


test01()

test02()

test03()