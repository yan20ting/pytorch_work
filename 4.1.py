import torch


def test01():
    data1 = torch.randint(1, 10, [4, 5])
    print("data1-->", data1)
    print(data1[0])
    print(data1[:, 0])
    print(data1[[0, 1], [1, 2]])
    print(data1[:3, :2])
    print(data1[1:, :2])
    print(data1[:, 2] > 5)
    print(data1[data1[:, 2] > 5])
    print(data1[1] > 5)
    print(data1[:, data1[1] > 5])


def test02():
    data2 = torch.randint(0, 10, [3, 4, 5])
    print("data2-->", data2)
    print(data2[0, :, :])
    print(data2[:, 0, :])
    print(data2[:, :, 0])






test01()
