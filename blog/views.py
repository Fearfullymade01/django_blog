from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Show approved comments, plus any unapproved comments by the logged-in user
    comments = post.comments.filter(
        Q(approved=True) | Q(author=request.user)
    ).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Handle new comment submissions
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to add a comment.")
            return redirect("account_login")
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, "Comment submitted and awaiting approval.")
            return redirect("post_detail", slug=slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "form": form,
        },
    )


@require_http_methods(["POST"])
def edit_comment(request, slug, comment_id):
    """
    Edit a comment if the user is the comment author.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    # Defensive programming: check if the user is the comment author
    if comment.author != request.user:
        messages.error(request, "You cannot edit a comment that is not yours.")
        return redirect("post_detail", slug=slug)

    # Update the comment body
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("post_detail", slug=slug)
        else:
            messages.error(request, "Error updating comment.")

    return redirect("post_detail", slug=slug)


@require_http_methods(["POST"])
def delete_comment(request, slug, comment_id):
    """
    Delete a comment if the user is the comment author.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    # Defensive programming: check if the user is the comment author
    if comment.author != request.user:
        messages.error(request, "You cannot delete a comment that is not yours.")
        return redirect("post_detail", slug=slug)

    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect("post_detail", slug=slug)
