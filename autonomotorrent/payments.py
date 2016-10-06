import os
import json
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

CONFIG_DIR = "~/.autonomotorrent"
HOST_ADDRESS_FILE = "~/.autonomotorrent/host_address_mappings"

class PaymentWatcher(object):
    """docstring for PaymentWatcher"""

'''
    def __init__(self):
        super(PaymentWatcher, self).__init__()
        self.bitcoin_api = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("none", "none"))
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
        if os.path.exists(HOST_ADDRESS_FILE):
            f = open(HOST_ADDRESS_FILE)
            self.host_address_mappings = json.loads(f.read())
            f.close()
        else:
            self.host_address_mappings = {}
'''
    def get_address_for_host(host):
        return 'jippii'
        '''
        if host in self.host_address_mappings.keys():
            return self.host_address_mappings[host]
        # new host, generate address
        address = self.bitcoin_api.getnewaddress()
        self.host_address_mappings[host] = address
        # write the new address to the hosts file for every 10 ip addresses
        f = open(HOST_ADDRESS_FILE)
        f.write(json.dumps(self.host_address_mappings))
        f.close()
        return address
        '''

    def has_host_paid(host, amount=0.0001, confirmations=0)
        if host not in self.host_address_mappings.keys():
            return False
        recv_amount = bitcoin_api.getreceivedbyaddress(self.host_address_mappings[host], confirmations)
        if recv_amount >= amount:
            return True
        return False

    def host_paid_amount(host, confirmations=0)
        if host not in self.host_address_mappings.keys():
            return 0.0
        recv_amount = bitcoin_api.getreceivedbyaddress(self.host_address_mappings[host], confirmations)
        return recv_amount
