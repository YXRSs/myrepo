import unittest
import boundedqueue

class TestBoundedQueue(unittest.TestCase):
      
    def test_enqueue_dequeue_1(self):
        '''
        test for enqueue dequeue with a lenth of 5
        '''
        self.bq = boundedqueue.BoundedQueue(5)
        for i in range(5):
            self.bq.enqueue(i)
        self.assertEqual(self.bq.dequeue(), 0)
        self.assertEqual(self.bq.dequeue(), 1)
        self.assertEqual(self.bq.dequeue(), 2)
        self.assertEqual(self.bq.dequeue(), 3)
        self.assertEqual(self.bq.dequeue(), 4)


    def test_enqueue_dequeue_2(self):
        '''
        test enqueue for exceed capacity
        '''
        self.bq = boundedqueue.BoundedQueue(1)
        self.bq.enqueue(0)
        self.bq.enqueue(1)
        self.assertEqual(self.bq.dequeue(), 0)
    
    
    def test_size(self):
        '''
        test size of queue
        '''
        self.bq = boundedqueue.BoundedQueue(0)
        self.assertEqual(self.bq.size(), 0) 
        self.bq2 = boundedqueue.BoundedQueue(5)
        for i in range(5):
            self.bq2.enqueue(i)        
        self.assertEqual(self.bq2.size(), 5)
    
    
    def test_is_empty(self):
        '''
        test is_empty function
        '''
        self.bq = boundedqueue.BoundedQueue(1)
        self.assertTrue(self.bq.is_empty())
        self.bq.enqueue(0)
        self.assertFalse(self.bq.is_empty())
        
        
    def test_init_with_iter(self):
        '''
        test for inititial queue with iter type
        '''
        self.bq = boundedqueue.BoundedQueue(5,[0,1,2,3,4,5])
        self.assertEqual(self.bq.size(), 5)
        self.assertFalse(self.bq.is_empty())
        self.assertEqual(self.bq.dequeue(), 0)
        self.assertEqual(self.bq.dequeue(), 1)
        self.assertEqual(self.bq.dequeue(), 2)
        self.assertEqual(self.bq.dequeue(), 3)
        self.assertEqual(self.bq.dequeue(), 4)        
        
        
    def test_iter_unusual_case(self):
        '''
        test for iter exceed queue's capacity
        '''
        self.bq = boundedqueue.BoundedQueue(3,[0,1,2,3,4,5])
        self.assertEqual(self.bq.size(), 3)        
        self.assertFalse(self.bq.is_empty())
        self.assertEqual(self.bq.dequeue(), 0)
        self.assertEqual(self.bq.dequeue(), 1)
        self.assertEqual(self.bq.dequeue(), 2)
    
    
    def test_long_queue(self):
        '''
        test a queue with lenth of 100
        '''
        self.bq = boundedqueue.BoundedQueue(100)
        for i in range(100):
            self.bq.enqueue(i)
        self.assertEqual(self.bq.size(), 100)
        for ii in range(100):
            self.assertEqual(self.bq.dequeue(), ii)
            
        
       
if __name__ == '__main__':
    unittest.main(exit=False)