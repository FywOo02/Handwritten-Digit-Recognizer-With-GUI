# Handwritten-Digit-Recognizer-With-GUI
> Handwritten digit recognizer with GUI based on Keras and Qypt5

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/FywOo02/Boston-House-Pricing-Forecast) 
![Python](https://img.shields.io/badge/python-3.10-519dd9.svg?v=103)
![Name](https://badgen.net/badge/Author/FywOo02/orange?)
![Language](https://badgen.net/badge/Language/English/pink?)
![Field](https://badgen.net/badge/Field/DeepLearning/blue?)
![Model](https://badgen.net/badge/Model/CNN/green?)

## What is this Project?
- The Handwritten Digit Recognizer is a device with a GUI interface developed on PyQt5. The principle is to train a MNIST digital dataset with a CNN model built on the keras package to obtain a recognizer to be able to recognize new samples of digit data brought by the user

<div align=center>
<img src="https://github.com/FywOo02/Handwritten-Digit-Recognizer-With-GUI/blob/main/Resorces/mnist%20graph.png">
</div>

## What is the structure of this CNN model
- 4 convolutional layers + 3 maximum pooling layers + 1 flatten layer + 1 fully connected layer
<div align=center>
<img src="https://github.com/FywOo02/Handwritten-Digit-Recognizer-With-GUI/blob/main/Resorces/CNN.png">
</div>


## How can I use the recognizer?
1. Install the related libraries
> This project uses deep learning related libraries, go check them out if you don't have them locally installed
```
pip install keras==2.12.0
pip install tensorflow==2.12.0
pip install numpy
pip install matplotlib
pip install PyQt5
```
2. Clone the original files in git bash
```
git clone https://github.com/FywOo02/Handwritten-Digit-Recognizer-With-GUI.git
```
3. Run the start.py, and try to play that!
```
python start.py
```
<div align=center>
<img src="https://github.com/FywOo02/Handwritten-Digit-Recognizer-With-GUI/blob/main/Resorces/result.png">
</div>

## File Descriptions
```
├── checkpoint/ 
├── PNG/ # save the numbers drawn by the user
├── Resources/
├── Environments.txt # environments needed to run the program
├── LICENSE.txt 
├── MainWidget.py # logical part of the GUI
├── model.h5 # the model for recognition
├── PaintBoard5.py # events part of the GUI
├── README.md
├── Start.py # @@place to start the recognition@@
├── Training_Model.py # model development
└── weights.txt
```

## Maintainer
[@FywOo02_Cho](https://github.com/FywOo02)

## Contributor
<a href="https://github.com/FywOo02">
  <img src="https://github.com/FywOo02.png?size=50">
</a>

## License
[MIT](https://github.com/FywOo02/Handwritten-Digit-Recognizer-With-GUI/blob/main/LICENSE) © Cho Zhu