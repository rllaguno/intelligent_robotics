// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__FUNCTIONS_H_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "signal_msg/msg/rosidl_generator_c__visibility_control.h"

#include "signal_msg/msg/detail/signal_decomposed__struct.h"

/// Initialize msg/SignalDecomposed message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * signal_msg__msg__SignalDecomposed
 * )) before or use
 * signal_msg__msg__SignalDecomposed__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__init(signal_msg__msg__SignalDecomposed * msg);

/// Finalize msg/SignalDecomposed message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
void
signal_msg__msg__SignalDecomposed__fini(signal_msg__msg__SignalDecomposed * msg);

/// Create msg/SignalDecomposed message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * signal_msg__msg__SignalDecomposed__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
signal_msg__msg__SignalDecomposed *
signal_msg__msg__SignalDecomposed__create();

/// Destroy msg/SignalDecomposed message.
/**
 * It calls
 * signal_msg__msg__SignalDecomposed__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
void
signal_msg__msg__SignalDecomposed__destroy(signal_msg__msg__SignalDecomposed * msg);

/// Check for msg/SignalDecomposed message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__are_equal(const signal_msg__msg__SignalDecomposed * lhs, const signal_msg__msg__SignalDecomposed * rhs);

/// Copy a msg/SignalDecomposed message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__copy(
  const signal_msg__msg__SignalDecomposed * input,
  signal_msg__msg__SignalDecomposed * output);

/// Initialize array of msg/SignalDecomposed messages.
/**
 * It allocates the memory for the number of elements and calls
 * signal_msg__msg__SignalDecomposed__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__Sequence__init(signal_msg__msg__SignalDecomposed__Sequence * array, size_t size);

/// Finalize array of msg/SignalDecomposed messages.
/**
 * It calls
 * signal_msg__msg__SignalDecomposed__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
void
signal_msg__msg__SignalDecomposed__Sequence__fini(signal_msg__msg__SignalDecomposed__Sequence * array);

/// Create array of msg/SignalDecomposed messages.
/**
 * It allocates the memory for the array and calls
 * signal_msg__msg__SignalDecomposed__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
signal_msg__msg__SignalDecomposed__Sequence *
signal_msg__msg__SignalDecomposed__Sequence__create(size_t size);

/// Destroy array of msg/SignalDecomposed messages.
/**
 * It calls
 * signal_msg__msg__SignalDecomposed__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
void
signal_msg__msg__SignalDecomposed__Sequence__destroy(signal_msg__msg__SignalDecomposed__Sequence * array);

/// Check for msg/SignalDecomposed message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__Sequence__are_equal(const signal_msg__msg__SignalDecomposed__Sequence * lhs, const signal_msg__msg__SignalDecomposed__Sequence * rhs);

/// Copy an array of msg/SignalDecomposed messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_signal_msg
bool
signal_msg__msg__SignalDecomposed__Sequence__copy(
  const signal_msg__msg__SignalDecomposed__Sequence * input,
  signal_msg__msg__SignalDecomposed__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL_DECOMPOSED__FUNCTIONS_H_
