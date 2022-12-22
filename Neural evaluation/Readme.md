## Chapter objectives 

* Describe some characteristics of natural intelligence, including recognition, classification, response, and learning.
* Label diagrams of a neuron and a synapse with the names of their constituent parts.
* Explain the process by which a neuron generates an action potential, including the role of the cell membrane and ion channels.
* Describe the action of a synapse and the phenomenon of long-term potentiation.
* Explain the role of units, input functions, activation functions, and weights in an artificial neural network.
* Use diagrams to explain how units and weights can be combined in various topologies to form an artificial neural network.
* Describe the concept of a learning rule in detail, including an example.
* Use mathematical representations, including signal graphs, sigma notation, and vector/matrix notation, to explain neural network concepts.


## Overview

In this unit, you will learn about neural networks, which are artificial systems that are inspired by the structure and function of the human brain. Neural networks are able to recognize patterns, classify stimuli, and select appropriate responses, similar to how the human brain does. They consist of special cells called <b>neurons</b>, which communicate with each other through junctions called <b> synapse </b>. The nervous system can be divided into the central nervous system (CNS) and the peripheral nervous system (PNS). The CNS consists of the brain and spinal cord, while the PNS consists of all other nerves. Neural networks can be arranged in different topologies, including feedforward, lattice, and recurrent. They can be trained using <b> learning rules </b> </b>, which adjust the weights of the connections between units based on the input data and the

# Biological background of the nervous system

A neuron is a cell that is specialized for transmitting information in the nervous system. It has several parts, including the cell body, dendrites, axon, and terminal buttons. A synapse is a junction between two neurons, through which one neuron can communicate with another by releasing chemical messengers called neurotransmitters.

When a neuron receives a signal from another neuron, it generates an action potential, which is a sudden change in the electrical charge of the cell membrane. This is caused by the movement of ions, such as sodium and potassium, through ion channels in the membrane. The action potential travels down the axon of the neuron and is transmitted to other neurons through the synapse.

At a synapse, the action potential causes the release of neurotransmitters, which bind to receptors on the receiving neuron and either excite or inhibit it. This process is called neurotransmission. Long-term potentiation is a process by which the strength of a synapse is increased, resulting in more efficient communication between neurons.

# Neural network in deep learning 

In an artificial neural network, units are the basic processing elements that perform computation based on the input data and weights. The input function determines how the input data is processed before it is passed to the units. The activation function is a mathematical function that determines the output of the units based on their inputs and weights. Weights are values that determine the strength of the connections between units. Different topologies can be used to arrange the units and weights in an artificial neural network, such as feedforward, lattice, and recurrent.



# Single-layer perceptron

A single-layer perceptron is a type of artificial neural network that consists of a single main unit, also known as a neuron, which receives input from multiple dummy units. These dummy units are connected to the main unit through weighted connections, and the activations of the dummy units are set externally. The main unit calculates its activation based on the weighted sum of the stimuli it receives from the input units using a threshold function. Single-layer perceptrons can be used to compute truth tables, such as AND and OR, or to classify patterns.

The input space of a single-layer perceptron is the set of all possible inputs that the perceptron can receive. If the inputs are limited to certain values, such as 1 or 0, the input space is restricted to specific points in the space. However, if the inputs can take real number values, the input space is the entire space. When a single-layer perceptron classifies its inputs, it is effectively dividing the input space into two parts, with one group of inputs resulting in an activation of 1 and the other group resulting in an activation of 0.

In the weight space of a single-layer perceptron, the weight vector represents the weights of the connections between the input units and the main unit. The weight vector can be adjusted during the learning process to improve the accuracy of the perceptron's output.<br>


##  Learning Rules

A learning rule is a set of instructions that determines how the weights of a neural network should be adjusted based on the input data and the desired output. There are two main learning strategies for single-layer perceptrons: the perceptron rule and the delta rule. The perceptron rule adjusts the weight vector based on the error between the desired output and the actual output of the perceptron, while the delta rule uses gradient descent to adjust the weight vector.

#  Multi-layer perceptrons

Multi-layer perceptrons also known as fully connected neural networks, are more complex than single-layer perceptrons and consist of multiple layers of neurons, with the neurons in one layer connected to all the neurons in the next layer. One of the most common learning strategies for multi-layer perceptrons is error backpropagation, which involves adjusting the weights of the connections between the neurons based on the error between the desired output and the actual output of the network. There are also other training strategies for multi-layer perceptrons, such as cascade correlation networks and radial basis function networks. And the backpropagation algorithm, which is a learning rule that adjusts the weights based on the error between the predicted output and the actual output. Mathematical representations, such as signal graphs, sigma notation, and vector/matrix notation, can be used to represent and analyze neural network concepts.


# Quizes


### 1. ........................ calculates how active the unit will become on the basis of the total it has received from the input area.
- [X]  Activation area
- [ ]  Input area
- [ ]  Output area
- [ ]  None of the above


  
 


