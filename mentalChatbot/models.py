from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    client_message = models.TextField()
    filled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class ForumPost(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Post {self.id} - {'Approved' if self.is_approved else 'Pending'}"

class ForumResponse(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name="responses")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Response {self.id} - {'Approved' if self.is_approved else 'Pending'}"






# Create your models here.
