import os
import requests
from sources.base import BaseSource

class Source(BaseSource):
    name = 'Multiproxy'

    def get_length(self):
        return 1

    def get_list(self, q=None):
        url = 'http://multiproxy.org/txt_all/proxy.txt'
        r = requests.get(url,timeout=10)

        for raw in r.text.split():
            ip = raw.split(':')[0]
            if ip not in self.ip_list:
                self.ip_list.append(ip)
                self.pbar.set_postfix(ipcount=str(len(self.ip_list)))

        self.pbar.update(1)

        if q:
            q.put(self.ip_list)
        return self.ip_list

if __name__ == '__main__':
    s = Source()
    s.get_list()
