from mysite.settings import DEBUG

def global_debug(request):
    return {'debug' : DEBUG}