"""In this file, we define the consumers for the chat application."""

# Importing libraries
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class PersonalChatConsumer(AsyncWebsocketConsumer):
    """This class defines the consumer for personal chat."""

    async def connect(self):
        """This method is called when a user is connected to the chat."""
        pass
