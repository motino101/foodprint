# !pip install sentence-transformers
# !pip install --upgrade pip
# !pip install openai
# !pip install pillow
# import torch
# !pip install ipython


from flask import Flask
from flask import request
from sentence_transformers import SentenceTransformer, util
import PIL
from PIL import Image
import glob
import re
import torch
import pickle
import zipfile
from IPython.display import display
from IPython.display import Image as IPImage
import os
from tqdm.autonotebook import tqdm
import torch
import pandas as pd
import openai
openai.api_key = "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"

# uploading image
from urllib.request import urlopen
from io import BytesIO

app = Flask(__name__)

@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    img_param = request.json['img_param']
    print("the image is: ", img_param)
    en_model = SentenceTransformer('clip-ViT-B-32')

    img_names = [img_param]
    img_emb = en_model.encode([Image.open(BytesIO(urlopen(url).read()))
                            for url in img_names], convert_to_tensor=True)
    
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv('food-list.csv')

    # Extract the first column and store it in a new variable, labels
    labels = df.iloc[:, 0].tolist()
    c_footprints = df.iloc[:, 1].tolist()

    # And compute the text embeddings for these labels
    en_emb = en_model.encode(labels, convert_to_tensor=True)

    # Now, we compute the cosine similarity between the images and the labels
    cos_scores = util.cos_sim(img_emb, en_emb)

    # Then we look which label has the highest cosine similarity with the given images
    pred_labels = torch.argmax(cos_scores, dim=1)


    # Finally we output the images + labels
    for img_name, pred_label in zip(img_names, pred_labels):
        display(IPImage(img_name, width=200))
        print("Predicted label:", labels[pred_label])
        print("\n\n")

    # Get carbon footprint
        # We use the original CLIP model for computing image embeddings and English text embeddings
    food_item = labels[pred_label] # get the predicted food item
    answer = c_footprints[pred_label] # get the carbon footprint of the food item

    calculated_Cost = float(answer) * 0.00110231 * 14.62
    print("The cost of offsetting this meal is: $" +
        str(round(calculated_Cost, 3)) + ".")

    return ("  The cost of offsetting this meal is: $" + str(round(answer, 0)) + "  The cost of offsetting this meal is: $" +
        str(round(calculated_Cost, 3)) + ".")

if __name__ == '__main__':
    app.run(debug=True)
