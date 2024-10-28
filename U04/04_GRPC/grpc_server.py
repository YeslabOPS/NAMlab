import subprocess
import grpc
from concurrent import futures
import arphello_pb2
import arphello_pb2_grpc

class do_it(arphello_pb2_grpc.Get_arpServicer):
    def __init__(self):
        self.known_ip = "127.0.0.1"
        
    def Get_it2(self, request, context):
        print(request.query_content)
        #如果查询的是127.0.0.1的ARP信息，就可以做，否则就返回
        if request.query_content == self.known_ip:
            arp_data = self.get_arp_info()

            return arphello_pb2.arpReply(arp_info=arp_data)
        else:
            print("查不到该IP的ARP信息")
            return arphello_pb2.arpReply(arp_info="查不到该IP的ARP信息")
        
    def get_arp_info(self):
        result = subprocess.run(['arp', '-a'], 
                                capture_output=True, 
                                text=True, 
                                check=True)
        return result.stdout


def serve():
    #创建gRPC服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #从定义的服务中部署gRPC servicer
    arphello_pb2_grpc.add_Get_arp2Servicer_to_server(do_it(),server)
    #启动服务器
    server.add_insecure_port('0.0.0.0:10050')
    server.start()
    print("服务端已启动！")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()