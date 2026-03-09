from tensorflow.keras.preprocessing import image

img = image.load_img("test_leaf.jpg", target_size=(128,128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

result = model.predict(img_array)

print(result)