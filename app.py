from flask import Flask, request, jsonify
from googletrans import Translator

# import os
#
# # 设置代理
# os.environ['http_proxy'] = 'http://127.0.0.1:7890'
# os.environ['https_proxy'] = 'http://127.0.0.1:7890'


app = Flask(__name__)
translator = Translator()


@app.route('/', methods=['POST'])
def translate():
    # 从表单中获取数据
    text = request.form.get('text')
    source_lang = request.form.get('from', 'auto')
    target_lang = request.form.get('to', 'en')

    # 检查是否提供了必要的字段
    if not text or not target_lang:
        return jsonify({'ok': False, 'error': 'Missing required fields'}), 400

    # 进行翻译
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
        return jsonify({'ok': False, 'error': str(e)}), 500

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=4000)
