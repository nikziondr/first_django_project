from django.http import HttpResponse

# Create your views here.
person = {'name': 'Nikson Restituyo', 'track': 'Backend (Python)', 'message': "thank you very much for the time dedicated to putting this material together."}
def index(request):
    
    return HttpResponse(f'Hello, this is student {person["name"]}, currently on track {person["track"]} and I just want to say {person["message"]}')