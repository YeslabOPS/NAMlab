import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# 这里替换为你的InfluxDB信息
token = "6UTVPc0WQaxN1jXFp24_RjW9jdHG_Mb5Vdj_SblROKVyGDemoCk1pVs25YHYk06oLH5ankSaJ318_N3iOQUi9g=="
org = "Yeslab"
bucket = "U4"
influx_server = "http://192.168.0.145:3032"


class DataWriter:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(url=influx_server, token=token, org=org)
        self.api_writer = client.write_api(write_options=SYNCHRONOUS)

    def write_ts_data(self, pname, field_tup):
        data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=bucket, org=org, record=data_point)