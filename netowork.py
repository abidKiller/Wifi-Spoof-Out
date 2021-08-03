from urllib3 import urlopen
from urllib3 import Request
def resolveMac(mac):
    try:
        # send request to macvendors.co
        url = "http://macvendors.co/api/vendorname/"
        request = Request(url + mac, headers={'User-Agent': "API Browser"})
        response = urlopen(request)
        vendor = response.read()
        vendor = vendor.decode("utf-8")
        vendor = vendor[:25]
        return vendor
    except KeyboardInterrupt:
        exit()
    except:
        return "N/A"