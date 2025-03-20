import torch
def test():
    data1 = torch.randint(0,10,[2,3])
    data2 = torch.randint(0, 10, [2, 3])
    print("data1-->",data1)
    print("data2-->",data2)
    new0_data = torch.stack([data1,data2],dim=0)
    print(new0_data.shape)
    print("new0_data-->",new0_data)
    new1_data = torch.stack([data1,data2],dim=0)
    print(new1_data.shape)
    print("new1_data-->",new1_data)
    new2_data = torch.stack([data1,data2],dim=0)
    print(new2_data.shape)
    print("new2_data-->",new2_data)
if __name__ == '__main__':
    test()