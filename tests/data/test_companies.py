

import unittest
import unittest.mock
import pyasx.data
import pyasx.data.companies


class CompaniesTest(unittest.TestCase):
    """
    Unit tests for pyasx.data.companies module
    """


    def __init__(self, *args, **kwargs):
        super(CompaniesTest, self).__init__(*args, **kwargs)

        self.get_listed_companies_data = []
        self.get_listed_companies_mock = ""
        self.get_company_info_mock = []
        self.get_company_announcements_mock = []


    def setUp(self):

        self.setUpGetListedCompanies()
        self.setUpGetCompanyInfo()
        self.setUpGetCompanyAnnouncements()


    def setUpGetListedCompanies(self):

        self.get_listed_companies_data = [
            # just the first ones from the file to test with
            # the fields for Pharmaceuticals and Food have been changed to use ampersands
            # instead of commas due to the way we're doing the mocks, change in the future
            # probably just read from a series of mock files, would make it cleaner
            ["14D", "1414 DEGREES LIMITED", "2018-09-12", "Capital Goods", "19592589"],
            ["1AD", "ADALTA LIMITED", "2016-08-22", "Pharmaceuticals & Biotechnology & Life Sciences", "15709237"],
            ["1AE", "AURORA ENERGY METALS LIMITED", "2022-05-18", "Materials", "37791912"],
            ["1AG", "ALTERRA LIMITED", "2008-05-16", "Food & Beverage & Tobacco", "10433288"],
            ["1MC", "MORELLA CORPORATION LIMITED", "2001-01-08", "Materials", "144141145"]
        ]

        # build the mock CSV data based on self.get_listed_companies_data

        self.get_listed_companies_mock += "\n"

        for row in self.get_listed_companies_data:

            csv_row = ",".join(row)
            csv_row += "\n"

            self.get_listed_companies_mock += csv_row


    def setUpGetCompanyInfo(self):

        # mock data in structure returned by the ASX API
        self.get_company_info_mock = {
            "code":                  "GEN",
            "name_full":             "GENERIC INCORPORATED",
            "name_short":            "GEN INC",
            "name_abbrev":           "GENERIC INC",
            "principal_activities":  "ACTIVITIES",
            "industry_group_name":   "Banks",
            "sector_name":           "Financials",
            "listing_date":          "2000-01-01T00:00:00+1000",
            "delisting_date":        None,
            "web_address":           "WEBSITE",
            "mailing_address":       "ADDRESS",
            "phone_number":          "4321 4321",
            "fax_number":            "1234 1234",
            "registry_name":         "REG NAME",
            "registry_address":      "REG ADDRESS",
            "registry_phone_number": "1800 123 456",
            "foreign_exempt":        False,
            "primary_share_code":    "GEN",  # so it pulls valid pricing info
            "recent_announcement":   False,
            "products":[
                "shares",
                "hybrid-securities",
                "options",
                "warrants"
            ]
        }


    def setUpGetCompanyAnnouncements(self):

        # mock data in structure returned by the ASX API
        self.get_company_announcements_mock = {
            "data": [
                {
                    "id": "12341234",
                    "document_date": "2018-03-15T00:00:00+1100",
                    "document_release_date": "2018-03-14T00:00:00+1100",
                    "url": "FULL URL",
                    "relative_url": "RELATIVE URL",
                    "header": "TITLE",
                    "market_sensitive": True,
                    "number_of_pages": 101,
                    "size": "200.1MB",
                    "legacy_announcement": False
                },
                {
                    "id": "43214321",
                    "document_date": "2018-03-12T00:00:00+1100",
                    "document_release_date": "2018-03-11T00:00:00+1100",
                    "url": "FULL URL",
                    "relative_url": "RELATIVE URL",
                    "header": "TITLE",
                    "market_sensitive": True,
                    "number_of_pages": 202,
                    "size": "100.2MB",
                    "legacy_announcement": True
                },

            ]
        }


    def testGetListedCompaniesMocked(self):
        """
        Unit test for pyasx.data.company.get_listed_companies()
        Test pulling mock data + verify
        """

        with unittest.mock.patch("requests.get") as mock:

            # set up mock iterator for response.iter_content()
            instance = mock.return_value
            instance.iter_content.return_value = iter([self.get_listed_companies_mock])

            # this is the test
            companies = pyasx.data.companies.get_listed_companies()

            # verify data is all correct
            i = 0;
            for company in companies:
                company_data = self.get_listed_companies_data[i]

                self.assertEqual(company["ticker"], company_data[0])
                self.assertEqual(company["name"], company_data[1])
                self.assertEqual(company["listing_date"], company_data[2])
                self.assertEqual(company["gics_industry"], company_data[3])
                self.assertEqual(company["market_cap"], company_data[4])

                i += 1


    def testGetListedCompaniesLive(self):
        """
        Unit test for pyasx.data.company.get_listed_companies()
        Simple check of pulling live data
        """

        companies = pyasx.data.companies.get_listed_companies()
        self.assertTrue(len(companies) > 1000) # there are atleast a couple thousand listed companies


    def testGetCompanyInfoMocked(self):
        """
        Unit test for pyasx.data.company.get_company_info()
        Test pulling mock data + verify
        """

        with unittest.mock.patch("requests.get") as mock:

            # set up mock iterator for response.json()
            instance = mock.return_value
            instance.json.return_value = self.get_company_info_mock

            company = pyasx.data.companies.get_company_info('CBA')

            self.assertEqual(company["ticker"], "GEN")
            self.assertEqual(company["name"], "GENERIC INCORPORATED")
            self.assertEqual(company["name_short"], "GENERIC INC")
            self.assertEqual(company["principal_activities"], "ACTIVITIES")
            self.assertEqual(company["gics_industry"], "Banks")
            self.assertEqual(company["gics_sector"], "Financials")
            self.assertEqual(pyasx.data._format_date(company["listing_date"]), "2000-01-01T00:00:00+1000")
            self.assertTrue(company["delisting_date"] is None)
            self.assertEqual(company["website"], "WEBSITE")
            self.assertEqual(company["mailing_address"], "ADDRESS")
            self.assertEqual(company["phone_number"], "4321 4321")
            self.assertEqual(company["fax_number"], "1234 1234")
            self.assertEqual(company["registry_name"], "REG NAME")
            self.assertEqual(company["registry_phone_number"], "1800 123 456")
            self.assertEqual(company["foreign_exempt"], False)
            self.assertTrue(len(company["products"]))
            self.assertTrue(len(company["last_dividend"]))
            self.assertTrue(len(company["primary_share"]))


    def testGetCompanyInfoLive(self):
        """
        Unit test for pyasx.data.company.get_listed_companies()
        Simple check of pulling live data
        """

        company = pyasx.data.companies.get_company_info('CBA')
        self.assertTrue("ticker" in company)
        self.assertTrue(len(company))


    def testGetCompanyAnnouncementsMocked(self):
        """
        Unit test for pyasx.data.company.get_company_announcements()
        Test pulling mock data + verify
        """

        with unittest.mock.patch("requests.get") as mock:

            # set up mock iterator for response.json()
            instance = mock.return_value
            instance.json.return_value = self.get_company_announcements_mock

            # this is the test
            announcements = pyasx.data.companies.get_company_announcements('CBA')

            # verify data is all correct against the mock data
            i = 0;
            for announcement in announcements:
                announcement_data = self.get_company_announcements_mock['data'][i]

                self.assertEqual(announcement["title"], announcement_data["header"])
                self.assertEqual(announcement["url"], announcement_data["url"])

                self.assertEqual(
                    pyasx.data._format_date(announcement["document_date"]),
                    announcement_data["document_date"]
                )

                self.assertEqual(
                    pyasx.data._format_date(announcement["release_date"]),
                    announcement_data["document_release_date"]
                )

                self.assertEqual(announcement["num_pages"], announcement_data["number_of_pages"])
                self.assertEqual(announcement["size"], announcement_data["size"])

                i += 1


    def testGetCompanyAnnouncementsLive(self):
        """
        Unit test for pyasx.data.company.get_company_annoucements()
        Simple check of pulling live data
        """

        announcements = pyasx.data.companies.get_company_announcements('CBA')
        self.assertTrue(len(announcements))

    def test_get_company_info_with_incorrect_ticker_length_raises_exception(self):
        """
        The Company Info API will not find any data for any ticker that is not 3
        chars long.
        """

        with self.assertRaises(ValueError):
            pyasx.data.companies.get_company_info(ticker="A")

        with self.assertRaises(ValueError):
            pyasx.data.companies.get_company_info(ticker="AA")

        with self.assertRaises(ValueError):
            pyasx.data.companies.get_company_info(ticker="AAAA")

        with self.assertRaises(ValueError):
            pyasx.data.companies.get_company_info(ticker="AAAAA")

        with self.assertRaises(ValueError):
            pyasx.data.companies.get_company_info(ticker="AAAAAA")
