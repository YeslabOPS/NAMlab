from concurrent import futures
import time
import importlib
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
    server.add_insecure_port('192.168.1.3:20000')
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
        in_octets = telemetry_data.data_gpbkv[0].fields[-1].fields[1].uint64_value
        out_octets = telemetry_data.data_gpbkv[0].fields[-1].fields[-1].uint64_value
        print(in_octets)
        print(out_octets)

if __name__ == '__main__':
    serve()