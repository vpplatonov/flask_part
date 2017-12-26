# project/tests/test_users.py


import json

from project.tests.base import BaseTestCase
from project import create_app

app = create_app()


class TestSendersService(BaseTestCase):
    """Tests for the Users Service."""

    def test_all_senders(self):
        """Ensure get all senders behaves correctly."""
        with self.client:
            response = self.client.get('/settings/senders')
            if response.status == 'error':
                self.assertEqual(response.status, "error")
                return
            data = json.loads(response.data.decode())
            self.assertTrue('id' in data['data']['senders'][0])
            self.assertTrue('status' in data['data']['senders'][0])
            self.assertTrue('login' in data['data']['senders'][0])
            self.assertTrue('label' in data['data']['senders'][0])
            self.assertIn('s170503t03', data['data']['senders'][0]['label'])
