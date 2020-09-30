from pytest_check import check


class Asssert:
    # Asssert().equal(fail_data['espect'],r.json(),"msg,status,code")
    def equal(self,expect,response,key_str):
        try:
            keys=key_str.split(",")    #Asssert().equal(fail_data['espect'], r.json(), "msg,status,code")
            for key in keys:
                r=str(response[key])
                e=str(expect[key])
                check.equal(r,e)
                print(f"响应信息为：{response}。预期结果为{expect}.校验字段为{key}.实际结果为：{r}。预期结果为：{e}。校验成功")
        except Exception as e:
                print(f"响应信息为：{response}。预期结果为{expect}.校验字段为{key}.实际结果为：{r}。预期结果为：{e}。校验失败")

