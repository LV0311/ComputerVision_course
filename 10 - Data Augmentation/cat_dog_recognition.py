import cv2
from tensorflow.keras.models import load_model

SCALE = (200, 200)

model = load_model('model_aug.h5')

# Caricamento dell'immagine
img_path = input("Inserire il percorso all'immagine: ")
img = cv2.imread(img_path)

# Preprocessing dell'immagine
small_img = cv2.resize(img, SCALE)
x = small_img.astype(float)
x/=255.

# Riconoscimento dell'immagine
x = x.reshape(1, SCALE[0], SCALE[1], 3)
y = model.predict(x)
y = y[0]
print("Network prediction: %.4f" % y[0])

# Stampiamo il risultato

label = "Cane" if y>0.5 else "Gatto"

start_point = (img.shape[1]-200, img.shape[0]-100)
end_point = (img.shape[1], img.shape[0])

cv2.rectangle(img, start_point, end_point, (0,0,255), cv2.FILLED)
cv2.putText(img, label, (start_point[0]+50, start_point[1]+50), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)