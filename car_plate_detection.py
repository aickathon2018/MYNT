import cv2
import requests
import json

file = "traf.jpg"
img = cv2.imread(file)
cv2.imshow('detected',img)

# url name
url = "https://lpr.recoqnitics.com/detect"
accessKey = "bf4ff23aa84538af3c9c"
secretKey = "b0a2198ab3a0e331235768bacee230701209dab1"

# access_key and secret_key
data = {'access_key': accessKey,
  'secret_key': secretKey}

filename = {'filename': open(file,'rb')}
r = requests.post(url, files = filename, data=data)
content = json.loads(r.content)
rect = cv2.rectangle(img,(content['x'],content['y']),(content['h'],content['w']),(0,255,0),3)
print(content)
cv2.waitKey(0)