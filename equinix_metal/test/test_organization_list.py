# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import equinix_metal
from equinix_metal.models.organization_list import OrganizationList  # noqa: E501
from equinix_metal.rest import ApiException

class TestOrganizationList(unittest.TestCase):
    """OrganizationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationList`
        """
        model = equinix_metal.models.organization_list.OrganizationList()  # noqa: E501
        if include_optional :
            return OrganizationList(
                meta = equinix_metal.models.meta.Meta(
                    first = equinix_metal.models.href.Href(
                        href = '', ), 
                    last = equinix_metal.models.href.Href(
                        href = '', ), 
                    next = , 
                    previous = , 
                    self = , 
                    total = 56, 
                    current_page = 56, 
                    last_page = 56, 
                    href = '', ), 
                organizations = [
                    equinix_metal.models.organization.Organization(
                        address = equinix_metal.models.address.Address(
                            address = '', 
                            address2 = '', 
                            city = '', 
                            coordinates = equinix_metal.models.coordinates.Coordinates(
                                latitude = '', 
                                longitude = '', 
                                href = '', ), 
                            country = '', 
                            state = '', 
                            zip_code = '', 
                            href = '', ), 
                        billing_address = equinix_metal.models.address.Address(
                            address = '', 
                            address2 = '', 
                            city = '', 
                            country = '', 
                            state = '', 
                            zip_code = '', 
                            href = '', ), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        credit_amount = 1.337, 
                        customdata = equinix_metal.models.customdata.customdata(), 
                        description = '', 
                        enforce_2fa_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        logo = bytes(b'blah'), 
                        members = [
                            equinix_metal.models.href.Href(
                                href = '', )
                            ], 
                        memberships = [
                            equinix_metal.models.href.Href(
                                href = '', )
                            ], 
                        name = '', 
                        projects = [
                            
                            ], 
                        terms = 56, 
                        twitter = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        website = '', 
                        href = '', )
                    ], 
                href = ''
            )
        else :
            return OrganizationList(
        )
        """

    def testOrganizationList(self):
        """Test OrganizationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
