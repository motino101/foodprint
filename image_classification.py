# !pip install sentence-transformers
# !pip install --upgrade pip
# !pip install openai
# !pip install pillow
# import torch


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
    # your code to run the Python script goes here
    # We use the original CLIP model for computing image embeddings and English text embeddings
    en_model = SentenceTransformer('clip-ViT-B-32')

    img_names = [img_param]
    img_emb = en_model.encode([Image.open(BytesIO(urlopen(url).read()))
                            for url in img_names], convert_to_tensor=True)
    # #We download some images from our repository which we want to classify
    # img_names = ['spag.jpg']  # TO DO: add image
    # url = 'https://github.com/UKPLab/sentence-transformers/raw/master/examples/applications/image-search/'
    # for filename in img_names:
    #     if not os.path.exists(filename):
    #         util.http_get(url+filename, filename)

    # # And compute the embeddings for these images
    # img_emb = en_model.encode([Image.open(filepath)
    #                         for filepath in img_names], convert_to_tensor=True)

    # Then, we define our labels as text.
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv('food-list.csv')

    # Extract the first column and store it in a new variable, labels
    labels = df.iloc[:, 0].tolist()

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

    food_item = labels[pred_label]
    prompt = "What is the carbon footprint of " + \
        food_item + " in kg based on scientific estimates."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)

    # Carbon offsets:

    # We use Cool Effect's cost of carbon offsets: (1 Tonne = $14.62 USD). Find more here: https://www.cooleffect.org/travel-offset
    pollution_Numericamount = ''.join(
        c for c in response.choices[0].text if (c.isdigit() or c == "."))
    pollution_Numericamount = pollution_Numericamount.rstrip(
        pollution_Numericamount[-1])

    calculated_Cost = float(pollution_Numericamount) * 0.00110231 * 14.62
    print("The cost of offsetting this meal is: $" +
        str(round(calculated_Cost, 3)) + ".")

    return (response.choices[0].text + "  The cost of offsetting this meal is: $" +
        str(round(calculated_Cost, 3)) + ".")





if __name__ == '__main__':
    app.run(debug=True)
