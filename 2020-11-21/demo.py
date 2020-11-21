import sys
import asyncio

from sanic import Sanic
from sanic.websocket import WebSocketProtocol
from websockets import (  # type: ignore
    InvalidHandshake,
    WebSocketCommonProtocol,
    handshake,
)

from sanic.exceptions import InvalidUsage
from websockets.framing import serialize_close

app = Sanic("websocket_example")


class MyWebSocketCommonProtocol(WebSocketCommonProtocol):
    async def close(self, code: int = 1000, reason: str = "") -> None:
        try:
            await asyncio.wait_for(
                self.write_close_frame(serialize_close(code, reason)),
                self.close_timeout,
                loop=self.loop if sys.version_info[:2] < (3, 8) else None,
            )
        except asyncio.TimeoutError:
            # If the close frame cannot be sent because the send buffers
            # are full, the closing handshake won't complete anyway.
            # Fail the connection to shut down faster.
            self.fail_connection()

        # If no close frame is received within the timeout, wait_for() cancels
        # the data transfer task and raises TimeoutError.

        # If close() is called multiple times concurrently and one of these
        # calls hits the timeout, the data transfer task will be cancelled.
        # Other calls will receive a CancelledError here.

        try:
            # If close() is canceled during the wait, self.transfer_data_task
            # is canceled before the timeout elapses.
            await asyncio.wait_for(
                self.transfer_data_task,
                self.close_timeout,
                loop=self.loop if sys.version_info[:2] < (3, 8) else None,
            )
        except (asyncio.TimeoutError, asyncio.CancelledError):
            pass

        print("hhhh close")
        # Wait for the close connection task to close the TCP connection.
        await asyncio.shield(self.close_connection_task)


class MyWebSocketProtocol(WebSocketProtocol):
    async def websocket_handshake(self, request, subprotocols=None):
        # let the websockets package do the handshake with the client
        headers = {}

        try:
            key = handshake.check_request(request.headers)
            handshake.build_response(headers, key)
        except InvalidHandshake:
            raise InvalidUsage("Invalid websocket request")

        subprotocol = None
        if subprotocols and "Sec-Websocket-Protocol" in request.headers:
            # select a subprotocol
            client_subprotocols = [
                p.strip()
                for p in request.headers["Sec-Websocket-Protocol"].split(",")
            ]
            for p in client_subprotocols:
                if p in subprotocols:
                    subprotocol = p
                    headers["Sec-Websocket-Protocol"] = subprotocol
                    break

        # write the 101 response back to the client
        rv = b"HTTP/1.1 101 Switching Protocols\r\n"
        for k, v in headers.items():
            rv += k.encode("utf-8") + b": " + v.encode("utf-8") + b"\r\n"
        rv += b"\r\n"
        request.transport.write(rv)

        # hook up the websocket protocol
        self.websocket = MyWebSocketCommonProtocol(
            close_timeout=self.websocket_timeout,
            max_size=self.websocket_max_size,
            max_queue=self.websocket_max_queue,
            read_limit=self.websocket_read_limit,
            write_limit=self.websocket_write_limit,
            ping_interval=self.websocket_ping_interval,
            ping_timeout=self.websocket_ping_timeout,
        )
        # Following two lines are required for websockets 8.x
        self.websocket.is_client = False
        self.websocket.side = "server"
        self.websocket.subprotocol = subprotocol
        self.websocket.connection_made(request.transport)
        self.websocket.connection_open()
        return self.websocket


@app.websocket('/feed')
async def feed(request, ws: WebSocketCommonProtocol):
    data = 'hello!'
    print('Sending: ' + data)
    i = 0
    while True:
        await ws.send(data)

        data = await ws.recv()
        print('Received: ' + data)
        i = i + 1
        if i > 3:
            raise EOFError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, protocol=MyWebSocketProtocol)
