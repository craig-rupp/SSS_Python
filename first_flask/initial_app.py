from flask import Flask
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

@app.route('/')
def home():
    return "Hello, world"

app.run(port=5000)

# Web Server - piece of software, deisgned to accept incoming web requests
# GET - Server sees request (verb - GET) uses the / (as the path), and the protocol generally (HTTP) ex - GET / HTTP
# GET - Retrieve Something, ( GET /item/1)
# POST - Server receives data (we sent), and use it
# PUT - Make sure something is there ( PUT /item)
# DELETE - Remove Something DELETE ( /item/1)

##Stateless REST principle - one request cannot depend on any other request
# server only knows about current request, not any other previous request

# POST /store_data {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>') ##<> flask syntax
def return_single_store(name):
    pass

# GET /store
@app.route('/store')
def return_all():
    pass

# POST /store/<string:name>/item {name:price}
@app.route('/store/<string:name>/item', methods=['POST'])
def post_item(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def return_store_item(name):
    pass
