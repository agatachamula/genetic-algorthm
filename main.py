#size of data(number of points
#size of population(10,50,200)
#number of generations (10, 100, 1000)
#mutation probability
#crossover probability
#selection method
#execution time



import numpy as np
from random import choice
import matplotlib.pyplot as plt
import csv
import pandas as pd

def load_points_from_csv(size):
    with open('positive.csv') as csvfile:
        dataset_reader = csv.reader(csvfile)
        labels = []
        features = []
        for row in dataset_reader:
            features.append([int(row[0]), int(row[1])]) # add features

    # convert into a numpy array (not necessary for displaying but might be useful later)
    positive = np.array(features)
    positive= positive[0:size,0:2]

    with open('negative.csv') as csvfile1:
        dataset_reader = csv.reader(csvfile1)
        labels = []
        features = []
        for row in dataset_reader:
            features.append([int(row[0]), int(row[1])]) # add features

    # convert into a numpy array (not necessary for displaying but might be useful later)
    negative = np.array(features)
    negative = negative[0:size, 0:2]


    return(positive,negative)

def points_generator(number, range_bottom, range_up):

    points=np.zeros((number,2),dtype=int)
    for j in range(0,2):
        if (j == 1):
            range_up = range_up * 100
        for i in range(0,number):
            points[i][j]=np.random.randint(range_bottom, range_up,size=1)

    return points

def crossover_and_mutate_one(parent1,parent2):

    sample11= format(parent1, '08b')
    sample22 = format(parent2, '08b')

    pos = int(np.random.randint(1,len(sample11)-1, size=1))
    sample11,sample22= (sample11[:pos]+sample22[pos:], sample22[:pos]+sample11[pos:])

    list2 = list(sample22)
    list1=list(sample11)

    mutation_chance_reverse=10
    if((int(np.random.randint(0, mutation_chance_reverse, size=1)) == 1)):
        bit_to_mutate=int(np.random.randint(0,len(sample11), size=1))
        if(list1[-bit_to_mutate]=='1'):
            list1[-bit_to_mutate]='0'
        else:

            list1[-bit_to_mutate] = '1'

    if (int(np.random.randint(0, mutation_chance_reverse, size=1)) == 1):
        bit_to_mutate = int(np.random.randint(0, len(sample22), size=1))
        if (list2[-bit_to_mutate] == '1'):
            list2[-bit_to_mutate] = '0'
        else:
            list2[-bit_to_mutate] = '1'

    sample11="".join(list1)
    sample22="".join(list2)


    sample1=int(sample11,2)
    sample2 = int(sample22, 2)

    return(sample1, sample2)

def crossover_and_mutate(parents):

    parent1=parents[0]
    parent2=parents[1]
    degree = parent1.shape[0] - 1
    returnValues=np.zeros((2,degree),dtype=int)


    for i in range(0,degree):
        new_values=crossover_and_mutate_one(parent1[i],parent2[i])
        returnValues[0][i]=new_values[0]
        returnValues[1][i] = new_values[1]

    return returnValues


def generate_population(size,degree,down,up):

    population=np.zeros((size,degree),dtype=int)
    for i in range(0,size):
        for j in range(0,degree):
            population[i][j]=np.random.randint(down,up,size=1)
    return population


def countPolynomial(values, coefficients):
    no_of_points=values.shape[0]

    calculated=np.zeros((no_of_points,1),dtype=int)

    for n in range(0,no_of_points):
        for i in range(0,len(coefficients)):
            calculated[n][0]= calculated[n][0] + (values[n][0]**i * coefficients[i])


    return calculated

def polynomial_value(values, coefficients):

    calculated = np.zeros((1,len(values)), dtype=int)
    for j in range(0,len(values)):
        for i in range(0, len(coefficients)-1):
            calculated[0][j] = calculated[0][j] + (values[j] ** i * coefficients[i])
    return np.transpose(calculated)


def fit_function(coefficients, positive, negative):
    sum_positive=0
    sum_negative=0

    calculated_pos=countPolynomial(positive,coefficients)
    calculated_neg=countPolynomial(negative,coefficients)

    #calculate how many positive were classified properly

    for i in range(0, positive.shape[0]):
        if (positive[i][1]>=calculated_pos[i][0]):
            sum_positive=sum_positive+1


    #how many negative calssified properly
    for i in range(0, negative.shape[0]):
        if (negative[i][1]<calculated_neg[i][0]):
            sum_negative=sum_negative+1

    return sum_positive+sum_negative

def tournamentSelection(population, contestants):

    population_size=population.shape[0]
    contestants_values=np.zeros((contestants,population.shape[1]),dtype=int)

    contestant_position=np.random.randint(0,population_size,size=contestants)

    for i in range(0,contestants):
        for j in range(0,population.shape[1]):
            contestants_values[i][j]=population[contestant_position[i]][j]

    position_winner=np.argmax(contestants_values, axis=0)[-1]
    winner1=contestants_values[position_winner]

    position_in_population=contestant_position[position_winner]

    while position_in_population in contestant_position:
        contestant_position = np.random.randint(0, population_size, size=contestants)

    for i in range(0,contestants):
        for j in range(0,population.shape[1]):
            contestants_values[i][j]=population[contestant_position[i]][j]

    position_winner=np.argmax(contestants_values, axis=0)[-1]
    winner2=contestants_values[position_winner]

    return (winner1,winner2)


def new_generation(population, no_of_contestants):

    size = population.shape[0]
    degree=(population.shape[1]-1)
    new_population=np.zeros((2,degree),dtype=int)


    iterations=size//2
    for i in range(0,iterations):
        #select parents
        parents=tournamentSelection(population,no_of_contestants)

        #do crossover and mutate
        new_pop=crossover_and_mutate(parents)

        #save into new population
        if (i==0):
            new_population=new_pop
        elif(i!=0):
            new_population=np.concatenate((new_population,new_pop), axis=0)

    if(size%2==1):
        return new_population[0:-1]

    return new_population



def genetic_algorthm(population, generations, positive, negative, contestants):

    #save best results in matrix
    degree=population.shape[1]
    best=np.zeros((generations,degree+1),dtype=int)

    #generations

    population_size=population.shape[0]
    fit_results=np.zeros((population_size,1),dtype=int)

    for i in range(0,generations):
        fit_results = np.zeros((population_size, 1), dtype=int)
        for j in range(0,population_size):
            fit_results[j][0]=fit_function(population[j],positive, negative)

        #get best in this generation
        pop_plus_fit=np.concatenate((population, fit_results), axis=1)

        position_winner = np.argmax(pop_plus_fit, axis=0)[-1]
        #save best
        best[i]=pop_plus_fit[position_winner]

        #create new generation
        population=new_generation(pop_plus_fit,contestants)

        #perform new generation

    position_winner = np.argmax(best, axis=0)[-1]
    best_parameters= best[position_winner]

    return(best, best_parameters)





def main():
    """
        positive=points_generator(50,-3,10)
        negative=points_generator(50,-10,3)
        pos=pd.DataFrame(positive)
        pos.to_csv("positive.csv", header=None, index=None)
        neg=pd.DataFrame(negative)
        neg.to_csv("negative.csv", header=None, index=None)
        #positive,negative=load_points_from_csv()
    """


    #degree is number of parameters
    degree=3
    population=generate_population(20,degree,-10,10)
    generations=30
    contestants=5
    #points_size from 1 to 50
    points_size=50

    positive, negative = load_points_from_csv(points_size)

    best,best_coef=genetic_algorthm(population,generations,positive,negative,contestants)
    print(best)
    print(best_coef)

    plt.plot(positive[:,0], positive[:,1], 'ro')
    plt.plot(negative[:, 0], negative[:, 1], 'bo')

    X = np.linspace(-10, 10, 51, endpoint=True)
    X=np.reshape(X,(51,1))

    F = countPolynomial(X,best_coef[0:-1])

    plt.plot(X,F)
    plt.show()




if __name__ == '__main__':
    main()