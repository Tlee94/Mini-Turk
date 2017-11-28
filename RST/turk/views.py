from django.shortcuts import render, get_object_or_404
from .models import Profile, Job, Bidder
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import JobForm, UserForm, FormToSuperUser
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

#url - views - html

# home page
def index(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'turk/index.html', context)


# profile page
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'turk/detail.html',  {'user': user})

'''
def job_description(request, user_id, job_id):
    user = get_object_or_404(User, pk=user_id)
    job = Job.objects.get(pk=job_id)
    context = {
        'user': user,
        'job': job,
        'lowest_bid': job.lowest_bid,
    }
    return render(request, 'turk/job_description.html', context)
    '''


def job_description(request, user_id, job_id):
    user = get_object_or_404(User, pk=user_id)
    job = Job.objects.get(pk=job_id)

    bid_list = job.bidder_set.all()
    lowest_bid = -1
    count = job.bidder_set.count()

    if count > 0:
        lowest_bid = bid_list[0].price
        for bid in bid_list:
            if bid.price < lowest_bid:
                lowest_bid = bid.price
        '''for i in range(0, count):
            if bid_list[i].price < lowest_bid:
                lowest_bid = bid_list[i].price'''
        job.lowest_bid = lowest_bid

    context = {
        'user': user,
        'job': job,
    }
    return render(request, 'turk/job_description.html', context)


def create_job(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'turk/login.html')
    else:
        user = get_object_or_404(User, pk=user_id)
        form = JobForm(request.POST or None)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = user
            job.save()
            return render(request, 'turk/detail.html', {'user': user})
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'turk/create_job.html', context)
    # profile = get_object_or_404(Profile, pk=profile_id)
    # return render(request, 'turk/create_job.html', {'profile': profile})


def form_to_superuser(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'turk/login.html')
    else:
        user = get_object_or_404(User, pk=user_id)
        form = FormToSuperUser(request.POST or None)
        if form.is_valid():
            ftsu = form.save(commit=False)
            ftsu.user = user
            ftsu.save()
            return render(request, 'turk/detail.html', {'user': user})
        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'turk/form_to_superuser.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'turk/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_jobs = Job.objects.all()
                context = {
                    'all_jobs': all_jobs,
                }
                return render(request, 'turk/index.html', context)
            else:
                return render(request, 'turk/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'turk/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'turk/login.html')


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'email', 'age', 'gender', 'money']
    success_url = reverse_lazy('turk:index')
    #success_url = reverse_lazy('turk:detail', args=[id])


class JobDelete(DeleteView):
    model = Job

    def get_success_url(self):
        return reverse('turk:index')
    #success_url = reverse_lazy('turk:index')


# Registration   'turk:update_profile' user.id user.profile.id
class UserFormView(View):
    form_class = UserForm
    template_name = 'turk/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # clean data
            username = form.cleaned_data['username'] # 'username' = field
            password = form.cleaned_data['password']
            user.set_password(password)
            user.is_active = False
            user.save()

            # request User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is None:
                all_jobs = Job.objects.all()
                context = {
                    'all_jobs': all_jobs,
                }
                return render(request, 'turk/index.html', context)

        return render(request, self.template_name, {'form': form})

