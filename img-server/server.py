import datetime
import os
import flask

# UPLOAD_BASE_FOLDER = os.path.basename('/opt/pi-camera/uploads')
UPLOAD_BASE_FOLDER_ = os.path.basename('uploads')

app = flask.Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
  # Uploads a file with the following parameters in it's name
  # {image_file}={location}_{timestamp in seconds}.{file extension}
  # 
  # A sample curl to manually test:
  # curl -v -X POST http://localhost:5000/upload -F 'image=@foo_1524945129.jpg'
  # 
  # The file will be saved:
  # uploads/{location}/{YYYY}/{MM}/{DD}/{image_file}

  image_file = flask.request.files['image']

  location_timestamp = os.path.splitext(image_file.filename)[0].split('_')
  location = location_timestamp[0]
  timestamp = datetime.datetime.fromtimestamp(float(location_timestamp[1]))
  save_directory = os.path.join(UPLOAD_BASE_FOLDER_, location, timestamp.strftime('%Y/%m/%d')) 
  if not os.path.exists(save_directory):
    os.makedirs(save_directory)

  save_location = os.path.join(save_directory, image_file.filename)
  image_file.save(save_location)
  return 'image uploaded to %s' % save_location
