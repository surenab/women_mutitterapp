from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Kling,KlingComment
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,View,DetailView
from .forms import KlingForm, MessageForm,KlingCommentForm, UserProfileForm, SubscriberForm, CommentReplyForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import KlingFilter
from django.core.paginator import Paginator
from django.db.models.functions import Length
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Base(LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class CreateKling(CreateView):
    form_class = KlingForm
    success_url = reverse_lazy("home")
    template_name = "create_kling.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,"Klinged succesfully!")
        return super().form_valid(form)

def image_view(request):
 
    if request.method == 'POST':
        form = KlingForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('create_kling')
    else:
        form = KlingForm()
    return render(request, 'create_kling.html', {'form': form})    

class MyKling(ListView):
    model = Kling
    context_object_name = "klings"
    form_class = KlingForm
    success_url = reverse_lazy("profile")
    paginate_by = 4

    def get_queryset(self):
        queryset = Kling.objects.filter(user=self.request.user)
        return queryset

class MyKlingUpdate(LoginRequiredMixin, UpdateView):
    model = Kling
    context_object_name = "kling"
    form_class = KlingForm
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        queryset = super(MyKlingUpdate, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "Kling instance is updated!")
        return super().form_valid(form)

class MyKlingDelete(LoginRequiredMixin, DeleteView):
    model = Kling
    context_object_name = "kling"
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        queryset = super(MyKlingDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class Home(FilterView):
    model = Kling
    context_object_name = 'klings'
    filterset_class = KlingFilter
    template_name = "homepage.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Kling.objects.order_by('-created_on')
        return queryset.annotate(text_length=Length('text'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = KlingFilter()  # Create an instance of KlingFilter without data
        return context

    def post(self, request, *args, **kwargs):
        filter = KlingFilter(request.POST)
        klings = self.filter_queryset(self.get_queryset())

        if filter.is_valid():
            # Access form data directly from the 'filter' instance
            if filter.cleaned_data['title_text']:
                klings = klings.filter(title_text__icontains=filter.cleaned_data['title_text'])
            if filter.cleaned_data['kling_category']:
                klings = klings.filter(kling_category__icontains=filter.cleaned_data['kling_category'])

        context = self.get_context_data(filter=filter, klings=klings)
        return self.render_to_response(context)

    
def about(request):
    return render(request, 'about.html')

class KlingDetailview(DetailView):
    model = Kling
    template_name = "post.html"
    context_object_name = "kling"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Kling = self.get_object()
        context['comments'] = KlingComment.objects.filter(kling=Kling)
        context['comment_form'] = KlingCommentForm
        context['reply_form'] = CommentReplyForm() 
        return context

class KlingCommentView(View):
    def post(self, request, pk):
        kling = get_object_or_404(Kling, pk=pk)
        form = KlingCommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = self.request.user
            comment.kling = kling
            comment.save()
            return redirect('post', pk=kling.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class CommentReplyView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(KlingComment, pk=comment_id)
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = self.request.user
            reply.comment = comment
            reply.save()
            return redirect('post', pk=comment.kling.pk)
        else:
            return HttpResponse("Form validation failed", status=400) 


def kling_list(request):
    klings = Kling.objects.all() 
    paginator = Paginator(klings, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'kling_list.html', context)

class MessageView(View):
    template_name = 'contact.html'
    success_url = reverse_lazy("home")
    
    def get(self, request):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        return render(request, self.template_name, {'form': form})
    
class CreateKlingComment(CreateView):
    model = KlingComment
    form_class= KlingCommentForm
    success_text="Created!"

    def get_success_url(self) -> str:
        return reverse_lazy("post", kwargs ={"pk": self.request.POST.get("Kling")})
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Kling comment created!")
        return super().form_valid(form)
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    my_kling_view = MyKling()
    my_kling_view.request = request  
    my_kling_view.form_class = KlingForm  
    my_kling_view.success_url = reverse_lazy("profile")  
    my_kling_view.paginate_by = 4  
    user_klings = my_kling_view.get_queryset()

    return render(request, 'profile/view_profile.html', {'user_profile': user_profile, 'user_klings': user_klings})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile/edit_profile.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            subject = 'Thanks for subscribing to Cackling'
            message = render_to_string('confirmation_email.html', {'subscriber': subscriber})
            plain_message = strip_tags('Tahnk You! You have subscribed to Cackling newsletter!')
            from_email = 'klingcackling@gmail.com '
            recipient_list = [subscriber.email]
            send_mail(subject, plain_message, from_email, recipient_list, html_message=message)
            messages.success(request, 'Thank you for subscribing! A confirmation email has been sent to your inbox.')
            return redirect('home')
    else:   
        form = SubscriberForm()
    return render(request, 'base_core.html', {'form': form})