# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player_badge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player_badge.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\"pogoprotos/data/player_badge.proto\x12\x0fpogoprotos.data\x1a!pogoprotos/enums/badge_type.proto\"\x8b\x01\n\x0bPlayerBadge\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.BadgeType\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x13\n\x0bstart_value\x18\x03 \x01(\x05\x12\x11\n\tend_value\x18\x04 \x01(\x05\x12\x15\n\rcurrent_value\x18\x05 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERBADGE = _descriptor.Descriptor(
  name='PlayerBadge',
  full_name='pogoprotos.data.PlayerBadge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='pogoprotos.data.PlayerBadge.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='pogoprotos.data.PlayerBadge.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_value', full_name='pogoprotos.data.PlayerBadge.start_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_value', full_name='pogoprotos.data.PlayerBadge.end_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_value', full_name='pogoprotos.data.PlayerBadge.current_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=91,
  serialized_end=230,
)

_PLAYERBADGE.fields_by_name['badge_type'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['PlayerBadge'] = _PLAYERBADGE

PlayerBadge = _reflection.GeneratedProtocolMessageType('PlayerBadge', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERBADGE,
  __module__ = 'pogoprotos.data.player_badge_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PlayerBadge)
  ))
_sym_db.RegisterMessage(PlayerBadge)


# @@protoc_insertion_point(module_scope)