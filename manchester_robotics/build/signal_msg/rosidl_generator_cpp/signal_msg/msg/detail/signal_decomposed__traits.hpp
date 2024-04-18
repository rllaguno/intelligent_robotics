// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__TRAITS_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "signal_msg/msg/detail/signal_decomposed__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace signal_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const SignalDecomposed & msg,
  std::ostream & out)
{
  out << "{";
  // member: path
  {
    out << "path: ";
    rosidl_generator_traits::value_to_yaml(msg.path, out);
    out << ", ";
  }

  // member: distance1
  {
    out << "distance1: ";
    rosidl_generator_traits::value_to_yaml(msg.distance1, out);
    out << ", ";
  }

  // member: distance2
  {
    out << "distance2: ";
    rosidl_generator_traits::value_to_yaml(msg.distance2, out);
    out << ", ";
  }

  // member: distance3
  {
    out << "distance3: ";
    rosidl_generator_traits::value_to_yaml(msg.distance3, out);
    out << ", ";
  }

  // member: distance4
  {
    out << "distance4: ";
    rosidl_generator_traits::value_to_yaml(msg.distance4, out);
    out << ", ";
  }

  // member: angle1
  {
    out << "angle1: ";
    rosidl_generator_traits::value_to_yaml(msg.angle1, out);
    out << ", ";
  }

  // member: angle2
  {
    out << "angle2: ";
    rosidl_generator_traits::value_to_yaml(msg.angle2, out);
    out << ", ";
  }

  // member: angle3
  {
    out << "angle3: ";
    rosidl_generator_traits::value_to_yaml(msg.angle3, out);
    out << ", ";
  }

  // member: angle4
  {
    out << "angle4: ";
    rosidl_generator_traits::value_to_yaml(msg.angle4, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SignalDecomposed & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "path: ";
    rosidl_generator_traits::value_to_yaml(msg.path, out);
    out << "\n";
  }

  // member: distance1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance1: ";
    rosidl_generator_traits::value_to_yaml(msg.distance1, out);
    out << "\n";
  }

  // member: distance2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance2: ";
    rosidl_generator_traits::value_to_yaml(msg.distance2, out);
    out << "\n";
  }

  // member: distance3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance3: ";
    rosidl_generator_traits::value_to_yaml(msg.distance3, out);
    out << "\n";
  }

  // member: distance4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance4: ";
    rosidl_generator_traits::value_to_yaml(msg.distance4, out);
    out << "\n";
  }

  // member: angle1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle1: ";
    rosidl_generator_traits::value_to_yaml(msg.angle1, out);
    out << "\n";
  }

  // member: angle2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle2: ";
    rosidl_generator_traits::value_to_yaml(msg.angle2, out);
    out << "\n";
  }

  // member: angle3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle3: ";
    rosidl_generator_traits::value_to_yaml(msg.angle3, out);
    out << "\n";
  }

  // member: angle4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle4: ";
    rosidl_generator_traits::value_to_yaml(msg.angle4, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SignalDecomposed & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace signal_msg

namespace rosidl_generator_traits
{

[[deprecated("use signal_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const signal_msg::msg::SignalDecomposed & msg,
  std::ostream & out, size_t indentation = 0)
{
  signal_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use signal_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const signal_msg::msg::SignalDecomposed & msg)
{
  return signal_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<signal_msg::msg::SignalDecomposed>()
{
  return "signal_msg::msg::SignalDecomposed";
}

template<>
inline const char * name<signal_msg::msg::SignalDecomposed>()
{
  return "signal_msg/msg/SignalDecomposed";
}

template<>
struct has_fixed_size<signal_msg::msg::SignalDecomposed>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<signal_msg::msg::SignalDecomposed>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<signal_msg::msg::SignalDecomposed>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__TRAITS_HPP_
