import azure.functions as func
import logging
import json

# Store the connected clients
connected_clients = set()

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    # Handle HTTP requests as usual

    # ...

    # Handle WebSocket requests
    if 'Upgrade' in req.headers.get('Connection', '') and \
       req.headers.get('Upgrade', '').lower() == 'websocket':
        # Upgrade the request to a WebSocket connection
        ws = WebSocketContext(context)

        # Add the client to the connected clients set
        connected_clients.add(ws)

        # Process WebSocket messages
        while True:
            message = ws.receive_message()
            if message is None:
                break

            # Handle the message from the client, if needed

    return func.HttpResponse(
        "This is a regular HTTP response",
        status_code=200
    )

def send_trade_information(trade_info):
    message = json.dumps(trade_info)
    for client in connected_clients:
        client.send(message)
