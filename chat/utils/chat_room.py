import uuid
from collections import defaultdict


class ChatRoom:
    def __init__(self):
        self.room_id = str(uuid.uuid4())
        self.client = defaultdict(list)

    def add_message_stream(self, key, value):
        self.client[key].append(value)

    def __str__(self):
        return (
        f"Chat Room id: {self.room_id}, "
        f"Clients={list(self.client.keys())}"
    )

    def add_client(self, client_id):
        if client_id not in self.client:
            self.client[client_id] = []

    def remove_client(self, client_id):
        if client_id in self.client:
            del self.client[client_id]
