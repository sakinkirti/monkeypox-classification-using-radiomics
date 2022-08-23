import os
import radiomics
import numpy as np
import pandas as pd
import SimpleITK as sitk

from radiomics import featureextractor
from PIL import Image

class MonkeypoxFeatureGenerator:

    def __init__(self, monkeypox_data_path, nonmonkeypox_data_path):
        '''
        init method to initialize the extractor and set up the data

        monkeypox_data_path: the path denoting all of the monkey pox data
        nonmonkeypox_data_path: the path denoting all of the non monkey pox images
        '''

        # pyradiomics feature extractor
        self.extractor = featureextractor.RadiomicsFeatureExtractor()

        # define the data paths
        self.mp_data = monkeypox_data_path
        self.nmp_data = nonmonkeypox_data_path
        self.data_paths = [self.mp_data, self.nmp_data]

        # define radiomic data storage solution
        self.storage

    def generate_features(self):
        '''
        method to load the image data in
        '''

        # iterate through data paths to generate features
        for path in self.data_paths:
            # iterate through mp or nmp data
            for mp_path in path:
                # get the image
                img = Image.open(mp_path)
                arr = np.asarray(img)


