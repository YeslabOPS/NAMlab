from grpc_tools import protoc

protoc.main(
    (
        '',
        '-I./proto',
        '--python_out=.',
        '--grpc_python_out=.',
        './proto/huawei-grpc-dialout.proto'
    )
)

protoc.main(
    (
        '',
        '-I./proto',
        '--python_out=.',
        '--grpc_python_out=.',
        './proto/huawei-telemetry.proto'
    )
)

protoc.main(
    (
        '',
        '-I./proto',
        '--python_out=.',
        '--grpc_python_out=.',
        './proto/huawei-devm.proto'
    )
)