from django.conf import settings
from sorl.thumbnail import get_thumbnail

def random_with_N(n):
    from random import randint
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def send_mail(recipient=[], subject='', template='', context={}, cc=[]):

    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import render_to_string

    from_ = settings.DEFAULT_FROM_EMAIL
    bodythml = render_to_string(template, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=bodythml,
        from_email="{0} <{1}>".format(settings.APPNAME, from_),
        to=recipient,
        cc=cc
    )
    email.attach_alternative(bodythml, "text/html")
    return email.send()


def get_thumbnail_image(request, image):
    if image:
        try:
            small  = get_thumbnail(image, '350x302', crop='center', quality=50).url
            small = request.build_absolute_uri(small)
        except:
            small = None
        try:
            medium  = get_thumbnail(image, '576x497', crop='center', quality=50).url
            medium =  request.build_absolute_uri(medium)
        except:
            medium = None
        try:
            large  = get_thumbnail(image, '768x662', crop='center', quality=50).url
            large =request.build_absolute_uri(large)
        except:
            large = None
        
        return {
            'small': small,
            'medium': medium,
            'large': large
        }
    return None