from network import Network

def main():
    net = Network()

    # adding users to network
    net.add('JDoe63')
    net.add('SJohnson78')
    net.add('DFord99')

    # 'friending' two users
    net.link('JDoe63', 'SJohnson78')
    net.link('DFord99', 'SJohnson78') 

    # testing out Network API
    print(f"DFord99 and JDoe63 are mutual friends: {net.are_mutual_friends('DFord99', 'JDoe63')}")
    print(f"JDoe63's friend list: {net.friend_list('JDoe63')}")
    net.update("JDoe63", "JDoeSixThree")
    print(f"SJohnson78's friend list: {net.friend_list('SJohnson78')}")

if __name__ == '__main__': 
    main()