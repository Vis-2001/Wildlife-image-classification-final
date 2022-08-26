import tensorflow as tf
model=tf.keras.models.load_model('cnn_model')
print(model.summary())
img_file = './model_arch.png'
tf.keras.utils.plot_model(model, to_file=img_file, show_shapes=True, show_layer_names=True)