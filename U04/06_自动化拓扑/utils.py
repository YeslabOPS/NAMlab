import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB Init
token = "s6SUDcsQx1uct15vdQ1-XsBlwYdfZFviYAkB1BBKkdZ7nSabGQJFkUtHRvEmDsvq3LfM5Nuh_LFmbvs9ec0KwA=="
org = "yeslab"
bucket = "first_demo"
influx_server = "http://183.6.42.206:3033"

class DataWriter:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(url=influx_server, token=token, org=org)
        self.api_writer = client.write_api(write_options=SYNCHRONOUS)

    def write_ts_data(self, pname, field_tup):
        data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=bucket, org=org, record=data_point)