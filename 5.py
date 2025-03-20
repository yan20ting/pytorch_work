import torch

def test():
    data = torch.randint(low = 0,high = 10,size = [2,3])
    print("data-->",data)

    new_data = data.add(10)
    print("new data-->",new_data)

    data.add_(10)
    print("data-->",data)

    print(data.sub(100))

    print(data.mul(100))

    print(data.div(100))

    print(data.neg())




test()