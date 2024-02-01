from __future__ import annotations

from panther import status
from panther.base_websocket import Websocket
from panther.configs import config


class GenericWebsocket(Websocket):
    auth: bool = False
    permissions: list = []

    async def connect(self, **kwargs):
        """
        Check your conditions then `accept()` or `close()` the connection
        """

    async def receive(self, data: str | bytes):
        """
        Received `data` of connection,
        You may want to use json.loads() on the `data`
        """

    async def send(self, data: any = None):
        """
        We are using this method to send message to the client,
        You may want to override it with your custom scenario. (not recommended)
        """
        return await super().send(data=data)


async def send_message_to_websocket(connection_id: str, data: any):
    config.websocket_connections.publish(connection_id=connection_id, action='send', data=data)


async def close_websocket_connection(connection_id: str, code: int = status.WS_1000_NORMAL_CLOSURE, reason: str = ''):
    data = {'code': code, 'reason': reason}
    config.websocket_connections.publish(connection_id=connection_id, action='close', data=data)
