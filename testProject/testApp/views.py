from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from testApp.models import ai_analysis_log
# Create your views here.

from django.http import HttpResponse

# index
def index(request):
    contextUI = f'''
                <form action="/imageanalysis/" method="post">
                    <input type="text" style="width:500px;" name="path" placeholder="input path" value="/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg">
                    <input type="submit" value="request">
                </form>
                <br/>
    '''
    for topic in ai_analysis_log.objects.all():
        contextUI += f'''<br/> {topic} '''

    return HttpResponse(contextUI)


@csrf_exempt
def imageApi(request):
    #get and save image path
    path = request.POST['path']

    # AIで分析
    result = json.loads(imageAnalysysApi(path))
    
    # AIで分析成功
    if result['success']:
        a = ai_analysis_log(image_path = path
                , success = result['success']
                , message = result['message']
                , class_id = result['estimated_data']['class']
                , confidence= result['estimated_data']['confidence']
                , request_timestamp = timezone.now()
                , response_timestamp = timezone.now())
        a.save()
        contextUI = f'''
                <form action="/" method="get">
                    <p>register success!</p>
                    <input type="submit" value="back">
                </form>
                <br/>
                '''
    # AIで分析失敗
    else:
        contextUI = f'''
                <form action="/" method="get">
                    <p>register fail .. </p>
                    <input type="submit" value="back">
                </form>
                <br/>
                '''

    return HttpResponse(contextUI)

def imageAnalysysApi(path):
    aiResult = AiAnalysys(path)
    return json.dumps({"success": True
                       , "message": "success"
                       , "estimated_data": {
                           "class": aiResult[0],
                            "confidence": aiResult[1]
                       }})

def AiAnalysys(path):
    return 3, 0.8683
