// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__STRUCT_HPP_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__signal_msg__msg__SignalDecomposed __attribute__((deprecated))
#else
# define DEPRECATED__signal_msg__msg__SignalDecomposed __declspec(deprecated)
#endif

namespace signal_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SignalDecomposed_
{
  using Type = SignalDecomposed_<ContainerAllocator>;

  explicit SignalDecomposed_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->path = 0l;
      this->distance1 = 0.0f;
      this->distance2 = 0.0f;
      this->distance3 = 0.0f;
      this->distance4 = 0.0f;
      this->angle1 = 0.0f;
      this->angle2 = 0.0f;
      this->angle3 = 0.0f;
      this->angle4 = 0.0f;
    }
  }

  explicit SignalDecomposed_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->path = 0l;
      this->distance1 = 0.0f;
      this->distance2 = 0.0f;
      this->distance3 = 0.0f;
      this->distance4 = 0.0f;
      this->angle1 = 0.0f;
      this->angle2 = 0.0f;
      this->angle3 = 0.0f;
      this->angle4 = 0.0f;
    }
  }

  // field types and members
  using _path_type =
    int32_t;
  _path_type path;
  using _distance1_type =
    float;
  _distance1_type distance1;
  using _distance2_type =
    float;
  _distance2_type distance2;
  using _distance3_type =
    float;
  _distance3_type distance3;
  using _distance4_type =
    float;
  _distance4_type distance4;
  using _angle1_type =
    float;
  _angle1_type angle1;
  using _angle2_type =
    float;
  _angle2_type angle2;
  using _angle3_type =
    float;
  _angle3_type angle3;
  using _angle4_type =
    float;
  _angle4_type angle4;

  // setters for named parameter idiom
  Type & set__path(
    const int32_t & _arg)
  {
    this->path = _arg;
    return *this;
  }
  Type & set__distance1(
    const float & _arg)
  {
    this->distance1 = _arg;
    return *this;
  }
  Type & set__distance2(
    const float & _arg)
  {
    this->distance2 = _arg;
    return *this;
  }
  Type & set__distance3(
    const float & _arg)
  {
    this->distance3 = _arg;
    return *this;
  }
  Type & set__distance4(
    const float & _arg)
  {
    this->distance4 = _arg;
    return *this;
  }
  Type & set__angle1(
    const float & _arg)
  {
    this->angle1 = _arg;
    return *this;
  }
  Type & set__angle2(
    const float & _arg)
  {
    this->angle2 = _arg;
    return *this;
  }
  Type & set__angle3(
    const float & _arg)
  {
    this->angle3 = _arg;
    return *this;
  }
  Type & set__angle4(
    const float & _arg)
  {
    this->angle4 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    signal_msg::msg::SignalDecomposed_<ContainerAllocator> *;
  using ConstRawPtr =
    const signal_msg::msg::SignalDecomposed_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      signal_msg::msg::SignalDecomposed_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      signal_msg::msg::SignalDecomposed_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__signal_msg__msg__SignalDecomposed
    std::shared_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__signal_msg__msg__SignalDecomposed
    std::shared_ptr<signal_msg::msg::SignalDecomposed_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SignalDecomposed_ & other) const
  {
    if (this->path != other.path) {
      return false;
    }
    if (this->distance1 != other.distance1) {
      return false;
    }
    if (this->distance2 != other.distance2) {
      return false;
    }
    if (this->distance3 != other.distance3) {
      return false;
    }
    if (this->distance4 != other.distance4) {
      return false;
    }
    if (this->angle1 != other.angle1) {
      return false;
    }
    if (this->angle2 != other.angle2) {
      return false;
    }
    if (this->angle3 != other.angle3) {
      return false;
    }
    if (this->angle4 != other.angle4) {
      return false;
    }
    return true;
  }
  bool operator!=(const SignalDecomposed_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SignalDecomposed_

// alias to use template instance with default allocator
using SignalDecomposed =
  signal_msg::msg::SignalDecomposed_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace signal_msg

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__STRUCT_HPP_
