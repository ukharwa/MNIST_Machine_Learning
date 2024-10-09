<h1>Description</h1>
<h2>About</h2>
This project is intended to develop an understanding of different machine learning algorithms and techniques.
I am implementing the algorithms and building the models from scratch without
the use of machine learning libraries (Tensorflow, Keras, SciKit, etc.)

This is not intended to build the best, most accurate, or most efficient models
but rather simplify and explain the workings behind different supervised learning algorithms commonly used in machine learning.

The problem being used to train and test these models is the common problem of
classifying hand written digits and predicting what they are. The data used
is the MNIST dataset. 
<br>
<h2>FEATURES</h2>
The repository contains two main sections:
<ul>
  <li>Classifiers</li>
  <li>Website</li>
</ul>
<h2>Classifiers</h2>
The models section is where the actual machine learning algorithms are implemented.
There are currently two classifiers used to predict the drawings:
<ul>
  <li>Dense Neural Network</li>
  <li>k-Nearest Neighbors</li>
</ul>
<h3>Dense Neural Network</h3>
The first model uses a dense neural network with 4 layers.
The input layer is 784 nodes (28x28 pixel input drawing) and 10 output nodes (digits 0-9)
It contains 2 hidden layers with variable sizes.
There is currently a neural network abstraction class being developed that will be able to
generate neural networks of custom sizes.
<br>
<h3>k-Nearest Neighbors</h3>
The k-nearest neighbors algorithm is used to predict the digit by measuring the distance of the
input with all the training data. The distances are then sorted and the ouput is the most common label 
of the k (integer) smallest distance training digits.
The distances are currently computed using the euclildean distance between the elements. The value of k
can be set when constructing the class.
<br>
<h2>Website</h2>
The website is very basic at the moment and contains two pages:
>one to draw new digits and format the output to be used for predictions
>one used to train the model by labelling drawn digits

It is not hosted anyhwhere and just exists as html, css, and js documents.
There are plans to work on it in the future to be able to send data directly to the models
for prediction and training.
	
