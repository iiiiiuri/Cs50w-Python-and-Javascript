from django import template
from network.models import Post

register = template.Library()

@register.filter
def is_liked_by_user(post, user):
    return post.likes.filter(id=user.id).exists()

@register.filter
def is_followed_by_user(user, profile_user):
    return user.following.filter(id=profile_user.id).exists()