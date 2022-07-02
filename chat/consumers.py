"""In this file, we define the consumers for the chat application."""

# Importing libraries
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class PersonalChatConsumer(AsyncWebsocketConsumer):
    """This class defines the consumer for personal chat."""

    async def connect(self):
        """Connect the user to the chat."""
        my_id = self.scope["user"].id

        # kwargs: get the id from websocket url
        other_user_id = self.scope["url_route"]["kwargs"]["id"]

        # Creating a unique group name for the chat
        if int(my_id) > int(other_user_id):
            self.room_name = f"{my_id}-{other_user_id}"
        else:
            self.room_name = f"{other_user_id}-{my_id}"

        self.room_group_name = "chat_%s" % self.room_name

        # fmt: off
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        """Disconnect the user from the chat."""
        # self.channel_layer.group_discard(self.room_group_name,
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_layer)
