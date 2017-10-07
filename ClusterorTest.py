'''
William Ray Johnson
'''

import unittest

import Clusteror

class ClusterorTest(unittest.TestCase):
    def setUp(self):
        self.clustorer = Clusteror.Clusteror([[-3, 3],[3, -3]], [[-4, 4],[-4, 3],[-3, 4],[4, -4],[0, 0]])
    
    def testDistanceFormula(self):
        pointOne = [0,0]
        pointTwo = [6,8]
        expectedDistance = 10.0
        actualDistance = self.clustorer.distanceFormula(pointOne, pointTwo)
        
        self.assertEqual(expectedDistance, actualDistance)
        
    def testCategorizeData(self):
        categories = [[-3, 3],[3, -3]]
        dataSet = [[-4, 4],[-4, 3],[-3, 4],[4, -4]]
        expectedCategorizedData = [[[-4, 4],[-4, 3],[-3, 4]],[[4, -4]]]
        actualCategorizedData = self.clustorer.categorizeData(categories, dataSet)
        
        self.assertEqual(len(expectedCategorizedData[0]), len(actualCategorizedData[0]))
        self.assertEqual(len(expectedCategorizedData[1]), len(actualCategorizedData[1]))
        
    def testRecalculateCentroids(self):
        categorizedData = [[[-4, 4],[-4, 3],[-3, 4]],[[4, -4]]]
        centroids = [[-3, 3],[3, -3]]
        expectedNewCentroids = [[-3.5, 3.5],[3.5, -3.5]]
        actualNewCentroids = self.clustorer.recalculateCentroids(centroids, categorizedData)
        
        self.assertEqual(expectedNewCentroids, actualNewCentroids)
        
    def testTrain(self):
        dataSet = [[-4, 4],[-4, 3],[-3, 4],[4, -4]]
        expectedCategorizedData = [[[-4, 4],[-4, 3],[-3, 4]],[[4, -4]]]
        self.clustorer.train(0.0000000000001)
        actualCategorizedData = self.clustorer.categorizeData(self.clustorer.centroids, dataSet)
        
        self.assertEqual(len(expectedCategorizedData[0]), len(actualCategorizedData[0]))
        self.assertEqual(len(expectedCategorizedData[1]), len(actualCategorizedData[1]))
        
if __name__ == '__main__':
    unittest.main()