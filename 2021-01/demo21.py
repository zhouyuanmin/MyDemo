from alipay import AliPay

# ======= settings =======
ALIPAY_APP_ID = 2021000117602712
ALIPAY_DEBUG = True
app_private_key_string = open("/Users/zhou/Desktop/app_private_key.pem").read()  # 需要写入沙盒应用
alipay_public_key_string = open("/Users/zhou/Desktop/app_public_key2.pem").read()  # 是支付宝的公钥，在沙盒应用里面

alipay = AliPay(
    appid=ALIPAY_APP_ID,
    app_notify_url=None,  # 默认回调url
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=ALIPAY_DEBUG,  # 默认False
)

order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no=320003230203299,
    total_amount=str(200),
    subject=f"测试订单{1234567890}",
    return_url="http://www.meiduo.site:8080/pay_success.html",  # 需要是真实的
)

# 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
print("https://openapi.alipaydev.com/gateway.do?" + order_string)
"""
商家信息
商家账号jyjxcb6495@sandbox.com
商户UID2088621955210430
登录密码111111
账户余额
0.00充值取现

买家信息
买家账号yvccux8381@sandbox.com
登录密码111111
支付密码111111
用户名称yvccux8381
证件类型身份证(IDENTITY_CARD)
证件号码924875198705059493
账户余额
99999.00充值取现
"""

"""
沙盒环境: https://openhome.alipay.com/platform/appDaily.htm?tab=info
Git上的SDK包和例子: https://github.com/fzlee/alipay/blob/master/README.zh-hans.md#alipay.trade.page.pay
"""
