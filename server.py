from flask import Flask, send_from_directory, send_file

app = Flask(__name__)

@app.route('/')
def send_index():
    return send_file('index.html')

@app.route('/index.html')
def send_indexhtml():
    return send_file('index.html')

@app.route('/bower_components/<path:path>')
def send_bower(path):
    print path
    return send_from_directory('bower_components', path)

@app.route('/manifest.json')
def send_manifest():
    return send_file('manifest.json')

@app.route('/src/<path:path>')
def send_src(path):
    return send_from_directory('src', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)



if __name__ == "__main__":
    app.run()
