# app.py

from flask import Flask
from flask_graphql import GraphQLView
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_jsonrpc import JSONRPC
from api_module import text_to_image_api
from graphql_module import text_to_image_graphql
from socketio_module import text_to_image_socketio
from tcp_socket_module import text_to_image_tcp_socket
from jsonrpc_module import text_to_image_rpc
from graphene import Schema  # Schema olarak değiştirildi
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
jsonrpc = JSONRPC(app)

# API endpoint
@app.route('/api/v1/text-to-image', methods=['POST'])
def api_endpoint():
    params = request.json
    return text_to_image_api(params)

# GraphQL endpoint
graphql_schema = GraphQLSchema(
    query=GraphQLObjectType(
        name='Query',
        fields={
            'text_to_image': GraphQLField(
                GraphQLString,
                args={
                    'prompt': {'type': GraphQLString},
                    'style': {'type': GraphQLString},
                    # ... Diğer parametreler
                },
                resolve=lambda root, info, **args: text_to_image_graphql(args)
            )
        }
    )
)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=graphql_schema, graphiql=True))

# WebSocket endpoint
@socketio.on('text_to_image')
def socketio_endpoint(data):
    text_to_image_socketio(data)

# TCP Socket endpoint
def tcp_socket_endpoint(data):
    return text_to_image_tcp_socket(data)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024).decode('utf-8')
    result = tcp_socket_endpoint(data)
    client_socket.sendall(str(result).encode('utf-8'))
    client_socket.close()

# RPC endpoint
@jsonrpc.method('text_to_image')
def jsonrpc_endpoint(**params):
    return text_to_image_rpc(**params)

if __name__ == '__main__':
    socketio.run(app, debug=True)
