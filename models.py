# Copyright (c) 2019 Ramy Zeineldin
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from config import *
from utils import *
from encoders import *
from decoders import *
#from decoders import get_unet_decoder, get_unet_modified_decoder

# UNet based models
def get_deepseg_encoder(encoder_name):
    global encoder
    if encoder_name == 'UNet':
            encoder = get_unet_encoder
    elif encoder_name == 'VGG16':
            encoder = get_vgg16_encoder
    elif encoder_name == 'ResNet50':
            encoder = get_resnet50_encoder
    elif encoder_name == 'MobileNet':
            encoder = get_mobilenet_encoder
    elif encoder_name == 'MobileNetV2':
            encoder = get_mobilenetv2_encoder
    elif encoder_name == 'Xception':
            encoder = get_xception_encoder
    elif encoder_name == 'NASNetMobile':
            encoder = get_nasnet_encoder
    elif encoder_name == 'DenseNet121':
            encoder = get_densenet121_encoder
    elif encoder_name == 'UNet-Mod':
            encoder = get_unet_modified_encoder
    else:
            print("Invalid encoder name!!")
            print("Please choose a valid encoder network of the following:")
            print("UNet, UNet-Mod, VGG16, ResNet50, MobileNet, MobileNetV2,")
            print("Xception, NASNetMobile, DenseNet121")
    return encoder

def get_deepseg_decoder(decoder_name, n_classes, encoder, input_height, input_width, depth, filter_size, encoder_name=None, up_layer=False, trainable=True):
    global decoder
    if decoder_name == 'UNet':
        decoder = get_unet_decoder(n_classes, encoder, input_height, input_width, depth, filter_size, encoder_name, up_layer, trainable)
    elif decoder_name == 'UNet-Mod':
        decoder = get_unet_modified_decoder(n_classes, encoder, input_height, input_width, depth, filter_size, encoder_name, up_layer, trainable)
    else:
            print("Invalid decoder name!!")
            print("Please choose a valid decoder network of the following:")
            print("UNet, UNet-Mod")
    return decoder

def get_deepseg_model(encoder_name, decoder_name, n_classes, input_height, input_width, depth, filter_size, up_layer=False, trainable=True, load_model=True):
    encoder = get_deepseg_encoder(encoder_name)
    model = get_deepseg_decoder(decoder_name, n_classes, encoder, input_height, input_width, depth, filter_size, encoder_name, up_layer, trainable)

    model.compile(
        loss=weighted_categorical_crossentropy,
        optimizer=config['optimizer_name'],
        metrics=[dice_argmax, specificity, sensitivity])

    # print(model.summary())

    # print(model.input_shape)
    # print(model.output_shape)

    # Load the saved model
    if load_model:
        if config['load_model_path'] is None:
            # print('GG here')
            model.load_weights(glob.glob(os.path.join(config['weight_dir']+config['project_name'],'*'+config['model_num']+'*'))[0])
        else:
            # print('GG there')
            model.load_weights(config['load_model_path'])
    return model
