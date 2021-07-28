class Conversation:
    def __init__(self, peer_id, title):
        self.peer_id = peer_id
        self.title = title

    def peer_id(self) -> str:
        return self.peer_id

    def title(self) -> str:
        return self.title
