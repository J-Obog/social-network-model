 
class Network:
    def __init__(self, capacity = -1):
        self.__capacity = capacity
        self.__size = 0
        self.__map = {}
        self.__graph = []
        self.__sparse_queue = []  

    """ add new user to the network """
    def add(self, user): 
        pass

    """ remove user from the network """
    def remove(self, remove): 
        pass

    """ change user's name """
    def update(self, user, new_user):
        pass

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