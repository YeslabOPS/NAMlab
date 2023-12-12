import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB Init
token = "8HaA9WcurzA4GoI7z-UzIX7asmHWl_X2m58gFlNrC5ug87tqn3__0RQ-AQBsbZz755PL04U9BmnijzTPoVTfFA=="
org = "yeslab"
bucket = "devices"
influx_server = "http://127.0.0.1:8086"

class DataWriter:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(url=influx_server, token=token, org=org)
        self.api_writer = client.write_api(write_options=SYNCHRONOUS)

    def write_ts_data(self, pname, field_tup):
        data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=bucket, org=org, record=data_point)