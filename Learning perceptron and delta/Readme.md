
# Overview

A single-layer perceptron is a type of artificial neural network that consists of a single main unit, or neuron, which receives input from other units (called dummy units) and produces an output according to a threshold function. Single-layer perceptrons can be used to perform simple operations such as computing truth tables (e.g. AND and OR) and classifying patterns. However, they have limitations in their ability to solve more complex problems and are not able to process non-linear relationships. Multi-layer perceptrons, on the other hand, consist of multiple layers of neurons and can process more complex relationships. They can be trained using the error backpropagation algorithm, which adjusts the weights of the connections between neurons based on the error between the predicted and actual output. There are also alternative training strategies for multi-layer perceptrons, such as cascade correlation networks and radial basis function networks.


# Layers and learning in artificial neural networks:

## Single-layer perceptrons:

A single-layer perceptron is a type of artificial neural network that consists of a single main unit, or neuron, which receives input from other units (called dummy units) and produces an output according to a threshold function. The main unit accumulates the weighted sum of the stimulus from the input units and then calculates its activation according to a threshold function.

Single-layer perceptrons can be used to perform simple operations such as computing truth tables (e.g. AND and OR) and classifying patterns. Given the importance of the recognition and classification of patterns in natural intelligence, this is an important application of single-layer perceptrons.

However, single-layer perceptrons have limitations in their ability to solve more complex problems and are not able to process non-linear relationships. This is because they only have a single layer of neurons, and thus cannot capture the complexity of more advanced relationships.

## Geometry: input space

The input space of a single-layer perceptron refers to the range of possible input values that the network can receive. If the input values can only be the integer values 1 or 0, as they would be in a truth table computation, then the only parts of the space that are available are the four corners of the square labeled in the figure: (x1 = 0, x2 = 0), (x1 = 1, x2 = 0), (x1 = 0, x2 = 1) and (x1 = 1, x2 = 1). However, if the input values can take real number values, then a possible input can be any point within the whole of the space depicted.

When the system classifies its inputs, it is dividing or partitioning the space of inputs into two parts. This partitioning line is quite arbitrary and there are countless other lines that could have been drawn that would do just as well. However, in what sense, then, is our perceptron learning? It is learning to draw the line that best separates the two classes of inputs.

## Geometry: weight space

The weight space of a single-layer perceptron refers to the range of possible values for the weights of the connections between the input units and the main unit. The weights of the connections can be adjusted to modify the behavior of the network.

# single-layer perceptrons training

There are two main training strategies for single-layer perceptrons: 
* The perceptron rule  <br>
The perceptron rule is a simple algorithm for adjusting the weights of the connections between the input units and the main unit in a single-layer perceptron. It is based on the idea of minimizing the error between the predicted output and the actual output.

* The delta rule <br>

The delta rule is a more general training algorithm that can be applied to any single-layer perceptron, regardless of the specific threshold function used. It is based on the idea of minimizing the error between the predicted output and the actual output by adjusting the weights of the connections between the input units and the main unit.

## Limitations of single-layer perceptrons

Despite their simplicity and usefulness in certain applications, single-layer perceptrons have several limitations. They are not able to process non-linear relationships and are therefore not suitable for solving more complex problems. They also have difficulty learning to classify patterns that are not linearly separable.

# Multi-layer perceptrons

Multi-layer perceptrons are a type of artificial neural network that consist of multiple layers of neurons. They are more powerful and effective than single-layer perceptrons because they can process more complex relationships.



The structure of a multi-layer perceptron consists of an input layer, one or more hidden layers, and an output layer. The input layer receives the input data, the hidden layers process the data, and the output layer produces the final output.

##  error backpropagation.

One of the most well-known training algorithms for multi-layer perceptrons is error backpropagation. This algorithm adjusts the weights of the connections between the neurons in the network based on the error between the predicted and actual output.

The process of error backpropagation involves the following steps:

Forward propagation: The input data is passed through the network, layer by layer, and the output of each neuron is calculated based on the weights of its connections and a non-linear activation function.

Calculating the error: The error between the predicted output and the actual output is calculated.

## Backward propagation: <br>
The error is backpropagated through the network, layer by layer, and the weights of the connections between the neurons are adjusted based on the error and a learning rate.

Repeat: The process is repeated until the error is minimized or reaches a satisfactory level.

The error surface of a multi-layer perceptron refers to the landscape of possible weight configurations and the corresponding error values. The goal of the error backpropagation algorithm is to find the weights that result in the lowest error, or the global minimum of the error surface.

There are several factors that can affect the training of a multi-layer perceptron using error backpropagation, such as the learning rate, the choice of activation function, and the number of hidden layers and neurons.

## Alternatives to backpropagation

There are several alternatives to error backpropagation for training multi-layer perceptrons, such as cascade correlation networks and radial basis function networks.

Cascade correlation networks are a type of artificial neural network that can learn to add new neurons to the network during training. This allows them to adapt to changing data and improve their performance over time.

Radial basis function networks are a type of artificial neural network that use radial basis functions as their activation function. They are particularly useful for solving problems with continuous inputs and outputs, such as function approximation and time series prediction.


#  Neural topology


* Feedforward: <br>
In a layered network topology, there are multiple layers of units, with all units in a layer connected to all units in the next layer, but not to units in other layers or within the same layer. The activity flows from the input layer through to the output layer in a feedforward manner. This type of network is commonly used for classification tasks, as it is able to process the input data and make a prediction based on the weights of the connections between the units.This is the most common network topology, where the units are arranged in layers and all units in a layer are connected to all units in the next layer, but not to units in other layers or within the same layer. Activity in a feedforward network flows from the input layer through to the output layer.
- application: classification 

* Lattice: <br>
In a lattice network topology, the units are arranged in a single sheet, with excitatory and inhibitory connections between them. Units tend to excite other units in their neighborhood and inhibit those further away. This type of network is useful for modeling spatial patterns, as it is able to capture the relationships between units based on their proximity to each other. This type of network has units arranged in a single sheet, with excitatory and inhibitory connections between them. Units tend to excite other units in their neighborhood and inhibit those further away.

* Recurrent: <br>
In a recurrent network topology, the units feed activity back to other units, except to themselves. There are delays on the feedback links, such that all feedback is synchronized. This allows the network to process sequences of data and maintain information over time, as the activity of the units is influenced by the activity of the units in previous time steps. Recurrent networks have dynamic behavior, meaning that they can exhibit complex temporal patterns of activity. This type of network is well-suited for tasks such as language modeling and time series prediction. This type of network has units that feed activity back to other units, except to themselves. There are delays on the feedback links, such that all feedback is synchronized. Recurrent networks have dynamic behavior.

Each of these network topologies has its own unique features and can be used for different types of tasks and applications. For example, feedforward networks are commonly used for classification tasks, lattice networks are useful for modeling spatial patterns, and recurrent networks are well-suited for processing sequences of data and maintaining information over time.
