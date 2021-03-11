class Cloudflare:
    def __init__(self):
        self.base_url = 'https://api.cloudflare.com/client/v4/'
        self.endpoint = None

    def zones(self):
        self.endpoint = self.base_url + 'zones'

    def dns_records(self, zone_id):
        self.endpoint = self.base_url + 'zones/' + zone_id + 'dns_records'
