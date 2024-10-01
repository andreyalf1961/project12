import module_12_2 as mod
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = mod.Runner("Усэйн", 10)
        self.runner_2 = mod.Runner("Андрей", 9)
        self.runner_3 = mod.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            value_new = str(value).replace("'", "")
            print(value_new)

    def test_run_1(self):
        tournament_1 = mod.Tournament(90, self.runner_1, self.runner_3)
        results = tournament_1.start()
        self.assertTrue(results[max(results)] == "Ник")
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_1'] = results

    def test_run_2(self):
        tournament_2 = mod.Tournament(90, self.runner_2, self.runner_3)
        results = tournament_2.start()
        self.assertTrue(results[max(results)] == 'Ник')
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_2'] = results

    def test_run_3(self):
        tournament_3 = mod.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament_3.start()
        self.assertTrue(results[max(results)] == 'Ник')
        for key, value in results.items():
            results[key] = value.name
        self.all_results['tour_3'] = results


if __name__ == '__main__':
    unittest.main()
