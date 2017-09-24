from flask import Flask, jsonify, request, render_template
##package is the lower case, class is upper clase

app = Flask(__name__)
stores = [
    {
        'name': 'Yo-Store',
        'items': [
            {
                'name': 'Item_1',
                'price': 15
            }
        ]
    }
]

##__name__ gives each a unique name

# Web Server - piece of software, deisgned to accept incoming web requests
# GET - Server sees request (verb - GET) uses the / (as the path), and the protocol generally (HTTP) ex - GET / HTTP
# GET - Retrieve Something, ( GET /item/1)
# POST - Server receives data (we sent), and use it
# PUT - Make sure something is there ( PUT /item)
# DELETE - Remove Something DELETE ( /item/1)

##Stateless REST principle - one request cannot depend on any other request
# server only knows about current request, not any other previous request

@app.route('/')
def home():
    return render_template('index.html')

# POST /store_data {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') ##<> flask syntax
def return_single_store(name):
    ##iterate over stores, if store name matches return that one, if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message' : 'Store does not exist'})


# GET /store
@app.route('/store')
def return_all():
    return jsonify({'stores': stores})
    ##json always returns double quotes, returns dictionary, list stores is saved as "key" with value [{}]

# POST /store/<string:name>/item {name:price}
@app.route('/store/<string:name>/item', methods=['POST'])
def post_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def return_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items' : store['items']})
    return jsonify({'message' : 'store not found'})


app.run(port=5000)
