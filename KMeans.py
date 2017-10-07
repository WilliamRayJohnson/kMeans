'''
William Ray Johnson
'''

import random
import Clusteror

def main():
    categories = [[5,5], [5,-5], [-5,5], [-5,-5]]
    dataSetSize = 100
    trainingThreshold = 0.000000000000000001
    dataSet = []
    
    for point in range(dataSetSize):
        dataSet.append([random.uniform(-10, 10), random.uniform(-10, 10)])
        
    clusteror = Clusteror.Clusteror(categories, dataSet)
    clusteror.train(trainingThreshold)
    
    for centroid in range(len(clusteror.centroids)):
        print("Category " + str(centroid) + ": " + str(clusteror.centroids[centroid]))
    
if __name__ == '__main__':
    main()