from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from module import func
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


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

        for event in events:#依序處理所有事件
            if isinstance(event, MessageEvent):#檢查是否為訊息事件
            	mtext = event.message.text
            	user_id = event.source.user_id
            	profile = line_bot_api.get_profile(user_id)
            	print(profile.display_name)
            	print(profile.user_id)
            	print(profile.picture_url)
            	if mtext == '抽':
            		func.sendImage(event)#event裡面有回郵的郵票
            	elif mtext=='文字':
            		func.sendText(event)
            	elif mtext == '貼圖':
            		func.sendStick(event)
            	elif mtext == '多傳':
            		func.sendMulti(event)
            	elif mtext == '位置':
            		func.sendPosition(event)
            	elif mtext == '選單':
            		func.sendQuickreply(event)
            	else:
            		func.replyText(event)
            		
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
