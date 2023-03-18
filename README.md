# Foodprint: A Sustainability Awareness App for iOS/Android
Foodprint is a mobile app for iOS and Android that helps users understand the environmental impact of their food choices by estimating the carbon footprint of a meal from a user-uploaded image. The app uses React Native and integrates the CLIP (Contrastive Language-Image Pre-Training) model to analyze photos and estimate the carbon footprint in kilograms of CO2.

## Introduction
Keeping track of one's carbon footprint can be challenging, but it is a necessary task as environmental awareness increases. Our team has developed an app that informs the user about the carbon footprint of any food item in a standard unit of 1 kilogram of CO2 by analyzing photos uploaded by the user. The app uses CLIP and ChatGPT technologies to identify and interpret the content of an image and then export the content using React in a user-friendly application interface.

## Features
Estimate the carbon footprint of a meal from a user-uploaded image
Provide information about the carbon footprint in kilograms of CO2
Educate users about the carbon footprint of various dishes and promote environmental education
Demo Video
Check out our demo video to see Foodprint in action!

## Foodprint Demo Video

## Installation
To install the app, first, ensure that all dependencies listed in requirements.txt are installed. Then run npm expo start in the terminal. If using the iOS Simulator, upload the images you want to classify into the local directory "./". If using expo start, download Expo Go and scan the QR code.

Please note that the app currently has some caveats. The estimates are based on serving size only.

## Usage
Using the app is incredibly easy. Simply upload a picture of your meal from your camera roll, and the app will provide you with an approximate estimate of the carbon footprint resulting from one serving of your meal. The estimate is usually accurate to within 0.5kg, and the app will also calculate the cost of offsetting the emissions.

## Contributors
Cole Lee
Lucas Leanza
Rachel Wang
License
This project is licensed under the MIT License.
