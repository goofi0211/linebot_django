from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from myapp.models import restaurant
import random
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendResPosition(event):  #傳送餐廳位置
    #try:
        restaurants = restaurant.objects.all()
        index=random.randint(0,len(restaurants)-1)
        message = LocationSendMessage(
            title=restaurants[index].cTitle,
            address=restaurants[index].cAddr,
            latitude=float(restaurants[index].cLatitude),  #緯度
            longitude= float(restaurants[index].cLongitude)
        )
        line_bot_api.reply_message(event.reply_token, message)
def sendMessage(event,name):
    print('name: ',name)
    if name=='潘文傑':
        print('good')
        message = TextSendMessage(text='太帥了把文傑')
    elif name=='Wilson Su':
        message = TextSendMessage(text='說說哥來了')
    line_bot_api.reply_message(event.reply_token, message)
