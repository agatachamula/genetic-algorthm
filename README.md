# Genetic algorithm using Python

This repository consists of implementation of genetic algorothm. 
Influence of parameters of the algorithm is tested with regards to accuracy and time of execution.

## Prerequisites

List of used packages:
* numpy
* random
* matplotlib
* csv
* pandas

## Dataset

Dataset for this task is generated randomly using included points_generator function.
Set of points with labels negative and positive of size from 10 to 100 (with 1:1 ratio) is saved in csv file. 
To ensure fair results of experiments the same dataset is used each time.

## Parameters to experiment with

Parameters that I will be checking: 
* size of dataset (10, 50, 100)
* size of population (10, 30, 200)
* number of generations 
* mutation probability (1, 0.1, 0.01)
* size of contestants group in tournament selection (1, 5, 30)
* degree of polynomial (0, 1, 2, 3, 4, 5)

## Selection method

Tournament selection is a method of selecting parents for crossover – n number of contestants are randomly selected and one with the best fit function value is chosen as a parent for crossover.

## Results

Results were prepared using graphs from graph.py template

* change of dataset size:

 <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image4.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image5.png?raw=true" height="300" width="400">
 
 * change of population size:

 <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image9.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image10.png?raw=true" height="300" width="400">
 
 * change of mutation probability:
 
  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image14.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image15.png?raw=true" height="300" width="400">
  
 * change of size of contestants group in tournament selection:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image19.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image20.png?raw=true" height="300" width="400">

* improment over generations:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image21.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image22.png?raw=true" height="300" width="400">
  
* change of degree of polynomial:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image29.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image30.png?raw=true" height="300" width="400">
  
  



