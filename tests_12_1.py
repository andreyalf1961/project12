import module_12_1 as mod
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = mod.Runner('walker')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = mod.Runner('runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_chelenge(self):
        runner_1 = mod.Runner('runner')
        runner_2 = mod.Runner('walker')
        for _ in range(10):
            runner_1.run()
        for _ in range(10):
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
