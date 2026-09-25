import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestPaperRAG(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_paper_analysis(self):
        res = self.client.post("/analyze", json={"arxiv_id": "2305.18290", "question": "What is DPO?"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Direct Preference Optimization", res.json()["title"])
        self.assertIn("bibtex", res.json())

if __name__ == "__main__":
    unittest.main()
