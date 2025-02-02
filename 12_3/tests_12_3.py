import unittest
import runner
import runner_and_tournament as rt

def repeat_fun(*f):
    """
    Метод для повторений функции(й) 10 раз
    """
    for i in range(10):
        for j in f:
            j()

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        rn1 = runner.Runner('Runner 1')
        repeat_fun(rn1.walk)
        self.assertEqual(rn1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        rn2 = runner.Runner('Runner 2')
        repeat_fun(rn2.run)
        self.assertEqual(rn2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        rn3 = runner.Runner('Runner 3')
        rn4 = runner.Runner('Runner 4')
        repeat_fun(rn3.walk, rn4.run)
        self.assertNotEqual(rn3.distance, rn4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = rt.Runner("Усэйн", 10)
        self.r2 = rt.Runner("Андрей", 9)
        self.r3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r1_r3(self):
        t = rt.Tournament(90, self.r1, self.r3)
        res = t.start()
        self.all_results["r1_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r2_r3(self):
        t = rt.Tournament(90, self.r2, self.r3)
        res = t.start()
        self.all_results["r2_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_r1_r2_r3(self):
        t = rt.Tournament(90, self.r1, self.r2, self.r3)
        res = t.start()
        self.all_results["r1_r2_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()