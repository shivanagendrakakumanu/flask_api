import requests

def test_post_headers_body_json():
    url = 'http://127.0.0.1:5000/getname'
    
    resp = requests.get(url)       
    assert resp.status_code == 200
    
    # print response full body as text
    print(resp.text)
