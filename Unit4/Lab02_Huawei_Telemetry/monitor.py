from concurrent import futures
import time
import importlib
import grpc                         
import huawei_grpc_dialout_pb2_grpc  
import huawei_telemetry_pb2        


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def serve():
  #创建一个grpc server对象
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))    
  #注册huawei的telemetry数据监听服务
  huawei_grpc_dialout_pb2_grpc.add_gRPCDataserviceServicer_to_server(
      Telemetry_CPU_Info(), server)     
  #设置socket监听端口
  server.add_insecure_port('192.168.1.6:20000')     
  #启动grpc server
  server.start()
  #死循环监听
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

#创建类继承huawei_grpc_dialout_pb2_grpc中Servicer方法    
class Telemetry_CPU_Info(huawei_grpc_dialout_pb2_grpc.gRPCDataserviceServicer): 
    def __init__(self):
        return
    
    def dataPublish(self, request_iterator, context):
        for i in request_iterator:
            print ('############ start ############\n')
            telemetry_data = huawei_telemetry_pb2.Telemetry.FromString(i.data)
            print (telemetry_data)            
            
            for row_data in  telemetry_data.data_gpb.row:
                print ('-----------------')
                print ('The proto path is :'+telemetry_data.proto_path)
                print ('-----------------')
                module_name = telemetry_data.proto_path.split('.')[0]
                root_class  = telemetry_data.proto_path.split('.')[1]
                
				#动态加载telemetry获取数据的对应模块，本例中为
                decode_module = importlib.import_module( module_name+'_pb2')
                print (decode_module)
                
				#定义解码方法：getattr获取动态加载的模块中的属性值，调用此属性的解码方法FromString
                decode_func = getattr(decode_module,root_class).FromString
                
                print ('----------- content is -----------\n')
				# 将row_data中的content中的内容使用此方法解码，并输出
                print (decode_func(row_data.content))
                print ('----------- done -----------------')


if __name__ == '__main__':
  serve()