from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

from .models import post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username = 'username1', password = 'abc123'
        )
        testuser1.save()


        testpost = post.objects.create(
            author = testuser1, title='Blog Test 1', body = 'This is the test body'
        )
        testpost.save()


    def test_blog_content(self):
        post_obj = post.objects.get(id=1)
        author = f'{post_obj.author}'
        title = f'{post_obj.title}'
        body = f'{post_obj.body}'

        self.assertEqual(author, 'username1')
        self.assertEqual(title, 'Blog Test 1')
        self.assertEqual(body, 'This is the test body')
