from config import TOTAL_SERVERS

class RaftMessage:

    def __init__(self, sender, receiver, *args):
        assert sender < TOTAL_SERVERS
        assert receiver < TOTAL_SERVERS
        assert sender != receiver


class AppendEntries(RaftMessage):

    def __init__(self, sender, receiver,
                 term,
                 leader_id,
                 prev_log_index,
                 prev_log_term,
                 entries,
                 leader_commit):
        super().__init__(sender, receiver)
        self.term = term
        self.leader_id = leader_id
        self.prev_log_index = prev_log_index
        self.prev_log_term = prev_log_term
        self.entries = entries
        self.leader_commit = leader_commit

class AppendEntries(RaftMessage):

    def __init__(self, sender, receiver,
                 term,
                 success):
        super().__init__(sender, receiver)
        self.term = term
        self.success = success
