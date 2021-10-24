## Network API

The [Network](https://github.com/J-Obog/social-network-model/blob/main/network.py) class contains the following member variables and methods:


### Variables

**capacity** *int* - Maximum amount of users a network can contain (a value of -1 means there is no capacity).

**map** *dict[str, int]* - Keys are the user's name and value is the respective user id

**graph** *List[List[int]]* - Adjacency matrix consisting of the network's edges and vertices

**sparse_queue** *List[int]* - Contains the ids of previously removed users. Used to reduce sparsity in the adjacency matrix when adding a new user

**size** *int* - Represents the length of the adjacency matrix

### Methods
**add**(*user: str) -> None* - Adds `user` to the network

**remove**(*user: str) -> None* - Removes `user` from the network

**update**(*user: str, new_user: str) -> None* - Updates the name of `user`

**link**(*user1: str, user2: str) -> None* - Makes `user1` and `user2` friends 

**friend_list**(*user: str) > List[str]* - Returns a list containing the names of all `user`'s friends

**mutual_friends**(*user1: str, user2: str) -> List[str]* - Returns a list containing the names of all `user`'s mutual friends

**are_friends**(*user1: str, user2: str) -> bool* - Returns `True` if `user1` and `user2` are friends, otherwise `False`.

**are_mutual_friends**(*user1: str, user2: str) -> bool* - Returns `True` if `user1` and `user2` are mutal friends, otherwise `False`