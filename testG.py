from googletrans import Translator
# import os
#
# # 设置代理
# os.environ['http_proxy'] = 'http://127.0.0.1:7890'
# os.environ['https_proxy'] = 'http://127.0.0.1:7890'

translator = Translator()

def translate(text, source_lang='auto', target_lang='en'):
    try:
        result = translator.translate(text, src=source_lang, dest=target_lang)
        response = {
            'ok': True,
            'text': text,
            'from': result.src,
            'to': result.dest,
            'response': result.text
        }
    except Exception as e:
        return {'ok': False, 'error': str(e)}

    return response

if __name__ == '__main__':
    text = 'Hello World!'
    result = translate(text, source_lang='auto', target_lang='ar')
    if result.get('ok') and result.get('text') == text and result.get('to') == 'ar':
        print("Test passed!")
        print("Translation:", result.get('response'))
    else:
        print("Test failed!")
        print("Response:", result)