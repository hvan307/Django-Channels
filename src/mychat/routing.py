from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import chat.routing

# When connection is made to the Channels development server, the ProtocolTypeRouter will first inspect the type of connection. If it is a websocket connect (ws:// or wss://), the connection will be given to the AuthMiddlewareStack, which the populates the connections scope. Then the connection will be given to the URLRouter
# Source: https://channels.readthedocs.io/en/latest/tutorial/part_2.html
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})