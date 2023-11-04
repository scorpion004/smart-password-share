import requests
import json

# By: scorpion004 (shuvasis.sarkar@gmail.com)
# github: https://github.com/scorpion004
# Using this module we can create link to share password to user without expose

#----setup----
# First signup to https://pwpush.com/
# Then generate API token

class PWPUSH:
    def __init__(self, email, token):
        self.email = email # Use same email id used in https://pwpush.com/
        self.token = token #Login/signup to https://pwpush.com/ and generate token

    def generate_passoword_url(self,password_value):
        #password_value is the string which you want to share with others
        #By default the link will be expired in 2 days and maximum 10 viewes supported
        try:
            url = "https://pwpush.com/p.json"
            payload = f'password%5Bpayload%5D={password_value}&password%5Bexpire_after_days%5D=2&password%5Bexpire_after_views%5D=10'
            headers = {
            'X-User-Email': self.email,
            'X-User-Token': self.token,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__cf_bm=XUXSGvNmdwDrS97tVUUKuKHE6_K3Gjpl9Xq0j2VNsSQ-1697009333-0-AXaSD5WehpGEksq2sj/OHlDXMHSzJFkdapL+ANj0oxcUcNchJaU+tQWkBwdbs2hhBFWcH2lUBZAJ8XyV8vtPTO8='
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            if response.status_code in [200,201]:

                # print(response.status_code)
                # print(type(response.text))
                # print((response.text))
                # print(json.loads(response.text)['url_token'])
                return "https://pwpush.com/en/p/" + json.loads(response.text)['url_token']
            else:
                print(response.status_code)
                print("Failed to generate URL")  
        except:
            print("Failed to generate URL")

    def delete_password_url(self,url):
        try:
            token = url.replace("https://pwpush.com/en/p/","")
            url = f"https://pwpush.com/p/{token}.json"
            payload = {}
            headers = {
            'X-User-Email': self.email,
            'X-User-Token': self.token,
            'Cookie': '__cf_bm=vOiPU_F2glmw0sIeFd0MNAntcmUmolOeL3tAtoqAhec-1697020917-0-Ac3QSeO/QrkWSqK5Q7mE9ow7W0UPlllspmxAXA5kySKKPUblqbizRI5f+smIcBv7EVEZ18JS1yHgAb2QX5INrI4='
            }

            response = requests.request("DELETE", url, headers=headers, data=payload)

            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    
    def monitor_url(self,url):
        #Using this function we can get audit log of the shared link
        #The return will be list of all views information
        #Output will be list of dictionary. Each dictionary we can get ip,browser,timestamp etc
        #if blank list, there are no viewes or clicks
        try:
            token = url.replace("https://pwpush.com/en/p/","")
            url = f"https://pwpush.com/p/{token}/audit.json"

            payload = {}
            headers = {
            'X-User-Email': self.email,
                'X-User-Token': self.token,
            'Cookie': '__cf_bm=.BPL2FA7ss92ktzkH0sVExqPd8Eh97brfohsKBuZ1bU-1697022469-0-AUzcnoE+0Xca0AfH3CpMfxxgy9C5LSHFoFcSljPdoiy1qyjSPeZ2k0GbiFf5wRwu533V5RAKSPfH6vSDSq3RClw='
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            print(response.text)

            if response.status_code == 200:
                return json.loads(response.text)['views']
            else:
                print(f"Failed to monitor URL (status code: {str(response.status_code)})")
        except:
            print("Failed to monitor URL")

