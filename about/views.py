from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About Me page with the most recent About content.
    """
    about = About.objects.all().order_by('-updated_on').first()  # pylint: disable=no-member
    
    return render(
        request,
        "about/about.html",
        {"about": about}
    )
