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


## Dataset:
Our dataset is a collection of recorded network-related data that contains column fields of the
connection log called network features. It’s used for building and training our AI model to detect
network intrusions. It includes various features that help us understand and classify network
connections as normal or potentially malicious.

  [**Dataset Features**](https://drive.google.com/file/d/1wL-fa94_UrBMrirEOCV1v3bvMu4gvRrm/view?usp=sharing)

  **Continuous:** This means that a feature is _numerical_ and can take on a range of real-number
  values. These values can be measured on a scale, and they typically represent quantities or
  measurements. Features marked as "continuous" are those where the data can be any real
  number, and they often represent things like counts, time durations, or quantities.

  **Symbolic:** This indicates that a feature is _categorical_ or _non-numeric_. Symbolic features have
  discrete values that represent categories or labels. They can be thought of as representing
  different types or classes, such as "yes" or "no", "TCP" or "UDP", or "success" or "failure."
  Symbolic features are used to represent qualitative data and are typically non-numeric in nature.

The results that our model can predict : [**AttackClasses.csv**](https://github.com/harbaouiwiem/SafeShield/blob/main/AttackClasses.csv)
You can understand each attack by following this [Link](https://archive.ll.mit.edu/ideval/docs/attackDB.html)

## Project Components: 
### 1. Operating system 
The IDS is deployed on Ubuntu a linux-based OS that is secure and flexible.

### 2. TrainedModel.py
The neural network is created using _keras_ library, compiled with the "categorical_crossentropy" 
loss function, the "adam" optimizer, and "accuracy" as a metric.
Trained for 20 epochs using a [Dataset](https://github.com/harbaouiwiem/SafeShield/blob/main/DataSet.csv) , and loaded the neural network weights in a serialized
file named "NeuralNetwork.h5".

Libraries used in this code are : _pandas, NumPy, scikit-learn,_ and _Keras._

### 3. Siem.py
In this code we will see if the model we created will predict wether the network is safe or not 
by giving it users logs. 

It integrates the IDS with Elasticsearch  for logging and monitoring security threats in users
logs data.

The code loads the neural network model from ["NeuralNetwork.h5"](https://github.com/harbaouiwiem/SafeShield/blob/main/Trained_Model.h5) using _TensorFlow_ and make
predictions on users log data identifying potential threats, which are generated to Elasticsearch creating searchable and real-time monitoring system.

Libraries used in this code are : _TensorFlow/Keras, NumPy,Pandas_ and _Elasticsearch_.

### 4. ELK Stack:
In this project the ELK stack serves for collecting and preprocessing logs using logstash,
storing and indexing log data for a fast retrieval using Elasticsearch and real-time threat
monitoring and visualization of potential security threats using Kibana.

### 5. Deployment on Docker:
We utilized Docker to containerize both our Python code and the ELK Stack components to 
run these services simultaneously ensuring that our IDS and ELK Stack work seamlessly together.

## Code Setup 
You need to use git clone command to download this project : 
The python used is Python 3.10.2.
 
##### updating the package list :
```
$- sudo apt update
```
##### Installing the disutils and setuptools :
```
$- sudo apt install python3-distutils python3-setuptools
```
##### Installing pip3 :
``` 
$- sudo apt install python3-pip
```

##### Install the libraries needed : 
```
$- pip3 install numpy pandas scikit-learn tensorflow keras elasticsearch
```

## Docker Setup:
As an initial step, Docker serves as a tool for the project deployment. Consequently, configuring
Docker on our system is essential to establish a seamless working environment.

+ You can skip this step if you already have Docker and Docker Compose installed and
functioning correctly.
+ If you encounter any difficulties during the Docker installation, you can find additional guidance
and support in [this official documentation link](https://docs.docker.com/engine/install/ubuntu/?fbclid=IwAR0JRdUbtYO2df1fhNxFVT7FgHShykMza1hpBCMc6tXnya34lkO9ZLNQJoY)

##### Updating the system:
```
$- sudo apt update
```
##### Installing the curl utility:
```
$- sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
##### Downloading the docker packages:
```
$- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
##### Adding the downloaded repository:
```
$- pip3 install --upgrade requests
$- sudo add-apt-repository deb [arch=amd64] https://download.docker.com/linux/ubuntu
bionic stable
```
##### Updating the system again:
```
$- sudo apt update
```
##### Adding the docker-ce cache policy:
```
$- apt-cache policy docker-ce docker-compose
```
##### Running the install command:
```
$- sudo apt install docker-ce docker-compose
```
##### Check the docker daemon's status, and the docker-compose version:
```
$- sudo systemctl status docker
$- docker-compose --version
```
##### Adding the current user to the docker users group :
```
$- sudo usermod -aG docker ${USER}
```
##### Checking that the user is added to the group:
```
$- su - ${USER}
```
## ELK Setup 

after successfully setting up docker in your system, you need to build the ELK stack.

##### starting docker containers : 
```
$- docker-compose up -d
```
##### checking the elk stack's health
after running the following command you need to see the 3 containers elasticsearch, logstash and kibana running : 
```  
$- docker ps
```
##### opening the kibana dashboard
you need to connect to your localhost on port 5601 :
 ```  
 http://localhost:5601
 ```
after running the last command, the kibana login page should be displayed.
    
username : elastic & password : changeme 




