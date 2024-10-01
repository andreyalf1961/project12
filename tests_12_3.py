import module_12_1 as mod1
import module_12_2 as mod
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = mod1.Runner('walker')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = mod1.Runner('runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = mod1.Runner('runner')
        runner_2 = mod1.Runner('walker')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner_1 = mod.Runner("Усэйн", 10)
        self.runner_2 = mod.Runner("Андрей", 9)
        self.runner_3 = mod.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            value_new = str(value).replace("'", "")
            print(value_new)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_1(self):
        tournament_1 = mod.Tournament(90, self.runner_1, self.runner_3)
        results = tournament_1.start()
        self.assertTrue(results[max(results)] == "Ник")
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_1'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_2(self):
        tournament_2 = mod.Tournament(90, self.runner_2, self.runner_3)
        results = tournament_2.start()
        self.assertTrue(results[max(results)] == 'Ник')
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_2'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run_3(self):
        tournament_3 = mod.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament_3.start()
        self.assertTrue(results[max(results)] == 'Ник')
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_3'] = results


if __name__ == '__main__':
    unittest.main()
