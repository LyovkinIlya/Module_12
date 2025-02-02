import rt_with_exceptions
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = rt_with_exceptions.Runner(10, 20)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {r1}')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r2 = rt_with_exceptions.Runner('R2', -10)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

