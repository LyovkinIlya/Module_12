import unittest
import runner_and_tournament as rt

class tournamentTest(unittest.TestCase):
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

    def test_r1_r3(self):
        t = rt.Tournament(90, self.r1, self.r3)
        res = t.start()
        self.all_results["r1_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")

    def test_r2_r3(self):
        t = rt.Tournament(90, self.r2, self.r3)
        res = t.start()
        self.all_results["r2_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")

    def test_r1_r2_r3(self):
        t = rt.Tournament(90, self.r1, self.r2, self.r3)
        res = t.start()
        self.all_results["r1_r2_r3"] = res
        self.assertTrue(res[max(res.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()