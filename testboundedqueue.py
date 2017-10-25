import unittest
import boundedqueue

class TestBoundedQueue(unittest.TestCase):
      
    def test_enqueue_dequeue_1(self):
        self.bq = boundedqueue.BoundedQueue(5)
        for i in range(5):
            self.bq.enqueue(i)
        self.assertEqual(self.bq.dequeue(), 0)
        self.assertEqual(self.bq.dequeue(), 1)
        self.assertEqual(self.bq.dequeue(), 2)
        self.assertEqual(self.bq.dequeue(), 3)
        self.assertEqual(self.bq.dequeue(), 4)


    def test_enqueue_dequeue_2(self):
        self.bq = boundedqueue.BoundedQueue(1)
        self.bq.enqueue(0)
        self.assertFalse(self.bq.enqueue(1))
       

if __name__ == '__main__':
    unittest.main(exit=False)