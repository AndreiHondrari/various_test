# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Message.proto',
  package='sample',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rMessage.proto\x12\x06sample\"\x9b\x01\n\x07Message\x12\x10\n\x03\x62la\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x02\x61\x31\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x0f\n\x02\x61\x32\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x0f\n\x02\x61\x33\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x0f\n\x02\x61\x34\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x0f\n\x02\x61\x35\x18\x06 \x01(\x05H\x05\x88\x01\x01\x42\x06\n\x04_blaB\x05\n\x03_a1B\x05\n\x03_a2B\x05\n\x03_a3B\x05\n\x03_a4B\x05\n\x03_a5b\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='sample.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bla', full_name='sample.Message.bla', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a1', full_name='sample.Message.a1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a2', full_name='sample.Message.a2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a3', full_name='sample.Message.a3', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a4', full_name='sample.Message.a4', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a5', full_name='sample.Message.a5', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_bla', full_name='sample.Message._bla',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_a1', full_name='sample.Message._a1',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_a2', full_name='sample.Message._a2',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_a3', full_name='sample.Message._a3',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_a4', full_name='sample.Message._a4',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_a5', full_name='sample.Message._a5',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=26,
  serialized_end=181,
)

_MESSAGE.oneofs_by_name['_bla'].fields.append(
  _MESSAGE.fields_by_name['bla'])
_MESSAGE.fields_by_name['bla'].containing_oneof = _MESSAGE.oneofs_by_name['_bla']
_MESSAGE.oneofs_by_name['_a1'].fields.append(
  _MESSAGE.fields_by_name['a1'])
_MESSAGE.fields_by_name['a1'].containing_oneof = _MESSAGE.oneofs_by_name['_a1']
_MESSAGE.oneofs_by_name['_a2'].fields.append(
  _MESSAGE.fields_by_name['a2'])
_MESSAGE.fields_by_name['a2'].containing_oneof = _MESSAGE.oneofs_by_name['_a2']
_MESSAGE.oneofs_by_name['_a3'].fields.append(
  _MESSAGE.fields_by_name['a3'])
_MESSAGE.fields_by_name['a3'].containing_oneof = _MESSAGE.oneofs_by_name['_a3']
_MESSAGE.oneofs_by_name['_a4'].fields.append(
  _MESSAGE.fields_by_name['a4'])
_MESSAGE.fields_by_name['a4'].containing_oneof = _MESSAGE.oneofs_by_name['_a4']
_MESSAGE.oneofs_by_name['_a5'].fields.append(
  _MESSAGE.fields_by_name['a5'])
_MESSAGE.fields_by_name['a5'].containing_oneof = _MESSAGE.oneofs_by_name['_a5']
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'Message_pb2'
  # @@protoc_insertion_point(class_scope:sample.Message)
  })
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
