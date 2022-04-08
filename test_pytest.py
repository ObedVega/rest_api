import requests

def test_endpoint2():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200    

        
