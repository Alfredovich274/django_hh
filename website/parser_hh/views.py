from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Vacancy, Param, Schedule, Experience, Skill, Specialization
from .forms import ContactForm, CreateParams
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .mymixins import AuthorPermissionMixin


# Create your views here.
#  @login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail('Contact message',
                      f'Ваш сообщение {message}, {name}, принято',
                      'from@example.com',
                      [email],
                      fail_silently=True,
                      )
            return HttpResponseRedirect(reverse('parser:index'))
        else:
            return render(request, 'parser_hh/contacts.html',
                          context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'parser_hh/contacts.html',
                      context={'form': form})


class ParamsListView(ListView):
    model = Param
    template_name = 'parser_hh/index.html'
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.id:
            return Param.active_objects.filter(author_id=self.request.user.id)
        else:
            return Param.active_objects.all()


class VacancyListView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'parser_hh/results.html'


@login_required
def create_params(request):
    if request.method == 'POST':
        form = CreateParams(request.POST, files=request.FILES)
        if form.is_valid():
            # Добавить в форму текущего пользователя request.user
            form.instance.author = request.user
            form.save()
        return HttpResponseRedirect(reverse('parser:index'))
    else:
        form = CreateParams()
        return render(request, 'parser_hh/create-options.html',
                      context={'form': form})


# class CreateNewParams(CreateView):
#     fields = '__all__'
#     model = Param
#     success_url = reverse_lazy('parser:index')
#     template_name = 'parser_hh/create-options.html'
#
#     def form_valid(self, form):
#         """
#         Метод срабатывает после того как форма валидна
#         :param form:
#         :return:
#         """
#         return super().form_valid(form)


class ParamsDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'parser_hh/delete-params.html'
    model = Param
    success_url = reverse_lazy('parser:index')

    def test_func(self):
        obj = self.get_object()  # рабочий вариант, но необходим объект
        return self.request.user.is_superuser or obj.author == self.request.user


class VacancyDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'parser_hh/delete-vacancy.html'
    model = Vacancy
    success_url = reverse_lazy('parser:results')

    def test_func(self):
        obj = self.get_object()  # рабочий вариант, но необходим объект
        return self.request.user.is_superuser or obj.author == self.request.user


class VacancyDetailView(UserPassesTestMixin, DetailView):
    model = Vacancy
    template_name = 'parser_hh/vacancy.html'

    def test_func(self):
        obj = self.get_object()  # рабочий вариант, но необходим объект
        return self.request.user.is_superuser or obj.author == self.request.user

    # def has_permission(self):
    #     return self.get_object().author == self.request.user


# class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     template_name = 'post_edit.html'
#     fields = ['title', 'body']
#
#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user
