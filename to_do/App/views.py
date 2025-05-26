from django.shortcuts import render,redirect,get_object_or_404
from.form import Formfield,Taskfield
from.models import Tasktodo,LoginMatch
x="user"
def login(request):
    if request.method == "POST":
        users=request.POST.get('users', '0')
        passw=request.POST.get('passw', '0')
        verify=LoginMatch.objects.all()
        for match in verify:
            if match.username == users:
                global x
                x=match.username
                return redirect('task')

            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def sign(request):
    if request.method == "POST":
        form = Formfield(request.POST)
        form.save()
        return redirect('login')
    else:
        form = Formfield()
        return render(request, 'signup.html', {'form': form})


def task(request):
    if request.method == "POST":
        boxes=Taskfield(request.POST)
        boxes.save()
        boxes = Taskfield()
        tasklist = Tasktodo.objects.all()
        return render(request, 'Task.html', {'boxes': boxes,'tasklist': tasklist})
    else:
        boxes = Taskfield()
        tasklist = Tasktodo.objects.all()
        return render(request, 'Task.html', {'boxes': boxes,'tasklist': tasklist})


def delete(request, pk):
    done = get_object_or_404(Tasktodo, pk=pk)
    done.delete()
    return redirect('task')
