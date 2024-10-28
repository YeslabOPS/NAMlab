import grpc
import arphello_pb2
import arphello_pb2_grpc

def run():
    #客户端实例化stub
    connect = grpc.insecure_channel('localhost:10050')
    stub = arphello_pb2_grpc.Get_arpStub(channel=connect)
    #通过stub调用服务端的Login_info方法
    response = stub.Get_it2(arphello_pb2.arpRequest(query_content="127.0.0.1"))
    print("---------客户端收到信息----------")
    print(response.arp_info)

if __name__ == "__main__":
    run()