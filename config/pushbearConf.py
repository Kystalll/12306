# coding: utf-8
from urllib.parse import quote
from urllib.request import urlopen
from config.ticketConf import _get_yaml
# from config.urlConf import urls
# from myUrllib.httpUtils import HTTPClient


# PUSH_BEAR_API_PATH = "https://pushbear.ftqq.com/sub"
PUSH_BEAR_API_PATH = "https://sc.ftqq.com/"


def sendPushBear(msg):
    """
    pushBear微信通知
    :param str: 通知内容 content
    :return:
    """
    conf = _get_yaml()
    if conf["pushbear_conf"]["is_pushbear"] and conf["pushbear_conf"]["send_key"].strip() != "":
        try:
            # sendPushBearUrls = urls.get("Pushbear")
            # data = {
            #     "sendkey": conf["pushbear_conf"]["send_key"].strip(),
            #     "text": "易行购票成功通知",
            #     "desp": msg
            # }
            # httpClint = HTTPClient(0)
            # sendPushBeaRsp = httpClint.send(sendPushBearUrls, data=data)
            msg = quote(msg)
            sendPushBeaRsp = urlopen('https://sc.ftqq.com/SCU47890T5f77adbc260def408ab5954210b0597d5ca55b3d535f1.send?text=' % msg)
            if sendPushBeaRsp:
                print(u"已下发微信通知, 请查收")
            else:
                print(sendPushBeaRsp)
        except Exception as e:
            print(u"sever酱配置有误 {}".format(e))
    else:
        pass


if __name__ == '__main__':
    sendPushBear(1)
