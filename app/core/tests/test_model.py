from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """test_create_user_with_email_successful"""
        email = 'testemail@gmail.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email) 
        self.assertTrue(user.check_password(password))
        

    def test_new_user_email_normalized(self):
        """test_new_user_email_normalized"""
        email = 'mhaikeljay@GMAIL.COM'

        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """test_new_user_invalid_email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """test_create_new_super_user"""
        user = get_user_model().objects.create_superuser(
            'mhaikeljay@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)