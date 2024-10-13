from concurrent import futures
import time
import grpc
import protoxemdt_grpc_dialout_pb2_grpc
import telemetry_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    # 创建一个grpc server对象
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册huawei的telemetry数据监听服务
    protoxemdt_grpc_dialout_pb2_grpc.add_gRPCMdtDialoutServicer_to_server(
        Telemetry_CPU_Info(), server)
    # 设置socket监听端口
    server.add_insecure_port('0.0.0.0:20000')
    # 启动grpc server
    server.start()
    # 死循环监听
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


class Telemetry_CPU_Info(protoxemdt_grpc_dialout_pb2_grpc.gRPCMdtDialoutServicer):
    def __init__(self):
        return

    def MdtDialout(self, request_iterator, context):
        data = request_iterator.next().data
        telemetry_data = telemetry_pb2.Telemetry.FromString(data)
        cpu_5s = telemetry_data.data_gpbkv[0].fields[1].fields[0].uint32_value
        cpu_1m = telemetry_data.data_gpbkv[0].fields[1].fields[1].uint32_value
        cpu_5m = telemetry_data.data_gpbkv[0].fields[1].fields[2].uint32_value
        print(f"CPU_5S:{cpu_5s}\nCPU_1M:{cpu_1m}\nCPU_5M:{cpu_5m}\n")

if __name__ == '__main__':
    serve()