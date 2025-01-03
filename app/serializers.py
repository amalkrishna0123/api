from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:  # Meta should be used to define model and fields
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]
