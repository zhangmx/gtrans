import requests


def test_translate():
    url = 'http://127.0.0.1:4000/'
    form_data = {
        'text': 'Hello World!',
        'from': 'auto',
        'to': 'ar'
    }

    try:
        response = requests.post(url, data=form_data)
        response.raise_for_status()  # 检查是否有HTTP错误
        result = response.json()

        # 检查响应的结构和内容
        if result.get('ok') and result.get('text') == form_data['text'] and result.get('to') == form_data['to']:
            print("Test passed!")
            print("Translation:", result.get('response'))
        else:
            print("Test failed!")
            print("Response:", result)

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)


if __name__ == '__main__':
    test_translate()
