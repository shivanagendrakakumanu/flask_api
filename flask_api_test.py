
import requests
import flask_api 

def test_get_name():
    web = flask_api.app.test_client()
    resp = web.get('/getname')
    # url = 'http://127.0.0.1:5000/getname'
    # resp = requests.get(url)
    assert resp.status_code == 200
    
    # print response full body as text
    print(resp.text)
