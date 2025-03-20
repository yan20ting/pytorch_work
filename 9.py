import torch


def test():
    data1 = torch.randint(0, 10, [1, 2, 3])
    data2 = torch.randint(0, 10, [1, 2, 3])
    print("data1-->", data1)
    print("data2-->", data2)

    new0_data = torch.cat([data1, data2], dim=0)
    print("new0_data-->", new0_data)
    new1_data = torch.cat([data1, data2], dim=1)
    print("new1_data-->", new1_data)
    new2_data = torch.cat([data1, data2], dim=2)
    print("new2_data-->", new2_data)


test()