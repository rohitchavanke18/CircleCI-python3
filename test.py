import unittest
from main import to_upper
class MyTestCase(unittest.TestCase):
    def test_to_uppper(self):
        name="Rohit"
        upper_name=to_upper(name)
        self.assertEqual(upper_name,"Rohit")

    if __name__=='__main__':
        unittest.main()