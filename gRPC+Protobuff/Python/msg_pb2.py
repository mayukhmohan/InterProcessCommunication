# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg.proto',
  package='msg',
  syntax='proto3',
  serialized_options=b'\n\034com.mayukh.grpc_standardizedP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmsg.proto\x12\x03msg\"\'\n\x07Message\x12\x1c\n\x07message\x18\x01 \x03(\x0b\x32\x0b.msg.Course\"?\n\x0fMessageResponse\x12,\n\x0fmessageResponse\x18\x01 \x03(\x0b\x32\x13.msg.CourseResponse\"\xcd\x01\n\x06\x43ourse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63ourse_name\x18\x02 \x01(\t\x12\x11\n\tavg_marks\x18\x03 \x01(\x02\x12+\n\rend_of_course\x18\x04 \x01(\x0b\x32\x14.msg.Course.DateTime\x1a\x62\n\x08\x44\x61teTime\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x0c\n\x04hour\x18\x04 \x01(\x05\x12\x0e\n\x06minute\x18\x05 \x01(\x05\x12\x0e\n\x06second\x18\x06 \x01(\x05\"\xe4\x01\n\x0e\x43ourseResponse\x12\x11\n\tCourse_ID\x18\x01 \x01(\x05\x12\x13\n\x0b\x43ourse_Name\x18\x02 \x01(\t\x12\x11\n\tAvg_Marks\x18\x03 \x01(\x02\x12\x33\n\rEND_of_COURSE\x18\x04 \x01(\x0b\x32\x1c.msg.CourseResponse.DateTime\x1a\x62\n\x08\x44\x61teTime\x12\x0c\n\x04Year\x18\x01 \x01(\x05\x12\r\n\x05Month\x18\x02 \x01(\x05\x12\x0b\n\x03\x44\x61y\x18\x03 \x01(\x05\x12\x0c\n\x04Hour\x18\x04 \x01(\x05\x12\x0e\n\x06Minute\x18\x05 \x01(\x05\x12\x0e\n\x06Second\x18\x06 \x01(\x05\x32>\n\x03Msg\x12\x37\n\x11getServerResponse\x12\x0c.msg.Message\x1a\x14.msg.MessageResponseB \n\x1c\x63om.mayukh.grpc_standardizedP\x01\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='msg.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='msg.Message.message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=18,
  serialized_end=57,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='msg.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageResponse', full_name='msg.MessageResponse.messageResponse', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=59,
  serialized_end=122,
)


_COURSE_DATETIME = _descriptor.Descriptor(
  name='DateTime',
  full_name='msg.Course.DateTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='msg.Course.DateTime.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='msg.Course.DateTime.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='msg.Course.DateTime.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hour', full_name='msg.Course.DateTime.hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minute', full_name='msg.Course.DateTime.minute', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='msg.Course.DateTime.second', index=5,
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
  ],
  serialized_start=232,
  serialized_end=330,
)

_COURSE = _descriptor.Descriptor(
  name='Course',
  full_name='msg.Course',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='msg.Course.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='course_name', full_name='msg.Course.course_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_marks', full_name='msg.Course.avg_marks', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_of_course', full_name='msg.Course.end_of_course', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COURSE_DATETIME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=330,
)


_COURSERESPONSE_DATETIME = _descriptor.Descriptor(
  name='DateTime',
  full_name='msg.CourseResponse.DateTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Year', full_name='msg.CourseResponse.DateTime.Year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Month', full_name='msg.CourseResponse.DateTime.Month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Day', full_name='msg.CourseResponse.DateTime.Day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Hour', full_name='msg.CourseResponse.DateTime.Hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Minute', full_name='msg.CourseResponse.DateTime.Minute', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Second', full_name='msg.CourseResponse.DateTime.Second', index=5,
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
  ],
  serialized_start=463,
  serialized_end=561,
)

_COURSERESPONSE = _descriptor.Descriptor(
  name='CourseResponse',
  full_name='msg.CourseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Course_ID', full_name='msg.CourseResponse.Course_ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Course_Name', full_name='msg.CourseResponse.Course_Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Avg_Marks', full_name='msg.CourseResponse.Avg_Marks', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='END_of_COURSE', full_name='msg.CourseResponse.END_of_COURSE', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COURSERESPONSE_DATETIME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=561,
)

_MESSAGE.fields_by_name['message'].message_type = _COURSE
_MESSAGERESPONSE.fields_by_name['messageResponse'].message_type = _COURSERESPONSE
_COURSE_DATETIME.containing_type = _COURSE
_COURSE.fields_by_name['end_of_course'].message_type = _COURSE_DATETIME
_COURSERESPONSE_DATETIME.containing_type = _COURSERESPONSE
_COURSERESPONSE.fields_by_name['END_of_COURSE'].message_type = _COURSERESPONSE_DATETIME
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
DESCRIPTOR.message_types_by_name['Course'] = _COURSE
DESCRIPTOR.message_types_by_name['CourseResponse'] = _COURSERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:msg.Message)
  })
_sym_db.RegisterMessage(Message)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:msg.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

Course = _reflection.GeneratedProtocolMessageType('Course', (_message.Message,), {

  'DateTime' : _reflection.GeneratedProtocolMessageType('DateTime', (_message.Message,), {
    'DESCRIPTOR' : _COURSE_DATETIME,
    '__module__' : 'msg_pb2'
    # @@protoc_insertion_point(class_scope:msg.Course.DateTime)
    })
  ,
  'DESCRIPTOR' : _COURSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:msg.Course)
  })
_sym_db.RegisterMessage(Course)
_sym_db.RegisterMessage(Course.DateTime)

CourseResponse = _reflection.GeneratedProtocolMessageType('CourseResponse', (_message.Message,), {

  'DateTime' : _reflection.GeneratedProtocolMessageType('DateTime', (_message.Message,), {
    'DESCRIPTOR' : _COURSERESPONSE_DATETIME,
    '__module__' : 'msg_pb2'
    # @@protoc_insertion_point(class_scope:msg.CourseResponse.DateTime)
    })
  ,
  'DESCRIPTOR' : _COURSERESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:msg.CourseResponse)
  })
_sym_db.RegisterMessage(CourseResponse)
_sym_db.RegisterMessage(CourseResponse.DateTime)


DESCRIPTOR._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='msg.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=563,
  serialized_end=625,
  methods=[
  _descriptor.MethodDescriptor(
    name='getServerResponse',
    full_name='msg.Msg.getServerResponse',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
