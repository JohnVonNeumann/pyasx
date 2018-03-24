"""
Unit tests for the pyasx.data.companies module
"""


import unittest
import unittest.mock
import pyasx.data.companies


class CompaniesTest(unittest.TestCase):


    def __init__(self, *args, **kwargs):
        super(CompaniesTest, self).__init__(*args, **kwargs)

        self.get_listed_companies_data = []
        self.get_listed_companies_mock = []


    def setUp(self):

        self.get_listed_companies_data = [
            # just the first ones from the file to test with
            [ "MOQ LIMITED", "MOQ", "Software & Services" ],
            [ "1-PAGE LIMITED", "1PG", "Software & Services" ],
            [ "1300 SMILES LIMITED", "ONT", "Health Care Equipment & Services" ],
            [ "1ST GROUP LIMITED", "1ST", "Health Care Equipment & Services" ],
        ]

        # build the mock CSV data based on self.get_listed_companies_data

        for i in range(0, 3):  # header
            self.get_listed_companies_mock.append("\n")

        for row in self.get_listed_companies_data:

            csv_row = ",".join(row)
            csv_row += "\n"

            self.get_listed_companies_mock.append(csv_row)


    def testGetListedCompaniesMocked(self):
        """
        Unit test for pyasx.data.company.get_listed_companies()
        Test pulling mock data + verify
        """

        with unittest.mock.patch("requests.get") as mock:

            # set up mock iterator for response.iter_content()
            instance = mock.return_value
            instance.iter_content.return_value = iter(self.get_listed_companies_mock)

            # this is the test
            companies = pyasx.data.companies.get_listed_companies()

            # verify data is all correct
            i = 0;
            for company in companies:
                company_data = self.get_listed_companies_data[i]

                self.assertEqual(company["name"], company_data[0])
                self.assertEqual(company["ticker"], company_data[1])
                self.assertEqual(company["gics"], company_data[2])

                i += 1


    def testGetListedCompaniesSimple(self):
        """
        Unit test for pyasx.data.company.get_listed_companies()
        Simple check of pulling live data
        """

        companies = pyasx.data.companies.get_listed_companies()
        self.assertTrue(len(companies) > 1000) # there are atleast a couple thousand listed companies


    def testGetCompanyInfo(self):

        companies = pyasx.data.companies.get_company_info('CBA')

        annoucements = pyasx.data.companies.get_company_annoucements('CBA')
        # print(annoucements)
