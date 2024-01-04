from concurrent import futures
import time
import importlib
import grpc
import huawei_grpc_dialout_pb2_grpc
import huawei_telemetry_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    # 创建一个grpc server对象
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册huawei的telemetry数据监听服务
    huawei_grpc_dialout_pb2_grpc.add_gRPCDataserviceServicer_to_server(
        Telemetry_CPU_Info(), server)
    # 设置socket监听端口
    server.add_insecure_port('192.168.1.2:20000')
    # 启动grpc server
    server.start()
    # 死循环监听
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


# 创建类继承huawei_grpc_dialout_pb2_grpc中Servicer方法
class Telemetry_CPU_Info(huawei_grpc_dialout_pb2_grpc.gRPCDataserviceServicer):
    def __init__(self):
        return

    def dataPublish(self, request_iterator, context):
        for i in request_iterator:
            print('############ start ############\n')
            telemetry_data = huawei_telemetry_pb2.Telemetry.FromString(i.data)
            temp_cpu = []
            for row_data in telemetry_data.data_gpb.row:
                module_name = telemetry_data.proto_path.split('.')[0]
                root_class = telemetry_data.proto_path.split('.')[1]

                decode_module = importlib.import_module(module_name + '_pb2')

                decode_func = getattr(decode_module, root_class).FromString
                data = decode_func(row_data.content)
                temp_cpu.append(data)
            monitoring(temp_cpu)

def monitoring(temp_cpu):
    cpu_usage_list = [cpu['cpuInfos']['cpuInfo']['systemCpuUsage'] for cpu in temp_cpu]
    print(cpu_usage_list)


if __name__ == '__main__':
    serve()