import os
from flask import Flask

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook_manager'
app.config["MONGO_URI"] = 'mongodb+srv://Gillian:N3wdb@2019@myfirstcluster-eimbl.mongodb.net/cookbook_manager?retryWrites=true&w=majority'


@app.route('/')
def hello():
    return 'Hello World ...three'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)