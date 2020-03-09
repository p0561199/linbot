from django.shortcuts import render
import logging
import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
logger = logging.getLogger("django")
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.CHANNEL_SECRET)

schedule = {}

@csrf_exempt
@require_POST
def webhook(request):
    signature = request.headers["X-Line-Signature"]
    body = request.body.decode()
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = (
            "Invalid signature. Please check your channel access token/channel secret."
        )
        logger.error(messages)
        return HttpResponseBadRequest(messages)
    return HttpResponse("OK")


# @handler.add(PostbackEvent)
# def handl_postback(event):
    # if event.postback.data == 'A':
    #     message = TextSendMessage(text='你選擇第一個按鈕')
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif event.postback.data == 'B':
    #     message = TextSendMessage(text='你選擇第二個按鈕')
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif event.postback.data == 'C':
    #     message = TextSendMessage(text='你選擇第三個按鈕')
    #     line_bot_api.reply_message(event.reply_token, message)


	# import json
	# from datetime import datetime
	# if event.postback.data == '1':
	# 	message = TextSendMessage(text="每張選單可以選擇一天日期，顯示編號後。請利用#編號換行輸入填寫內容\nex:\n#aabbc\n我要吃大餐")
	# 	line_bot_api.reply_message(event.reply_token, message)
	# elif event.postback.data == '2':
	# 	message = TextSendMessage(text="如果要刪除記事本資料，請利用$編號直接進行刪除\nex:\n$aabbc")
	# 	line_bot_api.reply_message(event.reply_token, message)
	# elif event.postback.data == '3':
	# 	schedule.clear()
	# 	message = TextSendMessage(text="已刪除所有記事本")
	# 	line_bot_api.reply_message(event.reply_token, message)

	# else:
	# 	data = event.postback.data
	# 	data = json.loads(data)
	# 	day = event.postback.params['datetime']
	# 	day = datetime.strptime(day, "%Y-%m-%dT%H:%M")

	# 	schedule[data["uuid"]] = {"date":str(day),"content": ''}
	# 	li = ''
	# 	for each in schedule:
	# 		tmp =  '編號:'+ each +'\n日期:'+schedule[each]['date']+'\n內容:'+schedule[each]['content']+'\n==========\n'
	# 		li+=tmp
	# 	line_bot_api.reply_message(event.reply_token, TextSendMessage(text=li))
    

@handler.add(event=MessageEvent)
def handl_message(event):
    #文字訊息
    
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

    #圖片訊息

#     if event.message.text == 'Ray':
#         message = ImageSendMessage(
#     original_content_url='https://scontent.frmq2-2.fna.fbcdn.net/v/t1.0-9/10421623_10204486414914414_4652257635742929259_n.jpg?_nc_cat=107&_nc_ohc=B3t3k0DAt3wAX_zYbkW&_nc_ht=scontent.frmq2-2.fna&oh=8be3a1940b1567063526e3ebf398538b&oe=5EB6202F',
#     preview_image_url='https://scontent.frmq2-2.fna.fbcdn.net/v/t1.0-9/10421623_10204486414914414_4652257635742929259_n.jpg?_nc_cat=107&_nc_ohc=B3t3k0DAt3wAX_zYbkW&_nc_ht=scontent.frmq2-2.fna&oh=8be3a1940b1567063526e3ebf398538b&oe=5EB6202F'
# )
#     elif '米羅' in event.message.text :
#         message = ImageSendMessage(
#     original_content_url='https://scontent.frmq2-1.fna.fbcdn.net/v/t1.0-1/12507263_1093242514027288_513884793190580569_n.jpg?_nc_cat=111&_nc_ohc=4vIOTtl4eiQAX-p8WQ4&_nc_ht=scontent.frmq2-1.fna&oh=14772f0ad95d5144c3cc390bfaf891bd&oe=5EC645A5',
#     preview_image_url='https://scontent.frmq2-1.fna.fbcdn.net/v/t1.0-1/12507263_1093242514027288_513884793190580569_n.jpg?_nc_cat=111&_nc_ohc=4vIOTtl4eiQAX-p8WQ4&_nc_ht=scontent.frmq2-1.fna&oh=14772f0ad95d5144c3cc390bfaf891bd&oe=5EC645A5'
# )
	
    #貼圖訊息

    # if event.message.text == '貼圖':
    #     message = StickerSendMessage(
    #     package_id='1',
    #     sticker_id='1')

    #日圓匯率查詢
    # if '日圓' in event.message.text:
    #     url = 'https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/'
    #     message = TextSendMessage(text=JPY_rate(url))
    #     line_bot_api.reply_message(event.reply_token, message)

    #天氣查詢

    # if '天氣' in event.message.text:
    #     message = TextSendMessage(text=Weather_get())
    #     line_bot_api.reply_message(event.reply_token, message)


    #抽狗狗的圖

    # if '狗' in event.message.text:
    #     res = requests.get('https://random.dog/woof.json')
    #     res = res.json()
    #     url = res['url']

    #     message = ImageSendMessage(original_content_url=url,preview_image_url=url)
    #     line_bot_api.reply_message(event.reply_token, message)

    #偵測網址

    # if 'http' in event.message.text:
    #     s = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
    #     import re
    #     url = event.message.text
    #     print(url)
    #     murl = re.match(s, url).string
    #     print(murl)
    #     res = malicious_website(murl)
    #     message = TextSendMessage(text=murl+'\n'+res)
    #     line_bot_api.reply_message(event.reply_token, message) 




#     import uuid
#     #個人選單
#     if '#' in event.message.text:
#         res = event.message.text.split('\n')
#         if len(res) <= 1:
#             line_bot_api.reply_message(event.reply_token, TextSendMessage(text="格式錯誤\n1111"))
#         else:
#             try:
#                 UID = res[0].split('#')[1]
#                 schedule[UID]['content'] = res[1]
#                 li = ''
#                 for each in schedule:
#                     tmp =  '編號:'+ each +'\n日期:'+schedule[each]['date']+'\n內容:'+schedule[each]['content']+'\n==========\n'
#                     li+=tmp
#                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text=li))
#             except:
#             	line_bot_api.reply_message(event.reply_token, TextSendMessage(text="編號錯誤"))
#     elif '$' in event.message.text:
#         res = event.message.text.split('\n')
#         if len(res) > 1:
#             line_bot_api.reply_message(event.reply_token, TextSendMessage(text="格式錯誤\n1111"))
#         else:
#             try:
#                 UID = res[0].split('$')[1]
#                 print(UID)
#                 schedule.pop(UID)
#                 if schedule=={}:
#                 	line_bot_api.reply_message(event.reply_token, TextSendMessage(text="目前行事曆是空的"))
#                 else:
#                     li = ''
#                     for each in schedule:
#                         tmp =  '編號:'+ each +'\n日期:'+schedule[each]['date']+'\n內容:'+schedule[each]['content']+'\n==========\n'
#                         li+=tmp
#                     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=li))
#             except:
#             	line_bot_api.reply_message(event.reply_token, TextSendMessage(text="編號錯誤"))

#     elif '行事曆' in event.message.text:
#         if schedule=={}:
#                 	line_bot_api.reply_message(event.reply_token, TextSendMessage(text="目前行事曆是空的"))
#         else:
#             li = ''
#             for each in schedule:
#                 tmp =  '編號:'+ each +'\n日期:'+schedule[each]['date']+'\n內容:'+schedule[each]['content']+'\n==========\n'
#                 li+=tmp
#             line_bot_api.reply_message(event.reply_token, TextSendMessage(text=li))



#     #嘗試做一個選單測試
#     if '測試選單' in event.message.text:
#         message = TemplateSendMessage(
#     alt_text='Buttons template',
#     template=ButtonsTemplate(
#         thumbnail_image_url='https://example.com/image.jpg',
#         title='選單',
#         text='請選擇',
#         actions=[
#                   PostbackTemplateAction(
#                                         label='選項一', 
#                                         text='選項一',
#                                         data='A'
#                                     ),
#                   PostbackTemplateAction(
#                                         label='選項二', 
#                                         text='選項二',
#                                         data='B'
#                                     ),
#                   PostbackTemplateAction(
#                                         label='選項二', 
#                                         text='選項二',
#                                         data='C'
#                                     ),
#         ]
#     )
# )



#     #客製化記事本
#     if event.message.text == '選單':
#         message = TemplateSendMessage(
#         alt_text='Buttons template',
#         template=ButtonsTemplate(
#             thumbnail_image_url='https://lh3.googleusercontent.com/proxy/8WqRg3AVyvWmG46ynZpcgECKn9VZPSe2ouLP1v-V33U4FSUEMf31jHhpcxBS09o_4uicZr2k319o8qZWi-RQXn-Ok2rYo8tO6AmSW-shXYPj',
#             title='管家選單',
#             text='請選擇',
#             actions=[
#                     DatetimePickerAction(label="選擇日期",
#                                     data="{\"uuid\":\""+ str(uuid.uuid4())[1:6]+"\"}",
#                                     mode="datetime",
#                                     ),
#                 	PostbackTemplateAction(
#                                         label='記事本填寫教學', 
#                                         text='記事本填寫教學',
#                                         data='1'
#                                     ),
#                 	PostbackTemplateAction(
#                                         label='刪除所有記事本', 
#                                         text='刪除所有記事本',
#                                         data='3'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='顯示所有行事曆', text='行事曆'
#                                     )

#                 ]
#             )
#         )

#         line_bot_api.reply_message(event.reply_token, message)
    
# def JPY_rate(url):

# 	response = requests.get(url)
# 	html_src = response.text

# 	soup = BeautifulSoup(html_src, "lxml")
	
# 	s = soup.find_all("td")
# 	for each in s:
# 		if '日圓(JPY) Japanese Yen' in str(each):
# 			x = each.findPrevious()
# 			soup2 = BeautifulSoup(str(x), "lxml")
# 			val = soup2.find_all("td")[2].text
# 	return "目前國泰世華的日圓匯率為" + val + "，該買了啦!"

# def Weather_get():

# 	res = requests.get('http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-8BE88B49-A8BB-4B43-B4A6-AAAEF4549A78&format=JSON&locationName=%E8%87%BA%E4%B8%AD%E5%B8%82')
# 	res = res.json()
# 	# print(res['records']['location'][0]['weatherElement'][2])

# 	for each in res['records']['location'][0]['weatherElement']:
# 		print(each)

# 	# 溫度最低溫
# 	MinT = ''
# 	for each in res['records']['location'][0]['weatherElement'][2]['time']:
# 		MinT += each['startTime'] + '~' + each['endTime']  + '最低溫為:' + each['parameter']['parameterName']+'度C'+'\n'
# 	print(MinT)
# 	MaxT = ''
# 	# 溫度最高溫
# 	for each in res['records']['location'][0]['weatherElement'][4]['time']:
# 		MaxT += each['startTime'] + '~' + each['endTime']  + '最高溫為:' + each['parameter']['parameterName']+'度C'+'\n'
# 	print(MaxT)

# 	#天氣
# 	wea = ''
# 	wea = res['records']['location'][0]['locationName'] +'，目前天氣為' + res['records']['location'][0]['weatherElement'][0]['time'][len(res['records']['location'][0]['weatherElement'][0]['time'])-2]['parameter']['parameterName'] + '\n'
	
# 	return MinT+'\n'+MaxT+'\n'+wea

# def malicious_website(url):

# 	from pysafebrowsing import SafeBrowsing
# 	s = SafeBrowsing('AIzaSyDt47tTRxgM9tV-btrHYXXFEOq14F-qg6I')
# 	r = s.lookup_urls([url])
	
# 	text = r[url]['malicious']
# 	if text == True:
# 		res = '發現疑似惡意病毒網站，恐為' + r[url]['threats'][0]
# 	else:
# 		res = '暫無發現任何不安全跡象，但不保證，謝謝。'
# 	return res