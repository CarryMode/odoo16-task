from odoo.tests.common import TransactionCase

class TestDevelopersManagement(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Developer = self.env["developers.management.developer"]
        self.Company = self.env["developers.management.company"]

    def test_01_create_developer(self):
        """Test basic developer creation"""
        dev = self.Developer.create({
            "name": "John",
            "type": "backend",
            "email": "john@test.com",
        })

        self.assertTrue(dev)
        self.assertEqual(dev.name, "John")
        self.assertEqual(dev.type, "backend")

    def test_02_global_identification_computed(self):
        """Check compute field global_identification"""
        dev = self.Developer.create({
            "name": "Alice",
            "type": "front-end",
        })

        self.assertEqual(dev.global_identification, "Alice-front-end")

        dev.type = "backend"
        dev._compute_global_identification()

        self.assertEqual(dev.global_identification, "Alice-backend")

    def test_03_company_relation(self):
        """Test linking developer to a company (Many2one/One2many)"""
        company = self.Company.create({
            "name": "TechCorp",
            "address": "123 Street",
        })

        dev = self.Developer.create({
            "name": "Bob",
            "type": "fullstack",
            "company_id": company.id,
        })

        self.assertEqual(dev.company_id, company)

        self.assertIn(dev, company.developers_ids)
