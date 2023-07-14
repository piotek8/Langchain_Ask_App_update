import unittest

from agent import Agent


class TestAgent(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self._subject = Agent()

    def test_get_agent_response(self):
        question = "moje pytanie"

        response = self._subject.get_agent_response(question)
        self.assertEqual("moja odpowiedz", response)
