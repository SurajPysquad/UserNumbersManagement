from django.shortcuts import render, reverse, redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
# from django.views import View
from .models import User, Numbers
from .forms import UserModelForm, NumberModelForm


class MainPageView(TemplateView):
    template_name = "projectindexpage.html"


class UserAddView(FormView):
    template_name = "login_register.html"
    form_class = UserModelForm
    success_url = "/all_user"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserModelForm()
        context['form1'] = NumberModelForm
        return context

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass

    def post(self, request, *args, **kwargs):
        form = UserModelForm(request.POST)
        form1 = NumberModelForm(request.POST)
        print("ALl Numbers Form", form1.data)
        print(form)
        print(form.data)
        print(form.cleaned_data)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create(name=name, email=email, password=password)
            result = dict(form.data)
            numbers = result['mobile']
            for number in tuple(numbers):
                Numbers.objects.create(user_id=user, mobile=number)

            return redirect('alluser')


class ALlUserView(ListView):
    template_name = "all_user_details.html"
    model = User


class UserDeleteView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs['id'])
        del_id = kwargs['id']
        User.objects.get(pk = del_id).delete()
        return reverse('alluser')


class UserUpdateView(UpdateView):
    template_name = "userupdate.html"
    queryset = User.objects.all()

    # queryset1 = Numbers.objects.all()
    fields = '__all__'
    success_url = '/all_user'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        print("******* User Id **********", pk)
        user = User.objects.get(id = pk)
        numbers = Numbers.objects.filter(user_id = user)
        return render(request, self.template_name, {'form': UserModelForm(instance = user),
                                                    'numbers': [NumberModelForm(instance=number) for number in numbers]})

    def post(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        pk = self.kwargs.get(self.pk_url_kwarg)
        user = User.objects.get(id = pk)
        print("******* POST User Id **********", user)
        main_form = UserModelForm(request.POST)

        n = Numbers.objects.filter(user_id=pk).delete()
        result = dict(main_form.data)
        numbers = result['mobile']
        for number in tuple(numbers):
            Numbers.objects.create( user_id = user, mobile = number)
        return super(UserUpdateView, self).post(request, *args, **kwargs)
