import unittest

from rolodex import Rolodex


class TestRolodex(unittest.TestCase):

    """Test Rolodex class."""

    def setUp(self):  # noqa
        self.rolodex = Rolodex()

    def do_inserts(self):
        """Insert some mock data."""
        self.rolodex.insert("Booker T., Washington, 87360, 373 781 7380, yellow")
        self.rolodex.insert("Chandler, Kerri, (623)-668-9293, pink, 123123121")
        self.rolodex.insert("James Murphy, yellow, 83880, 018 154 6474")
        self.rolodex.insert("asdfawefawea")

    def test_no_data_export(self):
        """Test export works without data inserted."""
        self.assertEqual(self.rolodex.export(), {"entries": [], "errors": []})

    def test_insert(self):
        """Test Rolodex.insert()."""

        self.do_inserts()

        #  Check the output
        self.assertEqual(self.rolodex.processed, 4)
        self.assertEqual(self.rolodex.errors, [1, 3])
        entries = [{'color': 'yellow',
                    'lastname': 'Washington',
                    'phonenumber': '373-781-7380',
                    'zipcode': '87360',
                    'firstname': 'Booker T.'},
                   {'color': 'yellow',
                    'lastname': 'Murphy',
                    'phonenumber': '018-154-6474',
                    'zipcode': '83880',
                    'firstname': 'James'}]
        self.assertEqual(self.rolodex.entries, entries)

    def test_export(self):
        """Test the main export function."""
        self.do_inserts()
        d = self.rolodex.export()
        expected = {'errors': [1, 3], 'entries': [{'color': 'yellow', 'lastname': 'Murphy', 'phonenumber': '018-154-6474', 'zipcode': '83880', 'firstname': 'James'}, {'color': 'yellow', 'lastname': 'Washington', 'phonenumber': '373-781-7380', 'zipcode': '87360', 'firstname': 'Booker T.'}]}  # noqa
        self.assertEqual(d, expected)

    def test_export_json(self):
        """Test the json export function runs."""
        self.do_inserts()
        s = self.rolodex.export_json()
        self.assertTrue(len(s) > 300)   # Basic test to make sure it prints more than an empty entries and error list

if __name__ == '__main__':
    unittest.main()
