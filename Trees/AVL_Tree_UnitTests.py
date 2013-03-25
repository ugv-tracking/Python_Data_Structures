#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/--/2013

from AVL_Tree import AVLTree
import unittest
import random

class TestAVL(unittest.TestCase):
    
    def setUp(self):
        self.avl = AVLTree()
        self.fullAVL = AVLTree()
        
        self.insertList = [47,30,2,6,12,64,62,98,93,95,97,99,3,4,5,7]
        for item in self.insertList:
            self.assertTrue(self.fullAVL.insert(item))
        self.result = '(None)<-93(BF:1)->(6,97)\n'\
                 '(93)<-6(BF:0)->(4,30)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(6)<-4(BF:1)->(3,5)\n'\
                 '(6)<-30(BF:0)->(12,62)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(4)<-3(BF:1)->(2,None)\n'\
                 '(4)<-5(BF:0)->(None,None)\n'\
                 '(30)<-12(BF:1)->(7,None)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(3)<-2(BF:0)->(None,None)\n'\
                 '(12)<-7(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'
        
        
    def testEmpty(self):
        self.assertEqual(self.avl.outputTesting(),'(Empty)')
        self.assertFalse(self.avl.find(1))
        self.assertEqual(self.avl.findMax(),None)
        self.assertEqual(self.avl.findMin(),None)
        self.assertFalse(self.avl.delete(1))
        self.assertTrue(self.avl.insert(5))
        self.assertEqual(self.avl.outputTesting(),'(None)<-5(BF:0)->(None,None)\n')
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        self.assertTrue(self.avl.insert(47))
        string = '(None)<-47(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(30))
        string = '(None)<-47(BF:1)->(30,None)\n'\
                 '(47)<-30(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(2))
        string = '(None)<-30(BF:0)->(2,47)\n'\
                 '(30)<-2(BF:0)->(None,None)\n'\
                 '(30)<-47(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(6))
        string = '(None)<-30(BF:1)->(2,47)\n'\
                 '(30)<-2(BF:-1)->(None,6)\n'\
                 '(30)<-47(BF:0)->(None,None)\n'\
                 '(2)<-6(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(12))
        string = '(None)<-30(BF:1)->(6,47)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-47(BF:0)->(None,None)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(64))
        string = '(None)<-30(BF:0)->(6,47)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-47(BF:-1)->(None,64)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(47)<-64(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(62))
        string = '(None)<-30(BF:0)->(6,62)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(98))
        string = '(None)<-30(BF:-1)->(6,62)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-62(BF:-1)->(47,64)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:-1)->(None,98)\n'\
                 '(64)<-98(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(93))
        string = '(None)<-30(BF:-1)->(6,62)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-62(BF:-1)->(47,93)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-93(BF:0)->(64,98)\n'\
                 '(93)<-64(BF:0)->(None,None)\n'\
                 '(93)<-98(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(95))
        string = '(None)<-30(BF:-1)->(6,93)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-93(BF:0)->(62,98)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(93)<-62(BF:0)->(47,64)\n'\
                 '(93)<-98(BF:1)->(95,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(98)<-95(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(97))
        string = '(None)<-30(BF:-1)->(6,93)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-93(BF:0)->(62,97)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(93)<-62(BF:0)->(47,64)\n'\
                 '(93)<-97(BF:0)->(95,98)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(99))
        string = '(None)<-93(BF:0)->(30,97)\n'\
                 '(93)<-30(BF:0)->(6,62)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(30)<-6(BF:0)->(2,12)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(6)<-2(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(3))
        string = '(None)<-93(BF:1)->(30,97)\n'\
                 '(93)<-30(BF:1)->(6,62)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(30)<-6(BF:1)->(2,12)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(6)<-2(BF:-1)->(None,3)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(2)<-3(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(4))
        string = '(None)<-93(BF:1)->(30,97)\n'\
                 '(93)<-30(BF:1)->(6,62)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(30)<-6(BF:1)->(3,12)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(6)<-3(BF:0)->(2,4)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(3)<-2(BF:0)->(None,None)\n'\
                 '(3)<-4(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        
        self.assertTrue(self.avl.insert(5))
        string = '(None)<-93(BF:1)->(30,97)\n'\
                 '(93)<-30(BF:1)->(4,62)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(30)<-4(BF:0)->(3,6)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(4)<-3(BF:1)->(2,None)\n'\
                 '(4)<-6(BF:0)->(5,12)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(3)<-2(BF:0)->(None,None)\n'\
                 '(6)<-5(BF:0)->(None,None)\n'\
                 '(6)<-12(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)

        self.assertTrue(self.avl.insert(7))
        string = '(None)<-93(BF:1)->(6,97)\n'\
                 '(93)<-6(BF:0)->(4,30)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(6)<-4(BF:1)->(3,5)\n'\
                 '(6)<-30(BF:0)->(12,62)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(4)<-3(BF:1)->(2,None)\n'\
                 '(4)<-5(BF:0)->(None,None)\n'\
                 '(30)<-12(BF:1)->(7,None)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(3)<-2(BF:0)->(None,None)\n'\
                 '(12)<-7(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'
        self.assertEqual(self.avl.outputTesting(),string)
        print('\ntextInsert PASSED')
        
    #def testDFSorder(self):
    #    print("\ntestDFS(pre&in&post)order PASSED")

    def testFind(self):
        self.assertEqual(self.fullAVL.outputTesting(),self.result)
        
        random.shuffle(self.insertList)
        for item in self.insertList:
            self.assertTrue(self.fullAVL.find(item))
        
        #FAIL FIND
        failFinds = [x for x in range(0,101)]
        for item in self.insertList:
            if item in failFinds:
                failFinds.remove(item)
        for item in failFinds:
            self.assertFalse(self.fullAVL.find(item))

        print("\ntestFind PASSED")
        
    def testDuplicateInsert(self):
        self.assertEqual(self.fullAVL.outputTesting(),self.result)
        
        #Duplicate Insert should fail and NOT change the output
        for item in self.insertList:
            self.assertFalse(self.fullAVL.insert(item))
        self.assertEqual(self.fullAVL.outputTesting(),self.result)
        
        print("\ntestDuplicateInsert PASSED")
        
    def testCopy(self):
        self.assertEqual(self.fullAVL.outputTesting(),self.result)
        
        copy = self.fullAVL.copyTree()
        self.assertEqual(copy.outputTesting(),self.result)
        
        self.assertTrue(self.fullAVL.insert(1))
        self.assertTrue(copy.insert(0))
        
        #fullAVL after inserting 1
        newResult = '(None)<-93(BF:1)->(6,97)\n'\
                 '(93)<-6(BF:0)->(4,30)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(6)<-4(BF:1)->(2,5)\n'\
                 '(6)<-30(BF:0)->(12,62)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(4)<-2(BF:0)->(1,3)\n'\
                 '(4)<-5(BF:0)->(None,None)\n'\
                 '(30)<-12(BF:1)->(7,None)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(2)<-1(BF:0)->(None,None)\n'\
                 '(2)<-3(BF:0)->(None,None)\n'\
                 '(12)<-7(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'
        #The copy after inserting 0
        newCopy = '(None)<-93(BF:1)->(6,97)\n'\
                 '(93)<-6(BF:0)->(4,30)\n'\
                 '(93)<-97(BF:-1)->(95,98)\n'\
                 '(6)<-4(BF:1)->(2,5)\n'\
                 '(6)<-30(BF:0)->(12,62)\n'\
                 '(97)<-95(BF:0)->(None,None)\n'\
                 '(97)<-98(BF:-1)->(None,99)\n'\
                 '(4)<-2(BF:0)->(0,3)\n'\
                 '(4)<-5(BF:0)->(None,None)\n'\
                 '(30)<-12(BF:1)->(7,None)\n'\
                 '(30)<-62(BF:0)->(47,64)\n'\
                 '(98)<-99(BF:0)->(None,None)\n'\
                 '(2)<-0(BF:0)->(None,None)\n'\
                 '(2)<-3(BF:0)->(None,None)\n'\
                 '(12)<-7(BF:0)->(None,None)\n'\
                 '(62)<-47(BF:0)->(None,None)\n'\
                 '(62)<-64(BF:0)->(None,None)\n'
        
        self.assertEqual(self.fullAVL.outputTesting(),newResult)
        self.assertEqual(copy.outputTesting(),newCopy)
        print("\ntestCopy PASSED")
    
    #def testFindMin(self):
    #    print("\ntestFindMin PASSED")
    #    
    #def testFindMax(self):
    #    print("\ntestFindMax PASSED")
    #    
    #def testDeleteLeaf(self):  
    #    print("\ntestDeleteLeaf PASSED")
    #    
    #def testDeleteFail(self): 
    #    print("\ntestDeleteFail PASSED")
    #
    #def testDeleteInternal(self):
    #    print("\ntestDeleteInternal PASSED")
    #    
    #def testDeleteRoot(self): 
    #    print("\ntestDeleteRoot PASSED")
    
    def testListSort(self):
        listToSort = [x for x in range(0,101,1)]
        random.shuffle(listToSort)
        for value in listToSort:
            self.avl.insert(value)
            
        sortedList = self.avl.traverseDFSinorder()
        self.assertEqual(sortedList,[x for x in range(0,101,1)])
        print("\ntestListSort PASSED")
    
if __name__ == '__main__':
    unittest.main()