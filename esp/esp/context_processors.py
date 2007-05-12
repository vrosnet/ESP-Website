import esp.web.util.globaltags

def media_url(request): 

    from django.conf import settings 
    return {'media_url': settings.MEDIA_URL} 

def esp_user(request):
    from esp.users.models import ESPUser
    user = ESPUser(request.user)

    return {'user': user}