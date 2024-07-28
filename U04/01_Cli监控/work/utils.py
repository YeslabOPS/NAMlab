import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# 这里替换为你的InfluxDB信息
token = "A4Urh_wTR87jhMeYmXmfsfpU4VlmW4HV6c_lPQfEoHMnLOmSR3n6BKFzSF0UjZptkJCCxpYoez_lYmrz5_YwBg=="
org = "yeslab"
bucket = "class"
influx_server = "http://127.0.0.1:8086"

class DataWriter:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(url=influx_server, token=token, org=org)
        self.api_writer = client.write_api(write_options=SYNCHRONOUS)

    def write_ts_data(self, pname, field_tup):
        data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=bucket, org=org, record=data_point)