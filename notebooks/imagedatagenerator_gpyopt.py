from ctypes import resize
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import pandas as pd

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
    # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
        print(e)

# Install Gpyopt
#!pip install GPyOpt
import GPy, GPyOpt

PATH_RESIZED = 'C:/Users/gaelp/Documents/Projet_DataScientest/data/raw/resized_regions/'

# On charge le fichier contenant les étiquettes
df = pd.read_csv('C:/Users/gaelp/Documents/Projet_DataScientest/data/raw/train_annotations_v2.csv')

# On crée notre dataset :
data = df[['filename', 'annotation_class']]
data.columns = ['filename', 'class']

df_train=data.sample(frac=0.80,
                     random_state=21)
df_val=data.drop(df_train.index)

"""
@tf.function
def load_image(filepath, resize=(256,256)):
    im = tf.io.read_file(filepath)
    im = tf.image.decode_png(im, channels=3)
    return tf.image.resize(im, resize)


dataset_train = tf.data.Dataset.from_tensor_slices((X_train_path, y_train))
dataset_train = dataset_train.map(lambda x, y : [load_image(x), y], num_parallel_calls =-1)
dataset_train = dataset_train.batch(32)

dataset_test = tf.data.Dataset.from_tensor_slices((X_test_path, y_test))
dataset_test = dataset_test.map(lambda x, y : [load_image(x), y], num_parallel_calls =-1)
dataset_test = dataset_test.batch(32)
"""

# model creation
def create_model(filters=256, kernel_size=(7, 7), rate=0.2):
    model = models.Sequential()
    
    model.add(layers.Conv2D(filters, kernel_size, activation='relu', padding='same', name='layer1', input_shape=(256, 256, 3)))
    model.add(layers.Dropout(rate))

    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(filters*2, (3, 3), activation='relu', name='layer2'))
    model.add(layers.Dropout(rate))

    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(filters*2, (3, 3), activation='relu', name='layer3'))
    model.add(layers.Dropout(rate))

    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(4, activation='softmax'))
    
    return model

# global parameter for counting iteration
image_data_generator_opt_iter = 0

# fuction for GpyOpt
def image_data_generator_opt_f(x):
    # global
    global image_data_generator_opt_iter

    image_data_generator_opt_iter += 1
    print("========== {:2d} ==========".format(image_data_generator_opt_iter))
    
    # parameters for fit
    bs = 32
    ep = 65
    
    # arguments
    rr = x[:, 0][0]  # rotation_range
    wsr = x[:, 1][0] # width_shear_range
    hsr = x[:, 2][0] # height_shear_range
    sr = x[:, 3][0]  # shear_range
    zr = x[:, 4][0]  # zoom_range
    hf = True       # horizontal_flip
    vf = True       # vertical_flip
    
    parameter_name = ["rotation_range", "width_shift_range", "hight_shift_range", "shear_range", "zoom_range",
                      "horizontal_flip", "vertical_flip"]
    parameter_value = [rr, wsr, hsr, sr, zr, hf, vf]
    
    for n, v in zip(parameter_name, parameter_value):
        print("{:<20} ; {}".format(n, v))
    
    # data split
    #X, X_cv, y, y_cv = train_test_split(data, target, test_size=0.2, stratify=target, random_state=1)
    
    # CNN model parameters
    cnn_model_parameters = {'filters':32}
    
    # create model and compile
    model = create_model(**cnn_model_parameters)
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # ImageDataGenerator
    datagen = ImageDataGenerator(rescale=1./255,
                                 rotation_range=rr,
                                 width_shift_range=wsr,
                                 height_shift_range=hsr,
                                 shear_range=sr,
                                 zoom_range=zr,
                                 horizontal_flip=hf,
                                 vertical_flip=vf,
                                 fill_mode='nearest')
    
    # callback
    reduce_lr_callback = ReduceLROnPlateau(monitor='val_loss',
                                           factor=0.47,
                                           patience=5,
                                           min_lr=0.00005,
                                           verbose=1)
    
    # fit
    history = model.fit_generator(datagen.flow_from_dataframe(dataframe=df_train, 
                                                              directory=PATH_RESIZED, 
                                                              #x_col='filename',
                                                              #y_col='annotation_class',
                                                              class_mode='raw',
                                                              #target_size=(256, 256),
                                                              batch_size=4
                                                              ),
                                  #steps_per_epoch=df_train.shape[0]/8,
                                  validation_data=datagen.flow_from_dataframe(dataframe=df_val, 
                                                              directory=PATH_RESIZED, 
                                                              #x_col='filename',
                                                              #y_col='annotation_class',
                                                              class_mode='raw', 
                                                              #target_size=(256, 256), 
                                                              batch_size=4
                                                              ),
                                  epochs=ep,
                                  callbacks=[reduce_lr_callback])
    
    # check history and minimum val_loss
    history_df = pd.DataFrame(history.history)
    val_loss_min = history_df["val_loss"].min()
    
    # print val_loss_min
    print("{:<20} ; {}".format("minimum val_loss", val_loss_min))
    print("")
    
    # return minimum val_loss
    return val_loss_min
  
# set parameters
bounds = [{'name': 'rr',  'type': 'continuous', 'domain': (10, 50)},
          {'name': 'wsr', 'type': 'continuous', 'domain': (0.1, 0.4)},
          {'name': 'hsr', 'type': 'continuous', 'domain': (0.1, 0.4)},
          {'name': 'sr',  'type': 'continuous', 'domain': (0.1, 0.4)},
          {'name': 'zr',  'type': 'continuous', 'domain': (0.1, 0.4)}]

# initialization
myBopt = GPyOpt.methods.BayesianOptimization(f=image_data_generator_opt_f,
                                             domain=bounds,
                                             initial_design_numdata=7,
                                             acquisition_type='LCB')

# optimization
myBopt.run_optimization(max_iter=13)

# show results
parameter_name = ["rotation_range", "width_shift_range", "hight_shift_range", "shear_range", "zoom_range"]

for i in range(len(parameter_name)):
    print("{:<20} ; {}".format(parameter_name[i], myBopt.x_opt[i]))
    
print("{:<20} ; {}".format("val_loss", myBopt.fx_opt))

# save results
myBopt_x = pd.DataFrame(myBopt.X, columns=parameter_name)
myBopt_y = pd.DataFrame(myBopt.Y, columns=["val_loss"])
myBopt_df = pd.concat([myBopt_x, myBopt_y], axis=1)
myBopt_df.to_csv("myBopt2.csv", index=False)

print("Optimum parameters are saved!")