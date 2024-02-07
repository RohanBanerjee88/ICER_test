import unittest
import yaml

class TestManifestYAML(unittest.TestCase):
    def test_manifest_structure(self):
        with open('/Users/rohanbanerjee/ICER/manifest.yml', 'r') as file:
            manifest_data = yaml.safe_load(file)

            # Check if the file contains required keys
            self.assertIn('name', manifest_data)
            self.assertIn('category', manifest_data)
            self.assertIn('subcategory', manifest_data)
            self.assertIn('role', manifest_data)
            self.assertIn('description', manifest_data)

    def test_placeholders_filled(self):
        with open('/Users/rohanbanerjee/ICER/manifest.yml', 'r') as file:
            manifest_content = file.read()

            # Check if placeholders are filled
            self.assertNotIn('![Name of your app]!', manifest_content)
            self.assertNotIn('![Subcategory of your app]!', manifest_content)
            self.assertNotIn('![Description of your app]!', manifest_content)

if __name__ == '__main__':
    unittest.main()
