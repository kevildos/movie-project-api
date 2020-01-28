from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Give data?
        return request.data
    return 'Flask'


if __name__ == '__main__':
    app.run(debug=True)
