import unittest
import tests_12_3

obj_suite = unittest.TestSuite()
obj_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
obj_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(obj_suite)
