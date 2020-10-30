import requests
import logging


class MonitorUtil(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(MonitorUtil, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance

    def set_url(self, __url__):
        self.url = __url__

    def set_token(self, __token__):
        self.token = __token__

    @staticmethod
    async def update_status(key_name, value):
        monitor = MonitorUtil()
        req = requests.post(
            url=monitor.url,
            data={
                'token': monitor.token,
                'key': key_name,
                'value': value
            }
        )
        logging.info(req.text)
