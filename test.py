from ast import Constant
import unittest, json
from project.app import app



class TestWord2Number(unittest.TestCase):

    def setUp(self):
        self.tester=app.test_client(self)

    def test_get_status_code(self):
        response=self.tester.get("/dubbeltech")
        self.assertEqual(response.status_code, 200)

    def test_get_return_proper_number(self):
        response=self.tester.get("/dubbeltech")
        data= json.loads(response.get_data())
        self.assertEqual(data[0]["owner"]["id"], 33356252)
        
 
if __name__ == "__main__":
    unittest.main

