import torch

def test():
    data1 = torch.tensor([[1, 2], [3, 4]])
    data2 = torch.tensor([[5, 6], [7, 8]])


    # 方式一: mul()
    data = torch.mul(data1, data2)
    print(data)
    print('-'*50)
    # 方式二: *
    data = data1 * data2
    print(data)
    print('-'*50)

    # 两个张量之间进行相加
    print(torch.add(data1, data2))


def test02():
    data1 = torch.randn(3, 4, 5)
    data2 = torch.randn(5, 4)
    print("=" * 50)
    print(data1, data1.shape)
    print(data2, data2.shape)
    data3 = torch.matmul(data1, data2)
    print(data3, data3.shape)


def test03():
    print("=" * 50)
    data1 = torch.randn(3,4,5)
    data2 = torch.randn(3,5,8)
    print(data1,data1.shape)
    print(data2,data2.shape)
    data3 = torch.bmm(data1,data2)
    print(data3,data3.shape)


test()

test02()

test03()