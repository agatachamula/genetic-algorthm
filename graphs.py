import matplotlib.pyplot as plt

def main():
    filename = input('Enter a file name: ')

    X = [0,1,2,3,4,5]
    Y=[0.78,0.92,0.91,0.88,0.88,0.89]

    #plt.ylabel('Generation with best result')
    plt.ylabel('Accuracy of result')

    plt.plot(X,Y)

    plt.xlabel('Degree of polynomial')


    plt.show()

    x = [[9, 5, 9], [7, 8, 9]]
    print(x)




if __name__ == '__main__':
    main()