
REGISTER="futureloan/mvc/api/member/register"

class Member:
    def register(self,url,base_requests,data):

        real_url=url+REGISTER
        r=base_requests.post(real_url,data=data)
        return  r


    def login(self):
        pass

if __name__ == '__main__':
    from jinrongzonghe.caw.BaseRequests import BaseRequests
    r = Member().register("http://192.168.150.222:8081/",BaseRequests(),{"mobilephone":"12345","pwd":"123456"})
    print("手机号码格式不正确" in r.text)