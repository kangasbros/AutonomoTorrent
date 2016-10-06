import os
import json
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

home_path = os.path.expanduser('~')

CONFIG_DIR = home_path + "/.autonomotorrent"
HOST_ADDRESS_FILE = home_path + "/.autonomotorrent/host_address_mappings.json"
BITCOIN_CONFIG_FILE = home_path + "/.autonomotorrent/bitcoin.conf"

class PaymentWatcher(object):
    """docstring for PaymentWatcher"""

    def __init__(self):
        super(PaymentWatcher, self).__init__()

        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
        if os.path.exists(BITCOIN_CONFIG_FILE):
            f = open(BITCOIN_CONFIG_FILE)
            self.config = json.loads(f.read())
            f.close()
            self.enabled = True
            self.bitcoin_api = AuthServiceProxy(self.config["connection_string"])
        else:
            self.enabled = False
        if os.path.exists(HOST_ADDRESS_FILE):
            f = open(HOST_ADDRESS_FILE)
            self.host_address_mappings = json.loads(f.read())
            f.close()
        else:
            self.host_address_mappings = {}

    def get_address_for_host(self, host):
        if not self.enabled:
            return None
        if host in self.host_address_mappings.keys():
            return self.host_address_mappings[host]
        # new host, generate address
        address = self.bitcoin_api.getnewaddress()
        self.host_address_mappings[host] = address
        # write the new address to the hosts file for every 10 ip addresses
        f = open(HOST_ADDRESS_FILE, 'w')
        f.write(json.dumps(self.host_address_mappings))
        f.close()
        return address

    def has_host_paid(self, host, amount=0.0001, confirmations=0):
        if not self.enabled:
            return False
        if host not in self.host_address_mappings.keys():
            return False
        recv_amount = self.bitcoin_api.getreceivedbyaddress(self.host_address_mappings[host], confirmations)
        if recv_amount >= amount:
            return True
        return False

    def host_paid_amount(self, host, confirmations=0):
        if not self.enabled or host not in self.host_address_mappings.keys():
            return 0.0
        recv_amount = bitcoin_api.getreceivedbyaddress(self.host_address_mappings[host], confirmations)
        return recv_amount

