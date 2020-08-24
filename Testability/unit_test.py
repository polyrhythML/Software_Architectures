import datetime
import unittest
from unittest.mock import patch

class DateTimeHelper:

    def today(self):
        """
        :return: current data/time.
        """
        return datetime.datetime.now()

    def date(self):
        """
        :return: today's date in the form of DD/MM/YY.
        """
        return self.today().strftime("%d/%m/%Y")

    def weekday(self):
        """
        :return: the day of the week for today.
        """
        return self.today().strftime("%A")

    def us_to_indian(self, date):
        """
        :return: Convert U.S. Style date mm/dd/yyyy to Indian style dd/mm/yyyy
        """
        mm, dd, yy = date.split("/")
        yy = int(yy)

        if yy <= 16:
            yy += 2000

        date_obj = datetime.date(year=yy, month=int(mm), day=int(dd))
        return date_obj.strftime("%d/%m/%Y")


# Create DateTimeHelperTestCase class

class DateTimeHelperTestCase(unittest.TestCase):

    def test_us_indian(self):

        # Test a few dates
        d1 = "9/01/2012"
        d2 = "02/09/1992"
        d3 = "05/10/2019"

        print("Testing US to Indian Conversion ...")
        self.obj = DateTimeHelper()

        # Perform the conversion check
        self.assertEqual(self.obj.us_to_indian(d1), "01/09/2012")
        self.assertEqual(self.obj.us_to_indian(d2), "09/02/1992")
        self.assertEqual(self.obj.us_to_indian(d3), "10/05/2019")
        print("Test Cases Passed ...")

    def test_date(self):

        # Test the helper's date method
        print("Testing date method  ...")
        self.obj = DateTimeHelper()
        # Put a specific date to test
        my_date = datetime.datetime(year=2016, month=8, day=16)

        # Patch the 'today' method with a specific return value
        with patch.object(self.obj, 'today', return_value=my_date):
            response = self.obj.date()
            self.assertEqual(response, '16/08/2016')
        print("Test case passed !!")

    def test_weekday(self):
        """ Test weekday() method """
        print("Testing weekday method  ...")
        self.obj = DateTimeHelper()
        # Put a specific date to test
        my_date = datetime.datetime(year=2016, month=8, day=21)
        # Patch the 'today' method with a specific return value
        with patch.object(self.obj, 'today', return_value=my_date):
            response = self.obj.weekday()
            self.assertEqual(response, 'Sunday')
        print("Test case passed !!")


if __name__ == "__main__":
    unittest.main()


