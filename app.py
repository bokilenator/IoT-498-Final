from flask import Flask, render_template, Response
import lights
# import camera driver
from camera_pi import Camera
from PIL import Image
from io import BytesIO

app = Flask(__name__)

capturing = False
newShoe = "slippers"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture/<shoe>')
def capture(shoe):
    global newShoe 
    newShoe = shoe
    global capturing 
    capturing = True
    return 'captured'

@app.route('/slippers')
def lightSlippers():
    lights.lightSlippers()
    return 'slippers'

@app.route('/sneakers')
def lightSneakers():
    lights.lightSneakers()
    return 'sneakers'

@app.route('/snowboots')
def lightSnowBoots():
    lights.lightSnowBoots()
    return 'snowboots'

@app.route('/rainboots')
def lightRainBoots():
    lights.lightRainBoots()
    return 'rainboots'

def gen(camera):
    """Video streaming generator function."""
    global capturing
    global newShoe
    while True:
        frame = camera.get_frame()
        if capturing:
            print(type(frame))
            # Load image from BytesIO
            im = Image.open(BytesIO(frame))
            im.save('static/' + newShoe + '.png')
            # snap = open('snap.jpg', 'w')
            # snap.write(frame)
            # snap.close()
            capturing = False
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=False, host='0.0.0.0')