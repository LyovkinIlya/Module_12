import unittest
import runner

def repeat_fun(*f):
    """
    Метод для повторений функции(й) 10 раз
    """
    for i in range(10):
        for j in f:
            j()

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn1 = runner.Runner('Runner 1')
        repeat_fun(rn1.walk)
        self.assertEqual(rn1.distance, 50)

    def test_run(self):
        rn2 = runner.Runner('Runner 2')
        repeat_fun(rn2.run)
        self.assertEqual(rn2.distance, 100)

    def test_challenge(self):
        rn3 = runner.Runner('Runner 3')
        rn4 = runner.Runner('Runner 4')
        repeat_fun(rn3.walk, rn4.run)
        self.assertNotEqual(rn3.distance, rn4.distance)

if __name__ == '__main__':
    unittest.main()