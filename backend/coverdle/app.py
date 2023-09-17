from base64 import b64encode
from blur import blur_image
from flask import Flask, jsonify, render_template, request, send_file
from io import BytesIO
from mangadex import get_random_manga, get_cover_urls

import random

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/get-random-cover", methods=['GET'])
def get_random_cover():
    random_manga_id = get_random_manga()
    covers = get_cover_urls(random_manga_id)

    random_cover = random.randint(0, len(covers)-1)
    response = jsonify(message=covers[random_cover])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/blur-image", methods=['GET'])
def get_cover():
    args = request.args
    image_url = args.get("url", None)

    blur_amount = int(request.args.get("blur-amount", 0))
    blurred_image = blur_image(image_url, blur_amount)

    image_io = BytesIO()
    blurred_image.save(image_io, 'PNG')
    image_io.seek(0)
    return send_file(image_io, as_attachment=False, mimetype='image/png')

if __name__ == "__main__":
    app.run("localhost", 1617)