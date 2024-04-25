// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "signal_msg/msg/detail/signal_decomposed__rosidl_typesupport_introspection_c.h"
#include "signal_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "signal_msg/msg/detail/signal_decomposed__functions.h"
#include "signal_msg/msg/detail/signal_decomposed__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  signal_msg__msg__SignalDecomposed__init(message_memory);
}

void signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_fini_function(void * message_memory)
{
  signal_msg__msg__SignalDecomposed__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_member_array[9] = {
  {
    "path",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, path),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, distance1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, distance2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance3",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, distance3),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance4",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, distance4),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angle1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, angle1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angle2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, angle2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angle3",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, angle3),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angle4",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(signal_msg__msg__SignalDecomposed, angle4),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_members = {
  "signal_msg__msg",  // message namespace
  "SignalDecomposed",  // message name
  9,  // number of fields
  sizeof(signal_msg__msg__SignalDecomposed),
  signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_member_array,  // message members
  signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_init_function,  // function to initialize message memory (memory has to be allocated)
  signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_type_support_handle = {
  0,
  &signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_signal_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, signal_msg, msg, SignalDecomposed)() {
  if (!signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_type_support_handle.typesupport_identifier) {
    signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &signal_msg__msg__SignalDecomposed__rosidl_typesupport_introspection_c__SignalDecomposed_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
