import torch


def tset():
    data_tensor = torch.tensor([2, 3, 4])
    data_numpy1 = data_tensor.numpy()
    data_numpy2 = data_tensor.numpy().copy()
    print(type(data_tensor))
    print(type(data_numpy1))
    print(type(data_numpy2))

    data_tensor[0] = 100
    print("data_tensor-->", data_tensor)
    print("data_numpy-->", data_numpy1)
    print("data_numpy2-->", data_numpy2)
