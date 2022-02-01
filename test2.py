from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import seaborn as sns

# docker run --name redisdb -p 6379:6379 -e REDIS_PASSWORD=password123 bitnami/redis:latest
# Redis Database Connection
from waihonanumpy import RedisStorage
redis = RedisStorage('password123')

# TODO
# CHANGE this to input params
input_folder = "original/original_R1B12"

df=[]
[df.append(x[0].split(input_folder)[1]) for x in os.walk(input_folder)]
patientid = list(filter(None, df)) #drop empty


data_df = pd.DataFrame()
df = []
for p in patientid: # p is the patient string to store in redis
    
    db_test = pd.DataFrame()
    patdir = os.path.join(input_folder,p[1:]) # Remove the first '/' 
    for root, dirs, files in os.walk(patdir): # iterate extracted features
        for file in files:
            feature = file.split('original_')[1].split('.nii')[0] #this is a string to store in redis key 'feature'
            if not feature == 'glcm_MCC':      
                
                test_file = os.path.join(patdir,file) 
                test_raw = sitk.ReadImage(test_file)             
                test_arr = sitk.GetArrayFromImage(test_raw)
                # test_arr is the feature 3D array to store in redis
                redis[str(p).strip('/'), feature.strip('.mha')] =test_arr


print("end...")

values = redis["*","firstorder*"]
for v in values:
    print(v)