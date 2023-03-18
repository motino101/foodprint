import React, { useState } from 'react';
import { StyleSheet,View, Text, Image, Button } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { LogBox } from 'react-native';
LogBox.ignoreLogs(['Warning: ...']); // Ignore log notification by message
LogBox.ignoreAllLogs();//Ignore all log notifications

export default function ImageUploader() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [description, setDescription] = useState('');

  const pickImage = async () => {
    
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
      selecteds: ["spag.jpg"],
    });

    if (!result.cancelled) {
      setSelectedImage(result.uri);

      // Call Uploader.JS to generate description
      setDescription('Calculating the carbon footprint...');
      fetch('http://127.0.0.1:5000/run-python-script', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({img_param: result.uri})
      })
        .then(response => response.text())
        .then(result => setDescription(result))
        .catch(error => console.log(error));
    }
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button title="Upload an image of your meal" onPress={pickImage} style={styles.buttonText} />
      {selectedImage && (
        <View style={styles.view}>
          <Image source={{ uri: selectedImage }} style={{ width: 200, height: 200 }} />
          <Text style={styles.bodyText}>{description}</Text>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  view: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonContainer: {
    marginBottom: 0,
    fontWeight: "bold",
    fontSize: 18,
    textAlign: 'center'
  },
  buttonText: {
  },

  bodyText: {
    marginBottom: 10,
    fontWeight: "bold",
    fontSize: 16,
    textAlign: 'center'
  }
});