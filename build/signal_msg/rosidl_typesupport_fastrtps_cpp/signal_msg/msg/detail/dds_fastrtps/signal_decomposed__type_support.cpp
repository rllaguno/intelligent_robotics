// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice
#include "signal_msg/msg/detail/signal_decomposed__rosidl_typesupport_fastrtps_cpp.hpp"
#include "signal_msg/msg/detail/signal_decomposed__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace signal_msg
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_signal_msg
cdr_serialize(
  const signal_msg::msg::SignalDecomposed & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: path
  cdr << ros_message.path;
  // Member: distance1
  cdr << ros_message.distance1;
  // Member: distance2
  cdr << ros_message.distance2;
  // Member: distance3
  cdr << ros_message.distance3;
  // Member: distance4
  cdr << ros_message.distance4;
  // Member: angle1
  cdr << ros_message.angle1;
  // Member: angle2
  cdr << ros_message.angle2;
  // Member: angle3
  cdr << ros_message.angle3;
  // Member: angle4
  cdr << ros_message.angle4;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_signal_msg
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  signal_msg::msg::SignalDecomposed & ros_message)
{
  // Member: path
  cdr >> ros_message.path;

  // Member: distance1
  cdr >> ros_message.distance1;

  // Member: distance2
  cdr >> ros_message.distance2;

  // Member: distance3
  cdr >> ros_message.distance3;

  // Member: distance4
  cdr >> ros_message.distance4;

  // Member: angle1
  cdr >> ros_message.angle1;

  // Member: angle2
  cdr >> ros_message.angle2;

  // Member: angle3
  cdr >> ros_message.angle3;

  // Member: angle4
  cdr >> ros_message.angle4;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_signal_msg
get_serialized_size(
  const signal_msg::msg::SignalDecomposed & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: path
  {
    size_t item_size = sizeof(ros_message.path);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance1
  {
    size_t item_size = sizeof(ros_message.distance1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance2
  {
    size_t item_size = sizeof(ros_message.distance2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance3
  {
    size_t item_size = sizeof(ros_message.distance3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance4
  {
    size_t item_size = sizeof(ros_message.distance4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: angle1
  {
    size_t item_size = sizeof(ros_message.angle1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: angle2
  {
    size_t item_size = sizeof(ros_message.angle2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: angle3
  {
    size_t item_size = sizeof(ros_message.angle3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: angle4
  {
    size_t item_size = sizeof(ros_message.angle4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_signal_msg
max_serialized_size_SignalDecomposed(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: path
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance3
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance4
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: angle1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: angle2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: angle3
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: angle4
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = signal_msg::msg::SignalDecomposed;
    is_plain =
      (
      offsetof(DataType, angle4) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _SignalDecomposed__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const signal_msg::msg::SignalDecomposed *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _SignalDecomposed__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<signal_msg::msg::SignalDecomposed *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _SignalDecomposed__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const signal_msg::msg::SignalDecomposed *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _SignalDecomposed__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_SignalDecomposed(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _SignalDecomposed__callbacks = {
  "signal_msg::msg",
  "SignalDecomposed",
  _SignalDecomposed__cdr_serialize,
  _SignalDecomposed__cdr_deserialize,
  _SignalDecomposed__get_serialized_size,
  _SignalDecomposed__max_serialized_size
};

static rosidl_message_type_support_t _SignalDecomposed__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_SignalDecomposed__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace signal_msg

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_signal_msg
const rosidl_message_type_support_t *
get_message_type_support_handle<signal_msg::msg::SignalDecomposed>()
{
  return &signal_msg::msg::typesupport_fastrtps_cpp::_SignalDecomposed__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, signal_msg, msg, SignalDecomposed)() {
  return &signal_msg::msg::typesupport_fastrtps_cpp::_SignalDecomposed__handle;
}

#ifdef __cplusplus
}
#endif
