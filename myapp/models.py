from django.db import models
from django.utils import timezone

class TextContent(models.Model):
    # Types of text content
    CONTENT_TYPE_CHOICES = [
        ('ARTICLE', 'Article'),
        ('NOVEL', 'Novel'),
        ('STORY', 'Story'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default='ARTICLE')
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Campo para imágenes
    video_url = models.URLField(blank=True, null=True)  # Campo para la URL del video
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text_content = models.ForeignKey(TextContent, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.text_content.title}'
