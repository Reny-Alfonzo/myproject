from django.shortcuts import render, get_object_or_404, redirect
from .models import TextContent, Comment
from .forms import CommentForm
from .forms import TextContentForm

def home(request):
    # Obtener todos los contenidos de texto
    text_contents = TextContent.objects.all()
    return render(request, 'myapp/home.html', {'text_contents': text_contents})
def text_content_detail(request, pk):
    text_content = get_object_or_404(TextContent, pk=pk)
    comments = text_content.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.text_content = text_content
            comment.save()
            return redirect('text_content_detail', pk=text_content.pk)
    else:
        form = CommentForm()

    return render(request, 'myapp/text_content_detail.html', {
        'text_content': text_content,
        'comments': comments,
        'form': form,
    })

def text_content_create(request):
    if request.method == 'POST':
        form = TextContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página principal después de guardar
    else:
        form = TextContentForm()
    return render(request, 'myapp/text_content_form.html', {'form': form})

def text_content_edit(request, pk):
    text_content = get_object_or_404(TextContent, pk=pk)
    if request.method == 'POST':
        form = TextContentForm(request.POST, request.FILES, instance=text_content)
        if form.is_valid():
            form.save()
            return redirect('text_content_detail', pk=text_content.pk)
    else:
        form = TextContentForm(instance=text_content)
    return render(request, 'myapp/text_content_form.html', {'form': form})