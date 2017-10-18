from django.http import HttpResponse
import base64

def pixel_gif(request):
    PIXEL_GIF_DATA = """
    R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
    """.strip()
    PIXEL_GIF_DATA = base64.b64decode(PIXEL_GIF_DATA)
    info=request.GET
    res=HttpResponse(PIXEL_GIF_DATA, content_type='image/gif')
    # print("url",info['url'])
    # print("title", info['t'])
    # print("ref", info['ref'])

    return res
def generatejs(request):
    js_str="""
    (function() {
        var img = new Image,
          url = encodeURIComponent(document.location.href),
          title = encodeURIComponent(document.title),
          ref = encodeURIComponent(document.referrer);
          img.src = 'https://phuonganalytic.herokuapp.com/a.gif?url=' + url + '&t=' + title + '&ref=' + ref;
        })();
    """
    return HttpResponse(js_str)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        ip = request.META.get('REMOTE_ADDR')
    return ip


