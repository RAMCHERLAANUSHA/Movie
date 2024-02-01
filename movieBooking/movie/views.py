
from django.shortcuts import render,redirect
from movie.models import  Location, Movie, Theatre, Premium_Movie, Movie_cast, Events, User, Payment, Adds
from django.contrib.auth.models import User as Admin
from movie.forms import  LocationForm, MovieForm, TheatreForm, Premium_MovieForm, Movie_castForm, EventsForm, UserForm, PaymentForm, AddsForm
from django.contrib.auth.hashers import check_password
from django.urls import reverse

def validate_mobile_number(value):
    value = str(value)
    if not value.isdigit() or len(value) != 10:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/~`"
    if not any(char in special_characters for char in password):
        return False
    
    return True



def adminLogin(request):
    context = {}
    context["comment"] = ''
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            a1 = Admin.objects.get(email=email)
            if check_password(password,a1.password):
                return redirect('/adminList/')
            else:
                context["comment"] = "Incorrect password.."
                return render(request,'AdminLogin.html', context)
        except:
            context["comment"] = "Admin not found.."
            return render(request,'AdminLogin.html', context)
    return render(request,'AdminLogin.html')

def adminList(request):
    return render(request,'adminList.html')

def addLocation(request):
    context={
        'form':LocationForm()
    }
    context['error']=''
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            context['error']="Location Added Successfully"
            return render(request,'addLocation.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,'addLocation.html',context)

def addTheatre(request):
    context={
        'form':TheatreForm()
    }
    context['error']=''
    if request.method == 'POST':
        form = TheatreForm(request.POST)
        if form.is_valid():
            form.save()
            context['error']="Theatre Added Successfully"
            return render(request,'addTheatre.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,'addTheatre.html',context)

def addMovies(request):
    context = {}
    context['form']=MovieForm
    context['error']=''
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['error']="Movie Added Successfully"
            return render(request,'addMovies.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,"addMovies.html",context)

def addPremiere(request):
    context = {}
    context['form']=Premium_MovieForm
    context['error']=''
    if request.method == 'POST':
        form = Premium_MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['error']="Premiere Added Successfully"
            return render(request,'addPremiere.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,"addPremiere.html",context)

def addEvents(request):
    context = {}
    context['form']=EventsForm
    context['error']=''
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['error']="Event Added Successfully"
            return render(request,'addEvents.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,"addEvents.html",context) 

def addCast(request):
    context = {}
    context['form']=Movie_castForm
    context['error']=''
    if request.method == 'POST':
        form = Movie_castForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['error']="Cast Added Successfully"
            return render(request,'addCast.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,"addCast.html",context)

def addAdds(request):
    context = {}
    context['form']=AddsForm
    context['error']=''
    if request.method == 'POST':
        form = AddsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['error']="Poster Added Successfully"
            return render(request,'addAdds.html',context)
        else:
            context['error']="Something went wrong"
    return render(request,"addAdds.html",context)

def locationManage(request):
    context={}
    location = Location.objects.all()
    context["locations"]=location
    return render(request,"locationManage.html",context)

def deleteLocation(request,id):
    locations = Location.objects.get(id=id)
    locations.delete()
    return redirect('/locationManage/')

def editLocation(request,id):
    context={}
    location = Location.objects.get(id=id)
    context['form'] = LocationForm(request.POST or None, instance=location)
    context['error']=''
    context['location']=location
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = LocationForm(request.POST or None,instance=location)
        if form.is_valid():
            form.save()
            return redirect('/locationManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addLocation.html',context)

def theatreManage(request):
    context={}
    theatre = Theatre.objects.all()
    context["theatres"] = theatre
    return render(request,"theatreManage.html",context)

def deleteTheatre(request,id):
    theatre = Theatre.objects.get(id=id)
    theatre.delete()
    return redirect('/theatreManage/')

def editTheatre(request,id):
    context={}
    theatre = Theatre.objects.get(id=id)
    context['form'] = TheatreForm(request.POST or None, instance=theatre)
    context['error']=''
    context['theatre']=theatre
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = TheatreForm(request.POST or None,instance=theatre)
        if form.is_valid():
            form.save()
            return redirect('/theatreManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addTheatre.html',context)

def userManage(request):
    context={}
    user = User.objects.all()
    context["users"]=user
    return render(request,"userManage.html",context)

def movieManage(request):
    context={}
    movie = Movie.objects.all()
    context["movies"]=movie
    return render(request,"movieManage.html",context)

def deleteMovie(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/movieManage/')

def editMovie(request,id):
    context={}
    movie = Movie.objects.get(id=id)
    context['form'] = MovieForm(request.POST or None, instance=movie)
    context['error']=''
    context['movie']=movie
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = MovieForm(request.POST or None, request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movieManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addMovies.html',context)

def premiereManage(request):
    context={}
    premiere = Premium_Movie.objects.all()
    context["premieres"]=premiere
    return render(request,"premiereManage.html",context)

def deletePremiere(request,id):
    premiere = Premium_Movie.objects.get(id=id)
    premiere.delete()
    return redirect('/premiereManage/')

def editPremiere(request,id):
    context={}
    premiere = Premium_Movie.objects.get(id=id)
    context['form'] = Premium_MovieForm(request.POST or None, instance=premiere)
    context['error']=''
    context['premiere']=premiere
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = Premium_MovieForm(request.POST or None, request.FILES,instance=premiere)
        if form.is_valid():
            form.save()
            return redirect('/premiereManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addPremiere.html',context)

def eventManage(request):
    context={}
    event = Events.objects.all()
    context["events"]=event
    return render(request,"eventManage.html",context)

def deleteEvent(request,id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect('/eventManage/')

def editEvent(request,id):
    context={}
    event = Events.objects.get(id=id)
    context['form'] = EventsForm(request.POST or None,instance=event)
    context['error']=''
    context['event']=event 
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = EventsForm(request.POST or None, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/eventManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addEvents.html',context)

def castManage(request):
    context={}
    cast = Movie_cast.objects.all()
    context["casts"]=cast
    return render(request,"castManage.html",context)

def deleteCast(request,id):
    cast = Movie_cast.objects.get(id=id)
    cast.delete()
    return redirect('/castManage/')

def editCast(request,id):
    context={}
    cast = Movie_cast.objects.get(id=id)
    context['form'] = Movie_castForm(request.POST or None, instance=cast)
    context['error']=''
    context['cast']=cast 
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = Movie_castForm(request.POST or None, request.FILES,instance=cast)
        if form.is_valid():
            form.save()
            return redirect('/castManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addCast.html',context)

def addManage(request):
    context={}
    add = Adds.objects.all()
    context["posters"]=add
    return render(request,"posterManage.html",context)

def deleteAdd(request,id):
    add = Adds.objects.get(id=id)
    add.delete()
    return redirect('/posterManage/')

def editAdd(request,id):
    context={}
    poster = Adds.objects.get(id=id)
    context['form'] = AddsForm(request.POST or None, instance=poster)
    context['error']=''
    context['poster']=poster
    context['btval'] = 'Update'
    if request.method == 'POST':
        form = AddsForm(request.POST or None, request.FILES,instance=poster)
        if form.is_valid():
            form.save()
            return redirect('/posterManage/')
        else:
            context['error']="Something went wrong"
    return render(request,'addAdds.html',context)

# =====================================================USERRRRRR=====================================================================

def userHomePage(request,id):
    context = {}
    users = User.objects.get(id=id)
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    movies=Movie.objects.all()
    poster = Adds.objects.all()
    location = Location.objects.all()
    user = User.objects.all()
    context['locations']=location
    context['user']=user
    context['posters']=poster
    context["movies"]=movies
    context['events']=events
    context['users']=users
    context['premieres']=premieres
    return render(request,'userHome.html',context) 

def signUp(request):
    context={
        'form':UserForm()
    }
    context['error']=''
    if request.method == 'POST':
        if not  validate_mobile_number(request.POST.get("mobile")) and not validate_password(request.POST.get("password")):
            context['error'] = "Please enter a 10-digit mobile number and Password should contain 8 characters and at least one special character,one uppercase letter,one lowercase letter and one digit."
            return render(request,'signup.html',context)
        elif not validate_password(request.POST.get("password")):
            context['error'] = "Password should contain 8 characters and at least one special character,one uppercase letter,one lowercase letter and one digit."
            return render(request,'signup.html',context)
        elif not  validate_mobile_number(request.POST.get("mobile")):
            context['error'] = "Please enter a 10 digit mobile number"
            return render(request,'signup.html',context)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            context['error']="Something went wrong"
    return render(request,'signup.html',context)
    
def signIn(request):
    context = {}
    context["error"] = ''
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            a1 = User.objects.get(email=email)
            if (password==a1.password):
                return redirect('/userHome/{0}'.format(a1.id))
            else:
                context["error"] = "Incorrect password.."
                return render(request,'signin.html', context)
        except:
            context["error"] = "User not found.."
            return render(request,'signin.html', context)
    return render(request,'signin.html')

def movieInner(request,id):
    context = {}
    movie = Movie.objects.get(id=id)
    movies = Movie.objects.all()
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    cast = Movie_cast.objects.filter(movie_name=movie)
    context['movie']=movie
    context['casts']=cast
    context['events']=events
    context['moviess']=movies
    context['premieres']=premieres
    return render(request,"movieInner.html",context)

def premiereInner(request,id):
    context = {}
    premiere = Premium_Movie.objects.get(id=id)
    movies = Movie.objects.all()
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    context['premiere']=premiere
    context['events']=events
    context['moviess']=movies
    context['premieres']=premieres
    return render(request,"premiereInner.html",context)

def eventInner(request,id):
    context = {}
    event = Events.objects.get(id=id)
    movies = Movie.objects.all()
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    context['event']=event
    context['events']=events
    context['moviess']=movies
    context['premieres']=premieres
    return render(request,"eventInner.html",context)

def paymentManage(request):
    payments = Payment.objects.all()
    context={}
    context["payments"]= payments
    return render(request,"paymentManage.html",context)


from django.shortcuts import get_object_or_404

def addPayment(request, id):
    context = {}
    context['form'] = PaymentForm()
    movies = Movie.objects.get(id=id)
    theatre = Theatre.objects.filter(movie=movies)
    location = Location.objects.filter(movie=movies)
    context['movies'] = movies
    context['theatre'] = theatre
    context['locations'] = location

    movies = Movie.objects.all()
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    context['events'] = events
    context['moviess'] = movies
    context['premieres'] = premieres
    context['error'] = ''

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_instance = get_object_or_404(User, email=email)
            if user_instance.password == password:
                form = PaymentForm(request.POST)
                if form.is_valid():
                    payment_instance = form.save(commit=False)
                    payment_instance.user = user_instance
                    payment_instance.save()
                    context['error'] = "Payment Successful"
                    return render(request, "payment.html", context)
                else:
                    context['error'] = "Something went wrong"
            else:
                context['error'] = "Incorrect password"
        except User.DoesNotExist:
            context['error'] = "Email not registered. Please SignUp"

    return render(request, "payment.html", context)


def ticketDetails(request,id):
    context = {}
    user = User.objects.get(id=id)
    movies = Movie.objects.all()
    premieres = Premium_Movie.objects.all()
    events = Events.objects.all()
    payment = Payment.objects.filter(user_id=user)
    context['events']=events
    context['moviess']=movies
    context['premieres']=premieres
    context['payments']=payment
    context['user']=user
    return render(request,"ticket_details.html",context)


def deletePayment(request,id,user_id):
    payment = Payment.objects.get(user_id=user_id,id=id)
    payment.delete()
    return redirect('/userHome/{0}/ticket'.format(payment.user_id))

