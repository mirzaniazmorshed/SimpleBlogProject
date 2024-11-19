from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def add_post(request):
    if request.method == "POST": #user post req korche
        post_form = forms.PostForm(request.POST) #user er post req data ekhane capture korlam
        if post_form.is_valid(): #post kora data valid kina check korechi
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save() #data valid hole database e save korbo
            return redirect('add_post') #sob thik thakle ei url e pathai dibo post 
    else:
        post_form = forms.PostForm() #user normally website e gele blank form pabe
    return render(request, 'add_post.html', {'form': post_form})    

#Add post using class based view
@method_decorator(login_required, name='dispatch') #non logged in user acces na paoyar jonno
class AddPostCreateView(CreateView):
    model = models.Post # models.py te amader age Post name e model chilo
    form_class = forms.PostForm  # je form k dekhaite chai
    template_name = 'add_post.html' # age je template render korsi seta
    success_url = reverse_lazy('add_post') #return redirect kora
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == "POST":
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
    return render(request, 'add_post.html', {'form': post_form})    

#edit post using class based view
@method_decorator(login_required, name='dispatch')
class EditPostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'  #pk = id ta acccept korar jonno
    success_url = reverse_lazy('profile')

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

#delete post using class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')
    
class DetailPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'    
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()        
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
