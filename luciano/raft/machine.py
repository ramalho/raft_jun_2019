
from config import TOTAL_SERVERS

class RaftMachine:
    """State machine of a Raft server"""

    def __init__(self, id):
        self.id = id
        self.term = 0
        self.state = Follower

class RaftState:
    pass


class Follower(RaftState):
    pass