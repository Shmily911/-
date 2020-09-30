

import requests
class BaseRequests:
    def __init__(self):
        self.session=requests.Session()

    # def get(self,url,data=None,json=None,**kwargs):
    #     try:
    #         r1=self.session.get(url,data=data,json,**kwargs)
    #         return r1
    #     except Exception as c:
    #         print(f"发送get请求:{url},{data},{json},{kwargs},异常{c})



    def post(self,url,data=None,json=None,**kwargs):

        try:
            r = self.session.post(url,data=data,json=json,**kwargs)
            return r
        except Exception as e:
            print(f"发送post请求：{url},{data},{json},{kwargs},异常{e}")


if __name__ == '__main__':
    r=BaseRequests().post("http://www.httpbin.org/post",data={"user":"root"})
    print(r.text)
