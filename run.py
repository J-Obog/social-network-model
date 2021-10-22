from network import Network

def main():
    net = Network()
    net.add('JDoe63')
    net.add('SJohnson78')
    net.add('DFord99')
    net.link('JDoe63', 'SJohnson78')
    net.link('JDoe63', 'DFord99')
    print(net.friend_list('JDoe63'))

if __name__ == '__main__': 
    main()