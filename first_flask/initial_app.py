from flask import Flask
##package is the lower case, class is upper clase

app = Flask(__name__)

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