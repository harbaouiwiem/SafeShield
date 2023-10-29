# SafeShield 
## Introduction:
SafeShield, an **Intrusion Detection System (IDS) prototype** based on Deep Learning!
Our project is a simulation of threat detection, developed during our second year of Computer
Engineering bachelor as part of the Federated Project course.

As beginners passionate about cybersecurity, we embarked on this journey to delve deeper into
real-life threat detection scenarios and learn more about **SIEM (Security Information and Event
Management)**.

Our motivation was simple: to learn and share our knowledge! As a result, we proudly present
this project to fellow beginners and students eager to understand the basics of IDS.

## Description:
We developed a prototype of a deep learning-based intrusion detection system. 
The model of the IDS processes network-based data inputs, as a result it will distinguish 
between normal network connections and potential attacks, also it recognizes the attacks and
categorizes them.

The IDS was initially a neural-network model, that is developed with python and keras library
then run on Ubuntu.

In order to enhance the visibility and behaviour analysis, we implemented the ELK stack to 
provide graphical illustrations.

## Project Components: 
###Operating system 
the IDS is deployed on Ubuntu a linux-based OS that is secure and flexible.

### 1. TrainedModel.py
The neural network is created using keras library, compiled with the "categorical_crossentropy" 
loss function, the "adam" optimizer, and "accuracy" as a metric.
Trained for 20 epochs using a Dataset , and loaded the neural network weights in a serialized
file named "NeuralNetwork.h5".

Libraries used in this code are : pandas, NumPy, scikit-learn, and Keras.

### 2. Siem.py
In this code we will see if the model we created will predict wether the network is safe or not 
by giving it users logs. 

It integrates the IDS with Elasticsearch  for logging and monitoring security threats in users
logs data.

The code loads the neural network model from "NeuralNetwork.h5" using TensorFlow and make
predictions on users log data identifying potential threats, which are generated to 
Elasticsearch creating searchable and real-time monitoring system.

Libraries used in this code are : TensorFlow/Keras, NumPy,Pandas and Elasticsearch.

### 3. ELK stack:
In this project the ELK stack serves for collecting and preprocessing logs using logstash,
storing and indexing log data for a fast retrieval using Elasticsearch and real-time threat
monitoring and visualization of potential security threats using Kibana.

### 4. Deployment on docker:
we utilize Docker to containerize both our Python code and the ELK Stack components to 
run these services simultaneously ensuring that our IDS and ELK Stack work seamlessly together.


