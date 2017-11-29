from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ATvd3ya/0U95dSYL7HAc2Ve2AIwGbp/joohmHN1WxviHrngc9ByOGUlmahIB4mvs/++C4doDuXTGgiTkdW60e3POS+dDY8OhG6RO1lSly5EsG0xLFer9yWQTNEJ/0dCKju3l24hi/roNE63w+pyRrQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d76edb2c835d4e162d880f7b53db43d4')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = 'hi'
    t = event.message.text
    if t == '嘉義':
        reply = '雞肉飯...'
    elif t == '台北':
        reply = '天龍人...'
    elif t == '彰化':
        reply = '都流氓...'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()