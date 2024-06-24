# SPDX-License-Identifier: MIT
# Copyright (c) 2023, Caprica LLC
import json


options_sample = {
    "memo": "clippy is the ultimate hazard",
    "fee_ratio": 1024,
    "passphrase": None
}


class TransactionOptions:
    """
    This class represents the options object for a transaction
    """

    def __init__(self, json_str=None):
        self.__type = 'vnx.addons.OptionsSample'
        self.memo = ''
        self.fee_ratio = 0
        self.passphrase = None

        if json_str:
            self.__dict__ = json.loads(json_str)

    def to_json(self):
        return json.dumps(self.__dict__)


class MMXSession:
    """
    This class represents a session object for the MMX server
    """

    def __init__(self, json_str=None):
        self.__type = 'vnx.addons.HttpSession'
        self.hsid = ''
        self.login_time = 0
        self.permissions = ['mmx.permission_e.PUBLIC', 'vnx.addons.permission_e.FILE_DOWNLOAD',
                            'vnx.addons.permission_e.HTTP_REQUEST']
        self.session_timeout = 0
        self.user = ''
        self.vsid = 0

        if json_str:
            self.__dict__ = json.loads(json_str)

    def to_json(self):
        return json.dumps(self.__dict__)


class SwapInfo:
    """
    This class represents a swap object for the MMX server

    this is likely not the right object - see offer
    """

    def __init__(self, json_str=None):
        self.__type = ''
        self.address = ''
        self.avg_apy_1d = []
        self.avg_apy_7d = []
        self.balance = []
        self.decimals = []
        self.fee_rates = []
        self.fees_claimed = []
        self.fees_paid = []
        self.name = ''
        self.pools = []
        self.price = 0.0
        self.symbols = []
        self.tokens = []
        self.user_total = []
        self.volume = []
        self.volume_1d = []
        self.volume_7d = []
        self.wallet = []

        if json_str:
            self.__dict__ = json.loads(json_str)

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)


class OfferData:
    """
    This class represents an offer object for the MMX server

    this is likely what you want - not swap
    """

    def __init__(self, json_str=None):
        self.__type = ''
        self.address = ''
        self.ask_amount = 0
        self.ask_balance = 0
        self.ask_balance_value = 0.0
        self.ask_currency = ''
        self.ask_decimals = 0
        self.ask_symbol = ''
        self.ask_value = 0.0
        self.bid_balance = 0
        self.bid_balance_value = 0.0
        self.bid_currency = ''
        self.bid_decimals = 0
        self.bid_symbol = ''
        self.display_price = 0.0
        self.height = 0
        self.inv_price = ''
        self.owner = ''
        self.price = 0.0
        self.time = 0

        if json_str:
            self.__dict__ = json.loads(json_str)

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)
