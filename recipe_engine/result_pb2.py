# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='result.proto',
  package='recipe_engine',
  syntax='proto3',
  serialized_pb=_b('\n\x0cresult.proto\x12\rrecipe_engine\"Z\n\x06Result\x12\x15\n\x0bjson_result\x18\x01 \x01(\tH\x00\x12)\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x16.recipe_engine.FailureH\x00\x42\x0e\n\x0coneof_result\"\xe6\x01\n\x07\x46\x61ilure\x12\x14\n\x0chuman_reason\x18\x01 \x01(\t\x12)\n\x07timeout\x18\x02 \x01(\x0b\x32\x16.recipe_engine.TimeoutH\x00\x12-\n\texception\x18\x03 \x01(\x0b\x32\x18.recipe_engine.ExceptionH\x00\x12,\n\tstep_data\x18\x04 \x01(\x0b\x32\x17.recipe_engine.StepDataH\x00\x12-\n\x07\x66\x61ilure\x18\x05 \x01(\x0b\x32\x1a.recipe_engine.StepFailureH\x00\x42\x0e\n\x0c\x66\x61ilure_type\"\x1e\n\tException\x12\x11\n\ttraceback\x18\x01 \x03(\t\"\x1c\n\x07Timeout\x12\x11\n\ttimeout_s\x18\x01 \x01(\x02\"\x18\n\x08StepData\x12\x0c\n\x04step\x18\x01 \x01(\t\"\x1b\n\x0bStepFailure\x12\x0c\n\x04step\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='recipe_engine.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_result', full_name='recipe_engine.Result.json_result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failure', full_name='recipe_engine.Result.failure', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='oneof_result', full_name='recipe_engine.Result.oneof_result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=31,
  serialized_end=121,
)


_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='recipe_engine.Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='human_reason', full_name='recipe_engine.Failure.human_reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='recipe_engine.Failure.timeout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exception', full_name='recipe_engine.Failure.exception', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_data', full_name='recipe_engine.Failure.step_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failure', full_name='recipe_engine.Failure.failure', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='failure_type', full_name='recipe_engine.Failure.failure_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=124,
  serialized_end=354,
)


_EXCEPTION = _descriptor.Descriptor(
  name='Exception',
  full_name='recipe_engine.Exception',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceback', full_name='recipe_engine.Exception.traceback', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=386,
)


_TIMEOUT = _descriptor.Descriptor(
  name='Timeout',
  full_name='recipe_engine.Timeout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout_s', full_name='recipe_engine.Timeout.timeout_s', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=416,
)


_STEPDATA = _descriptor.Descriptor(
  name='StepData',
  full_name='recipe_engine.StepData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='recipe_engine.StepData.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=442,
)


_STEPFAILURE = _descriptor.Descriptor(
  name='StepFailure',
  full_name='recipe_engine.StepFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='recipe_engine.StepFailure.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=471,
)

_RESULT.fields_by_name['failure'].message_type = _FAILURE
_RESULT.oneofs_by_name['oneof_result'].fields.append(
  _RESULT.fields_by_name['json_result'])
_RESULT.fields_by_name['json_result'].containing_oneof = _RESULT.oneofs_by_name['oneof_result']
_RESULT.oneofs_by_name['oneof_result'].fields.append(
  _RESULT.fields_by_name['failure'])
_RESULT.fields_by_name['failure'].containing_oneof = _RESULT.oneofs_by_name['oneof_result']
_FAILURE.fields_by_name['timeout'].message_type = _TIMEOUT
_FAILURE.fields_by_name['exception'].message_type = _EXCEPTION
_FAILURE.fields_by_name['step_data'].message_type = _STEPDATA
_FAILURE.fields_by_name['failure'].message_type = _STEPFAILURE
_FAILURE.oneofs_by_name['failure_type'].fields.append(
  _FAILURE.fields_by_name['timeout'])
_FAILURE.fields_by_name['timeout'].containing_oneof = _FAILURE.oneofs_by_name['failure_type']
_FAILURE.oneofs_by_name['failure_type'].fields.append(
  _FAILURE.fields_by_name['exception'])
_FAILURE.fields_by_name['exception'].containing_oneof = _FAILURE.oneofs_by_name['failure_type']
_FAILURE.oneofs_by_name['failure_type'].fields.append(
  _FAILURE.fields_by_name['step_data'])
_FAILURE.fields_by_name['step_data'].containing_oneof = _FAILURE.oneofs_by_name['failure_type']
_FAILURE.oneofs_by_name['failure_type'].fields.append(
  _FAILURE.fields_by_name['failure'])
_FAILURE.fields_by_name['failure'].containing_oneof = _FAILURE.oneofs_by_name['failure_type']
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
DESCRIPTOR.message_types_by_name['Exception'] = _EXCEPTION
DESCRIPTOR.message_types_by_name['Timeout'] = _TIMEOUT
DESCRIPTOR.message_types_by_name['StepData'] = _STEPDATA
DESCRIPTOR.message_types_by_name['StepFailure'] = _STEPFAILURE

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Result)
  ))
_sym_db.RegisterMessage(Result)

Failure = _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), dict(
  DESCRIPTOR = _FAILURE,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Failure)
  ))
_sym_db.RegisterMessage(Failure)

Exception = _reflection.GeneratedProtocolMessageType('Exception', (_message.Message,), dict(
  DESCRIPTOR = _EXCEPTION,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Exception)
  ))
_sym_db.RegisterMessage(Exception)

Timeout = _reflection.GeneratedProtocolMessageType('Timeout', (_message.Message,), dict(
  DESCRIPTOR = _TIMEOUT,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Timeout)
  ))
_sym_db.RegisterMessage(Timeout)

StepData = _reflection.GeneratedProtocolMessageType('StepData', (_message.Message,), dict(
  DESCRIPTOR = _STEPDATA,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.StepData)
  ))
_sym_db.RegisterMessage(StepData)

StepFailure = _reflection.GeneratedProtocolMessageType('StepFailure', (_message.Message,), dict(
  DESCRIPTOR = _STEPFAILURE,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.StepFailure)
  ))
_sym_db.RegisterMessage(StepFailure)


# @@protoc_insertion_point(module_scope)
