from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'craig'
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = [


]

class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        ## make sure to have None as available argument should next not return any filter
        return {'item' : item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return{'message': "An item with a name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {
            'name' : name,
            'price' : data['price']
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items' : items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)