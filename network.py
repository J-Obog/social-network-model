 
class Network:
    def __init__(self, capacity = -1):
        self.__capacity = capacity
        self.__size = 0
        self.__map = {}
        self.__graph = []
        self.__sparse_queue = []  

    """ add new user to the network """
    def add(self, user):
        if self.__map.get(user) != None:
            raise Exception('Username already exists in network')

        if len(self.__sparse_queue) == 0:
            self.__map[user] = self.__size
            
            for i in range(self.__size):
                self.__graph[i].append(0)
            
            self.__graph.append([0] * (self.__size + 1))
        else:
            self.__map[user] = self.__sparse_queue[0]
            self.__sparse_queue.pop(0)
        
        self.__size += 1

    """ remove user from the network """
    def remove(self, user): 
        if self.__map.get(user) == None:
            raise Exception("User doesn't exist in network")

        self.__sparse_queue.append(self.__map[user])
        self.__map.pop(user)
        
    """ change user's name """
    def update(self, user, new_user):
        if self.__map.get(user) == None:
            raise Exception("User doesn't exist in network")

        if self.__map.get(new_user) != None:
            raise Exception('Username already exists in network')

        self.__map[new_user] = self.__map[user]
        self.__map.pop(user)

    """ get list of user's friends """
    def friends(self, user):
        pass

    """ get list of user1 and user2's mutual friends """
    def mutual_friends(self, user1, user2):
        pass
    
    """ check if user1 and user 2 are friends """
    def are_friends(self, user1, user2):
        pass

    """ check if user1 and user2 are mutual friends """
    def are_mutual_friends(self, user1, user2):
        pass