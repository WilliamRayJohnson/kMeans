'''
William Ray Johnson
'''

import math

class Clusteror():
    def __init__(self, centroids, dataSet):
        self.centroids = centroids
        self.trainingSet = dataSet[:int(len(dataSet) * 0.8)]
        self.testSet = dataSet[int(len(dataSet) * 0.8):]
    
    def distanceFormula(self, pointOne, pointTwo):
        a = pointOne[0] - pointTwo[0]
        b = pointOne[1] - pointTwo[1]
        
        return math.sqrt(a**2 + b**2)
        
    def categorizeData(self, categories, dataSet):
        categorizedData = []
        for category in categories:
            categorizedData.append([]);
                
        for point in dataSet:
            smallestDistance = float("inf")
            pointsCategory = 0
            for category in categories:
                distance = self.distanceFormula(point, category)
                if distance < smallestDistance:
                    smallestDistance = distance
                    pointsCategory = categories.index(category)
            
            categorizedData[pointsCategory].append(point)
            
        return categorizedData
        
    def recalculateCentroids(self, centroids, categorizedData):
        newCentroids = []
        for category in categorizedData:
            xTotal = 0
            yTotal = 0
            for point in category:
                xTotal += point[0]
                yTotal += point[1]
            xTotal += centroids[categorizedData.index(category)][0]
            yTotal += centroids[categorizedData.index(category)][1]
            newCentroid = [xTotal/(len(category) + 1), yTotal/(len(category) + 1)]
            newCentroids.append(newCentroid)
        
        return newCentroids
        
    def train(self, movementThreshold):
        thresholdMet = False
        while not thresholdMet:
            categorizedData = self.categorizeData(self.centroids, self.trainingSet)
            newCentroids = self.recalculateCentroids(self.centroids, categorizedData)
            for category in range(len(self.centroids)):
                centroidDistance = self.distanceFormula(newCentroids[category], self.centroids[category])
                if centroidDistance <= movementThreshold:
                    thresholdMet = True
                else:
                    thresholdMet = False
                    
            self.centroids = newCentroids