import pandas as pd
import matplotlib.pyplot as plt  

"""
    def generateData(String subject, String text_type):
    returns DataFrame

    Params:
    String subject: Pass an index of List dyslexic/non-dylexic.
    String text_type: Pass a value of Dict text_type for text_type.
"""
def generateData(subject, text_type):
    path='essential_dataset/data/Subject_'+ subject + text_type + '_raw.csv'
    return pd.read_csv(path)

"""
    def plotScatter(DataFrame df, String image_path):
    Creates a scatter plot based on DataFrame, with an image as background.

    Params:
    DataFrame df: Use GenerateData to get a valid DataFrame
    String image_path: Pass a value of Dict image_path for image_path.
"""
def plotScatter(df, image_path):
    gaze_x_mean = (df['gaze_x_left'] + df['gaze_x_right']) / 2
    gaze_y_mean = (df['gaze_y_left'] + df['gaze_y_right']) / 2

    print(df)

    fig, ax = plt.subplots()
    img = plt.imread(image_path)
    ax.imshow(img)
    ax.scatter(gaze_x_mean, gaze_y_mean, s = 5, alpha=0.1) 
    plt.title('')  
    plt.show()  