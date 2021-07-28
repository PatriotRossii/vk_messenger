import vk

import conversation

class ConversationsHelper:
    def __init__(self, api: vk.API):
        self.api = api

    def get(self, count: int):
        conversations = []

        response = self.api.messages.searchConversations(
            count=count, extended=True, v=5.131
        )

        items = response["items"]
        profile = response["profiles"] if "profiles" in response else []
        groups = response["groups"] if "groups" in response else []

        for item in items:
            peer_id = item["id"]
            local_id = item["local_id"]

            type = item["type"]

            title = "unknown"

            if type == "user":
                profile = [profile for profile in profiles if profile["id"] == peer_id][0]
                title = "{} {}".format(
                    profile["first_name"], profile["last_name"]
                )
            elif type == "chat":
                title = item["chat_settings"]["title"]
            elif type == "group":
                group = [group for group in groups if group["id"] == local_id]
                title = group["name"]

            conversations.append(conversation.Conversation(peer_id, title))

        return conversations
