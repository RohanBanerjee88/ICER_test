import unittest
import yaml

class TestFormYAML(unittest.TestCase):
    def setUp(self):
        with open('/Users/rohanbanerjee/ICER/form.yml', 'r') as file:
            self.form_data = yaml.safe_load(file)

    def test_required_keys_present(self):
        # Ensure required keys are present in the form.yml
        self.assertIn('cluster', self.form_data)
        self.assertIn('form', self.form_data)
        self.assertIn('attributes', self.form_data)

    def test_attributes_definition(self):
        # Check if the 'attributes' section contains expected attribute definitions
        attributes = self.form_data.get('attributes', {})

        # Example checks for a few attribute definitions
        self.assertIn('is_vnc', attributes)
        self.assertIn('modules', attributes)
        self.assertIn('num_cores', attributes)
        # Add similar checks for other attribute definitions as needed

    def test_attributes_representation_rules(self):
        # Validate representation rules for specific attributes
        attributes = self.form_data.get('attributes', {})

        # Example representation rules checks for 'num_cores' attribute
        num_cores_info = attributes.get('num_cores', {})
        self.assertEqual(num_cores_info['widget'], 'number_field')
        self.assertEqual(num_cores_info['label'], 'Number of cores per task')
        self.assertEqual(num_cores_info['value'], 1)
        self.assertEqual(num_cores_info['min'], 0)
        self.assertEqual(num_cores_info['max'], 128)
        self.assertEqual(num_cores_info['step'], 1)
        # Add similar checks for other attribute representation rules

if __name__ == '__main__':
    unittest.main()
