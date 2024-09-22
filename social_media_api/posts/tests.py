from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment

class PostsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = get_user_model().objects.create_user(username='user1', password='testpass1')
        self.user2 = get_user_model().objects.create_user(username='user2', password='testpass2')
        self.client.force_authenticate(user=self.user1)

    def test_create_post(self):
        data = {'title': 'Test Post', 'content': 'This is a test post'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_create_comment(self):
        post = Post.objects.create(author=self.user, title='Test Post', content='This is a test post')
        data = {'post': post.id, 'content': 'This is a test comment'}
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().content, 'This is a test comment')

    def test_follow_user(self):
        response = self.client.post(f'/api/accounts/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user1.following.filter(id=self.user2.id).exists())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        response = self.client.post(f'/api/accounts/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user1.following.filter(id=self.user2.id).exists())

    def test_feed(self):
        self.user1.following.add(self.user2)
        Post.objects.create(author=self.user2, title='Test Post', content='This is a test post')
        response = self.client.get('/api/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)