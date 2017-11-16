from MNIST_experiment import Experiment
import numpy as np

class MNIST_DOMAIN_OPTIONS:
    """
    Class for the Setup of the Domain Parameters
    """
    # Size of each image: MNIST_SIZE x MNIST_SIZE
    MNIST_SIZE = 28
    #
    #   ================
    #   Reward constants
    #   ================
    #   Reward for correctly Identifying a number:
    REWARD = +1.
    #   Step Reward

    #   ======================
    #   Domin specific options
    #   ======================
    #
    # Number of image channels: 1
    # --> greyscale
    CHANNELS = 1
    #
    # Resolution of the Sensor
    SENSOR = 8
    # Number of zooms
    NZOOMS = 1
    # Minimal zoom size # zooms -> mnist_size * (min_zoom **<depth_level>)
    MIN_ZOOM = 2
    # Number of Glimpses
    NGLIMPSES = 7
    # Standard Deviation of the Location Policy
    LOC_STD = 0.11
    # This variable basically outlines how far (in pixels) near the borders
    # the center of each glimpse can reach with respect to the center.
    # So a value of 13 (the default) means that the center of the glimpse
    # can be anywhere between the 2rd and 27th pixel (for a 1x28x28 MNIST example).
    # So glimpses of the corner will have fewer zero-padding values
    # then if UNIT_PIXELS = 14
    UNIT_PIXELS = 13
    # Translated MNIST
    TRANSLATE = False
    # Size of each image: MNIST_SIZE x MNIST_SIZE
    TRANSLATED_MNIST_SIZE = 60

class PARAMETERS:
    """
    Class for specifying the parameters for
    the learning algorithm
    """

    #   =========================
    #   General parameters for the
    #   experiment
    #   =========================

    #   Number of learning epochs
    MAX_EPOCHS= 600
    #   Batch size
    BATCH_SIZE = 20

    #   =========================
    #   Save and Load the Model
    #   =========================
    LOAD_MODEL = False
    MODEL_FILE_PATH = './'
    MODEL_FILE = '001-network'


    #   =========================
    #   Algorithm specific parameters
    #   =========================

    #   To be used optimizer:
    #   rmsprop
    #   adam
    #   adadelta
    #   sgd
    OPTIMIZER = 'sgd'
    # Learning rate alpha
    LEARNING_RATE = 0.01
    # Number of steps the Learning rate should (linearly)
    # decay to MIN_LEARNING_RATE
    LEARNING_RATE_DECAY = 200
    # Minimal Learning Rate
    MIN_LEARNING_RATE = 0.00001
    # Momentum
    MOMENTUM = 0.9
    # Clipnorm
    CLIPNORM = 0
    # Clipvalue
    CLIPVALUE = 0


def main():
    params = PARAMETERS
    dom_opt = MNIST_DOMAIN_OPTIONS
    for i in range(1, 2):
        exp = Experiment(params, dom_opt, "{0:03}".format(i) + "-results.json", "{0:03}".format(i) + "-network")
        del exp


if __name__ == '__main__':
    main()
