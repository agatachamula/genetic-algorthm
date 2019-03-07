# Genetic algorithm with parameters experiments using Python

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
 
 Fewer samples tend to get result faster, but with less accuracy. When we have more points “anomalies” don’t affect the result so much that is why we get steadily increasing accuracy over generations.
 
 * change of population size:

 <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image9.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image10.png?raw=true" height="300" width="400">
 
 With bigger population size we get result faster – there is a bigger chance of bigger result being in first population. Quality also slightly increases with increasing of populations size for the same reason.
 
 * change of mutation probability:
 
  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image14.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image15.png?raw=true" height="300" width="400">
  
  My samples don’t show any pattern. It seems it is the best to choose moderate value of mutation probability.
  
 * change of size of contestants group in tournament selection:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image19.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image20.png?raw=true" height="300" width="400">
  
  When we have one contestant it means we randomly choose parents for next generation. We have best result very soon since result can’t improve when we choose random samples to crossover. With 30 contestants only two best samples have children which very soon leads to not enough variability in population to improve result. Best is to choose parents “semi-randomly” – parents with better results have better probability of being chosen.

* improvement over generations:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image21.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image22.png?raw=true" height="300" width="400">
  
  Accuracy improves with generations. The dependence looks similar to logarithmic dependence. Accuracy improves rapidly in initial generations and slows down in later generations.
  
* change of degree of polynomial:

  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image29.png?raw=true" height="300" width="400">  <img src="https://github.com/agatachamula/genetic-algorthm/blob/master/Results/image30.png?raw=true" height="300" width="400">
  
  Generally we tend to get results later with bigger degree and accuracy seems to be also improving. Degree of polynomial is specific  to specific set of points. In points generated in my experiment it seems the best suiting function is linear function.



