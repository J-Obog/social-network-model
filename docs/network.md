## Network API

The [Network](https://github.com/J-Obog/social-network-model/blob/main/network.py) class contains the following member variables and methods:

`*` denotes a method are member variable that is private


##### Variables

`*capacity: int`

`*size: int` 

`*map: dict[str, int]`

`*graph: List[List[int]]`

`*sparse_queue: List[int]`


##### Methods
`add(user: str) -> None`

`remove(user: str) -> None`

`update(user: str, new_user: str) -> None`

`link(user1: str, user2: str) -> None`

`friend_list(user: str) -> List[str]`

`mutual_friends(user1: str, user2: str) -> List[str]`

`are_friends(user1: str, user2: str) -> bool`