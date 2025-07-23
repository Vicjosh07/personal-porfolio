from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def cloudinary_resize(image_url, dimensions):
    """
    Applies Cloudinary transformations to resize images.
    Usage: {{ image.url|cloudinary_resize:"w_2200,h_1400,c_fill" }}
    """
    if not image_url:
        return ''
    
    # Add transformation parameters to the URL
    if '?' in image_url:
        return f"{image_url}&{dimensions}"
    else:
        return f"{image_url}?{dimensions}"

@register.filter
def cloudinary_thumbnail(image_url, size="w_300,h_200,c_fill"):
    """
    Creates thumbnail versions of images using Cloudinary.
    Usage: {{ image.url|cloudinary_thumbnail }}
    Usage: {{ image.url|cloudinary_thumbnail:"w_150,h_150,c_thumb" }}
    """
    if not image_url:
        return ''
    
    if '?' in image_url:
        return f"{image_url}&{size}"
    else:
        return f"{image_url}?{size}"

@register.filter
def cloudinary_optimize(image_url, quality="auto"):
    """
    Applies Cloudinary optimization parameters.
    Usage: {{ image.url|cloudinary_optimize }}
    Usage: {{ image.url|cloudinary_optimize:"q_80,f_auto" }}
    """
    if not image_url:
        return ''
    
    optimization = f"q_{quality},f_auto" if quality == "auto" else quality
    
    if '?' in image_url:
        return f"{image_url}&{optimization}"
    else:
        return f"{image_url}?{optimization}"