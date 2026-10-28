import unittest
from fastapi.testclient import TestClient
from app import app, account

class TestBankingAPI(unittest.TestCase):
    def setUp(self):
        account["balance"] = 0.0 
        self.client = TestClient(app)

    def test_deposit(self):
        res = self.client.post("/deposit", json={"amount": 100.0})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["balance"], 100.0)

    def test_insufficient_funds_withdrawal(self):
        self.client.post("/deposit", json={"amount": 50.0})
        res = self.client.post("/withdraw", json={"amount": 100.0})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json()["detail"], "Insufficient funds.")

if __name__ == "__main__":
    unittest.main()
