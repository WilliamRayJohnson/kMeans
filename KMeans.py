'''
William Ray Johnson
'''

import random
import Clusteror

def main():
    fourCategories = [[5,5], [5,-5], [-5,5], [-5,-5]]
    sixCategories = [[5,5], [5,-5], [-5,5], [-5,-5], [0,5], [0,-5]]
    dataSetSize = 100000
    trainingThreshold = 0.000000000000000001
    dataSet = []
    
    for point in range(dataSetSize):
        dataSet.append([random.uniform(-10, 10), random.uniform(-10, 10)])
    
    print("Training with 4 Categories.... \n")
    clusteror4K = Clusteror.Clusteror(fourCategories, dataSet)
    clusteror4K.train(trainingThreshold)
    testSet4K = clusteror4K.categorizeData(clusteror4K.centroids, clusteror4K.testSet)
    print("Test Set Results:")
    
    for centroid in range(len(clusteror4K.centroids)):
        print("Category " + str(centroid) + ": " + str(len(testSet4K[centroid])) + " values")
        print("\t Old Center: " + str(fourCategories[centroid]))
        print("\t New Center: " + str(clusteror4K.centroids[centroid]))
        
    print("Training with 6 Categories.... \n")
    clusteror6K = Clusteror.Clusteror(sixCategories, dataSet)
    clusteror6K.train(trainingThreshold)
    testSet6K = clusteror6K.categorizeData(clusteror6K.centroids, clusteror6K.testSet)
    print("Test Set Results:")
    
    for centroid in range(len(clusteror6K.centroids)):
        print("Category " + str(centroid) + ": " + str(len(testSet6K[centroid])) + " values")
        print("\t Old Center: " + str(sixCategories[centroid]))
        print("\t New Center: " + str(clusteror6K.centroids[centroid]))
    
if __name__ == '__main__':
    main()