from django.http import HttpResponseForbidden 

class RejectSpambotRequestsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        self.blacklist = ['bot1.com', 'bot2.com']

    def __call__(self, request):  
        referer = request.META.get('HTTP_REFERER')
        response = self.get_response(request)

        if not referer:
            return response

        for bad in self.blacklist:
            if bad in referer:
                return HttpResponseForbidden()
        return response