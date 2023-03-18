import React from 'react';
import { StyleSheet, View, Text } from 'react-native';
import ImageUploader from './Uploader';
import { LogBox } from 'react-native';
LogBox.ignoreLogs(['Warning: ...']); // Ignore log notification by message
LogBox.ignoreAllLogs();//Ignore all log notifications

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>FoodPrint</Text>
      <Text style={styles.bodyText}>A photo says a thousand words - including your meal's carbon impact!</Text>
      <View style={styles.imageUploadContainer}>
        <ImageUploader />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#90c689',
    alignItems: 'center',
    justifyContent: 'flex-start',
    paddingTop: 50,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 50,
    fontWeight: 'bold',
    marginBottom: 20,
    color: "#ffffff",
  },
  imageUploadContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 2,
    borderStyle: 'dashed',
    borderRadius: 5,
    borderColor: '#ccc',
    paddingVertical: 20,
    paddingHorizontal: 40,
    marginBottom: 20,
    backgroundColor: "#f0f7f0"
  },
  cameraIcon: {
    marginRight: 20,
  },
  imageUploadText: {
    fontSize: 20,
    color: '#999',
  },
  textBoxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  textIcon: {
    marginRight: 10,
  },
  textBox: {
    flex: 1,
    fontSize: 18,
    color: '#333',
  },

  bodyText: {
    marginBottom: 20,
    fontWeight: "bold",
    fontSize: 18,
    textAlign: 'center'
  }
});
