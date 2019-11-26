from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from myapp.models import restaurant
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from module import func
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# Create your views here.


def listR(request):
        # 列出餐廳
    restaurants = restaurant.objects.all().order_by('id')  # 讀取資料表, 依 id 遞增排序
    return render(request, "listRestaurant.html", locals())


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:  # 依序處理所有事件
            if isinstance(event, MessageEvent):  # 檢查是否為訊息事件
                mtext = event.message.text
                user_id = event.source.user_id
                profile = line_bot_api.get_profile(user_id)
                print('name: ',profile.display_name)
                Pname = profile.display_name
                print('id: ',profile.user_id)
                if mtext == '賈崩':
                    func.sendResPosition(event)  # event裡面有回郵的郵票
                else :
                    func.sendMessage(event,Pname)
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
