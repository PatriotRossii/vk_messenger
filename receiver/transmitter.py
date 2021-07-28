import zmq

class Transmitter:
    def __init__(self, host: str, port: int):
        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{host}:{port}")

    def send_conversations(self, conversations):
        self.socket.send(b"START_CONVERSATIONS")
        for conversation in conversations:
            self.socket.send(bytes(str(conversation)), encoding="utf-8")
        self.socket.send(b"END_CONVERSATIONS")
