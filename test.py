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

    def testAddition(self):
        expect_ten = {"operation": "add", "values": [1, 4, -7, 12]}
        expect_ten_response = { 'result': 10 }
        ten = MathEngine.handleRequest(self.math_engine, expect_ten)
        self.assertEqual(expect_ten_response, ten)

    def testSubtraction(self):
        json_in = {"operation": "subtract", "values": [4, 1]}
        res = MathEngine.handleRequest(self.math_engine, json_in)
        self.assertEqual({"result": 3}, res)

    def testMultiplication(self):
        json_in = {"operation": "multiply", "values": [4, 3]}
        res = MathEngine.handleRequest(self.math_engine, json_in)
        self.assertEqual({"result": 12}, res)

    def testDivision(self):
        json_in = {"operation": "divide", "values": [15, 3]}
        res = MathEngine.handleRequest(self.math_engine, json_in)
        self.assertEqual({"result": 5}, res)

unittest.main()
