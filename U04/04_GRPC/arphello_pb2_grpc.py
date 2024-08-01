# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import arphello_pb2 as arphello__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in arphello_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class get_arpStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login_info = channel.unary_unary(
                '/get_arp.get_arp/Login_info',
                request_serializer=arphello__pb2.arpRequest.SerializeToString,
                response_deserializer=arphello__pb2.arpReply.FromString,
                _registered_method=True)


class get_arpServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_get_arpServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login_info': grpc.unary_unary_rpc_method_handler(
                    servicer.Login_info,
                    request_deserializer=arphello__pb2.arpRequest.FromString,
                    response_serializer=arphello__pb2.arpReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'get_arp.get_arp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('get_arp.get_arp', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class get_arp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/get_arp.get_arp/Login_info',
            arphello__pb2.arpRequest.SerializeToString,
            arphello__pb2.arpReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)