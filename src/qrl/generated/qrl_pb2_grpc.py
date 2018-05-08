# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import qrl.generated.qrl_pb2 as qrl__pb2


class PublicAPIStub(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetNodeState = channel.unary_unary(
        '/qrl.PublicAPI/GetNodeState',
        request_serializer=qrl__pb2.GetNodeStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetNodeStateResp.FromString,
        )
    self.GetKnownPeers = channel.unary_unary(
        '/qrl.PublicAPI/GetKnownPeers',
        request_serializer=qrl__pb2.GetKnownPeersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetKnownPeersResp.FromString,
        )
    self.GetPeersStat = channel.unary_unary(
        '/qrl.PublicAPI/GetPeersStat',
        request_serializer=qrl__pb2.GetPeersStatReq.SerializeToString,
        response_deserializer=qrl__pb2.GetPeersStatResp.FromString,
        )
    self.GetStats = channel.unary_unary(
        '/qrl.PublicAPI/GetStats',
        request_serializer=qrl__pb2.GetStatsReq.SerializeToString,
        response_deserializer=qrl__pb2.GetStatsResp.FromString,
        )
    self.GetAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressState',
        request_serializer=qrl__pb2.GetAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressStateResp.FromString,
        )
    self.GetObject = channel.unary_unary(
        '/qrl.PublicAPI/GetObject',
        request_serializer=qrl__pb2.GetObjectReq.SerializeToString,
        response_deserializer=qrl__pb2.GetObjectResp.FromString,
        )
    self.GetLatestData = channel.unary_unary(
        '/qrl.PublicAPI/GetLatestData',
        request_serializer=qrl__pb2.GetLatestDataReq.SerializeToString,
        response_deserializer=qrl__pb2.GetLatestDataResp.FromString,
        )
    self.TransferCoins = channel.unary_unary(
        '/qrl.PublicAPI/TransferCoins',
        request_serializer=qrl__pb2.TransferCoinsReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.PushTransaction = channel.unary_unary(
        '/qrl.PublicAPI/PushTransaction',
        request_serializer=qrl__pb2.PushTransactionReq.SerializeToString,
        response_deserializer=qrl__pb2.PushTransactionResp.FromString,
        )
    self.GetMessageTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetMessageTxn',
        request_serializer=qrl__pb2.MessageTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetTokenTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetTokenTxn',
        request_serializer=qrl__pb2.TokenTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetTransferTokenTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetTransferTokenTxn',
        request_serializer=qrl__pb2.TransferTokenTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetSlaveTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetSlaveTxn',
        request_serializer=qrl__pb2.SlaveTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetLatticePublicKeyTxn = channel.unary_unary(
        '/qrl.PublicAPI/GetLatticePublicKeyTxn',
        request_serializer=qrl__pb2.LatticePublicKeyTxnReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.GetAddressFromPK = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressFromPK',
        request_serializer=qrl__pb2.GetAddressFromPKReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressFromPKResp.FromString,
        )


class PublicAPIServicer(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Public API used by clients (wallet/cli/etc)
  """

  def GetNodeState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKnownPeers(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPeersStat(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStats(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObject(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestData(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferCoins(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMessageTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokenTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransferTokenTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlaveTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatticePublicKeyTxn(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressFromPK(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetNodeState': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeState,
          request_deserializer=qrl__pb2.GetNodeStateReq.FromString,
          response_serializer=qrl__pb2.GetNodeStateResp.SerializeToString,
      ),
      'GetKnownPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnownPeers,
          request_deserializer=qrl__pb2.GetKnownPeersReq.FromString,
          response_serializer=qrl__pb2.GetKnownPeersResp.SerializeToString,
      ),
      'GetPeersStat': grpc.unary_unary_rpc_method_handler(
          servicer.GetPeersStat,
          request_deserializer=qrl__pb2.GetPeersStatReq.FromString,
          response_serializer=qrl__pb2.GetPeersStatResp.SerializeToString,
      ),
      'GetStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetStats,
          request_deserializer=qrl__pb2.GetStatsReq.FromString,
          response_serializer=qrl__pb2.GetStatsResp.SerializeToString,
      ),
      'GetAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressState,
          request_deserializer=qrl__pb2.GetAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetAddressStateResp.SerializeToString,
      ),
      'GetObject': grpc.unary_unary_rpc_method_handler(
          servicer.GetObject,
          request_deserializer=qrl__pb2.GetObjectReq.FromString,
          response_serializer=qrl__pb2.GetObjectResp.SerializeToString,
      ),
      'GetLatestData': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestData,
          request_deserializer=qrl__pb2.GetLatestDataReq.FromString,
          response_serializer=qrl__pb2.GetLatestDataResp.SerializeToString,
      ),
      'TransferCoins': grpc.unary_unary_rpc_method_handler(
          servicer.TransferCoins,
          request_deserializer=qrl__pb2.TransferCoinsReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'PushTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.PushTransaction,
          request_deserializer=qrl__pb2.PushTransactionReq.FromString,
          response_serializer=qrl__pb2.PushTransactionResp.SerializeToString,
      ),
      'GetMessageTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessageTxn,
          request_deserializer=qrl__pb2.MessageTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetTokenTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokenTxn,
          request_deserializer=qrl__pb2.TokenTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetTransferTokenTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransferTokenTxn,
          request_deserializer=qrl__pb2.TransferTokenTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetSlaveTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlaveTxn,
          request_deserializer=qrl__pb2.SlaveTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetLatticePublicKeyTxn': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatticePublicKeyTxn,
          request_deserializer=qrl__pb2.LatticePublicKeyTxnReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'GetAddressFromPK': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressFromPK,
          request_deserializer=qrl__pb2.GetAddressFromPKReq.FromString,
          response_serializer=qrl__pb2.GetAddressFromPKResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.PublicAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AdminAPIStub(object):
  """This is a place holder for testing/instrumentation APIs
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class AdminAPIServicer(object):
  """This is a place holder for testing/instrumentation APIs
  """


def add_AdminAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.AdminAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
