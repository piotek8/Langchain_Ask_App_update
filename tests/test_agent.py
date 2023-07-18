import unittest
from unittest.mock import patch
import sys
sys.path.append('/Langchain_Ask_App/source_code/')
from ..source_code.app_st import Agent, Program

class AgentTestCase(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()

    def test_use_calculator(self):
        calculation = "2 + 2"
        result = self.agent.use_calculator(calculation)
        self.assertEqual(result, "4")

    def test_use_language_model(self):
        query = "What is the capital of France?"
        result = self.agent.use_language_model(query)
        self.assertTrue(isinstance(result, str))

    def test_search_pdf(self):
        pdf_path = "path/to/pdf.pdf"
        question = "What is the main topic of the document?"
        result = self.agent.search_pdf(pdf_path, question)
        self.assertTrue(isinstance(result, str))

class ProgramTestCase(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        self.program = Program(self.agent)

    def test_language_model(self):
        input_values = ["2", "What is the time now?", "exit"]
        expected_output = "The current time is"
        with patch("builtins.input", side_effect=input_values) as mock_input, patch("sys.stdout") as mock_output:
            mock_output.write = lambda msg: print(msg)
            self.program.run()
            output = mock_output.getvalue().strip()
            self.assertIn(expected_output, output)

    def test_search_pdf(self):
        input_values = ["3", "path/to/pdf.pdf", "What is the main topic of the document?", "exit"]
        expected_output_prefix = "The document's main topic is"
        with patch("builtins.input", side_effect=input_values) as mock_input, patch("sys.stdout") as mock_output:
            mock_output.write = lambda msg: print(msg)
            self.program.run()
            output = mock_output.getvalue().strip()
            self.assertTrue(output.startswith(expected_output_prefix))

if __name__ == "__main__":
    unittest.main()

