# Run all the tests in the project
import unittest

from apps.mathengine.engine import MathEngine


class EngineTestCase(unittest.TestCase):
    def setUp(self):
        self.math_engine = MathEngine()
        pass

    def testSimpleAddition(self):
    	json_in = { "operation": "add", "values": [1, 4] }
        expected_response = { 'result': 5 }
        response = MathEngine.handleRequest(self.math_engine, json_in)
        self.assertEqual(expected_response, response)

unittest.main()
