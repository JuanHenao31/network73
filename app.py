from flask import Flask
from flask_restx import Api, Resource, fields
from system73.controller.network_controller import get_network_status, delete_node_network, add_node_network

app = Flask(__name__)

api = Api(app)


resource_fields_add_node = api.model('AddNode', {
    'key': fields.Integer(description='Key of the Node, Unique', required=True),
    "capacity": fields.Integer(description='Capacity of the Node, Unique', required=True),

})
resource_fields_delete_node = api.model('DeleteNode', {
    'key': fields.Integer(description='Key of the Node, Unique', required=True),
})

elimination_node_ok = api.model('EliminationRs', {
    'message': fields.String(description='Node Eliminated')
})

network_status = api.model('NetworkStatusRs', {
    'key': fields.Integer,

    "capacity": fields.Integer,
    "availability": fields.Integer,
    "parent_id": fields.Integer,
    "children_ids": fields.Integer
})


@api.errorhandler
def page_not_found(e):
    return {'message': 'Route not found'},


@api.route('/network',
           doc={"description": "End point for getting the status of the network"}, )
@api.doc('DOC NETWORK')
class GetNetwork(Resource):
    @api.response(200, 'Success', network_status)
    def get(self):
        return get_network_status()


@api.route('/add-node',
           doc={"description": "End point for adding nodes to the network"}, )
class AddNode(Resource):
    @api.response(200, 'Success', network_status)
    @api.response(400, 'Fail')
    @api.expect([resource_fields_add_node])
    def post(self):
        return add_node_network()


@api.route('/delete-node',
           doc={"description": "End point for deleting  nodes from the network"}
           )
class AddNode(Resource):
    @api.response(200, 'Success', elimination_node_ok)
    @api.response(400, 'Fail')
    @api.expect([resource_fields_delete_node])
    def post(self):
        return delete_node_network()


if __name__ == '__main__':
    app.run()
