import numpy as np
import  torch
def test():
    data_numpy = np.array([2,3,4])
    data_tensor1 = torch.from_numpy(data_numpy)
    data_tensor2 = torch.tensor(data_numpy)
    print(type(data_tensor1))
    print(type(data_tensor2))
    data_numpy[0] = 100
    print("data_tensor1-->",data_tensor1)
    print("data_tensor2-->", data_tensor2)
    print("data_numpy-->", data_numpy)

if __name__ == '__main__':
    test()