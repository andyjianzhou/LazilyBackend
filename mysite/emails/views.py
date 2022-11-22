from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from . import mail
@csrf_exempt
def index(request):
    # Get the data sent from the client
    #retrieve request body
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        email = data['params']['email']
        mail.send_email(email)  
        # return HttpResponse(email)
    return HttpResponse("OK")