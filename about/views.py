from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CollaborateForm
from .models import About


def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()  # pylint: disable=no-member
    if request.method == "POST":
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
            return redirect('about')
    else:
        form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "form": form}
    )
