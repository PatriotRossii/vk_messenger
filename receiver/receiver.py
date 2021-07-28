import vk

import get_conversations

class Receiver:
    def __init__(self, access_token: str):
        session = vk.Session(access_token=access_token)

        self.api = vk.API(session)
        self.conversations_helper = get_conversations.ConversationsHelper(
            self.api
        )

    def conversations(self):
        conversations = self.conversations_helper.get(5)
        return conversations
