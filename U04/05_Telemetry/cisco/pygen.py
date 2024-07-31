from grpc_tools import protoc

protoc.main(
    (
        '',
        '-I./proto',
        '--python_out=.',
        '--grpc_python_out=.',
        './proto/protoxemdt_grpc_dialout.proto'
    )
)

protoc.main(
    (
        '',
        '-I./proto',
        '--python_out=.',
        '--grpc_python_out=.',
        './proto/telemetry.proto'
    )
)