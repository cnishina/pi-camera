import os
import picamera
import requests
import time

import ConfigParser

DIRECTORY_ = 'images'

if not os.path.exists(DIRECTORY_):
    os.makedirs(DIRECTORY_)

config = ConfigParser.RawConfigParser()
config.read('camera_dev.cfg')
connection = config.get('camera', 'connection')
location = config.get('camera', 'location')

camera = picamera.PiCamera()

while True:
  seconds = int(round(time.time()))
  filename = '%s_%d.png' % (location, seconds)

  camera.capture(os.path.join(DIRECTORY_, filename))

  files = {'image': open(os.path.join(DIRECTORY_, filename), 'rb')}
  requests.post(connection + '/upload', files=files)
