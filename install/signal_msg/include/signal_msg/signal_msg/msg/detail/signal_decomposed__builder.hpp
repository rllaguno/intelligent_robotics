// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__BUILDER_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "signal_msg/msg/detail/signal_decomposed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace signal_msg
{

namespace msg
{

namespace builder
{

class Init_SignalDecomposed_angle4
{
public:
  explicit Init_SignalDecomposed_angle4(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  ::signal_msg::msg::SignalDecomposed angle4(::signal_msg::msg::SignalDecomposed::_angle4_type arg)
  {
    msg_.angle4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_angle3
{
public:
  explicit Init_SignalDecomposed_angle3(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_angle4 angle3(::signal_msg::msg::SignalDecomposed::_angle3_type arg)
  {
    msg_.angle3 = std::move(arg);
    return Init_SignalDecomposed_angle4(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_angle2
{
public:
  explicit Init_SignalDecomposed_angle2(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_angle3 angle2(::signal_msg::msg::SignalDecomposed::_angle2_type arg)
  {
    msg_.angle2 = std::move(arg);
    return Init_SignalDecomposed_angle3(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_angle1
{
public:
  explicit Init_SignalDecomposed_angle1(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_angle2 angle1(::signal_msg::msg::SignalDecomposed::_angle1_type arg)
  {
    msg_.angle1 = std::move(arg);
    return Init_SignalDecomposed_angle2(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_distance4
{
public:
  explicit Init_SignalDecomposed_distance4(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_angle1 distance4(::signal_msg::msg::SignalDecomposed::_distance4_type arg)
  {
    msg_.distance4 = std::move(arg);
    return Init_SignalDecomposed_angle1(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_distance3
{
public:
  explicit Init_SignalDecomposed_distance3(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_distance4 distance3(::signal_msg::msg::SignalDecomposed::_distance3_type arg)
  {
    msg_.distance3 = std::move(arg);
    return Init_SignalDecomposed_distance4(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_distance2
{
public:
  explicit Init_SignalDecomposed_distance2(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_distance3 distance2(::signal_msg::msg::SignalDecomposed::_distance2_type arg)
  {
    msg_.distance2 = std::move(arg);
    return Init_SignalDecomposed_distance3(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_distance1
{
public:
  explicit Init_SignalDecomposed_distance1(::signal_msg::msg::SignalDecomposed & msg)
  : msg_(msg)
  {}
  Init_SignalDecomposed_distance2 distance1(::signal_msg::msg::SignalDecomposed::_distance1_type arg)
  {
    msg_.distance1 = std::move(arg);
    return Init_SignalDecomposed_distance2(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

class Init_SignalDecomposed_path
{
public:
  Init_SignalDecomposed_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SignalDecomposed_distance1 path(::signal_msg::msg::SignalDecomposed::_path_type arg)
  {
    msg_.path = std::move(arg);
    return Init_SignalDecomposed_distance1(msg_);
  }

private:
  ::signal_msg::msg::SignalDecomposed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::signal_msg::msg::SignalDecomposed>()
{
  return signal_msg::msg::builder::Init_SignalDecomposed_path();
}

}  // namespace signal_msg

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__BUILDER_HPP_
