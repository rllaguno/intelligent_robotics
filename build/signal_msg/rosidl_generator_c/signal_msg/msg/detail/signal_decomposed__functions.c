// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice
#include "signal_msg/msg/detail/signal_decomposed__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
signal_msg__msg__SignalDecomposed__init(signal_msg__msg__SignalDecomposed * msg)
{
  if (!msg) {
    return false;
  }
  // path
  // distance1
  // distance2
  // distance3
  // distance4
  // angle1
  // angle2
  // angle3
  // angle4
  return true;
}

void
signal_msg__msg__SignalDecomposed__fini(signal_msg__msg__SignalDecomposed * msg)
{
  if (!msg) {
    return;
  }
  // path
  // distance1
  // distance2
  // distance3
  // distance4
  // angle1
  // angle2
  // angle3
  // angle4
}

bool
signal_msg__msg__SignalDecomposed__are_equal(const signal_msg__msg__SignalDecomposed * lhs, const signal_msg__msg__SignalDecomposed * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // path
  if (lhs->path != rhs->path) {
    return false;
  }
  // distance1
  if (lhs->distance1 != rhs->distance1) {
    return false;
  }
  // distance2
  if (lhs->distance2 != rhs->distance2) {
    return false;
  }
  // distance3
  if (lhs->distance3 != rhs->distance3) {
    return false;
  }
  // distance4
  if (lhs->distance4 != rhs->distance4) {
    return false;
  }
  // angle1
  if (lhs->angle1 != rhs->angle1) {
    return false;
  }
  // angle2
  if (lhs->angle2 != rhs->angle2) {
    return false;
  }
  // angle3
  if (lhs->angle3 != rhs->angle3) {
    return false;
  }
  // angle4
  if (lhs->angle4 != rhs->angle4) {
    return false;
  }
  return true;
}

bool
signal_msg__msg__SignalDecomposed__copy(
  const signal_msg__msg__SignalDecomposed * input,
  signal_msg__msg__SignalDecomposed * output)
{
  if (!input || !output) {
    return false;
  }
  // path
  output->path = input->path;
  // distance1
  output->distance1 = input->distance1;
  // distance2
  output->distance2 = input->distance2;
  // distance3
  output->distance3 = input->distance3;
  // distance4
  output->distance4 = input->distance4;
  // angle1
  output->angle1 = input->angle1;
  // angle2
  output->angle2 = input->angle2;
  // angle3
  output->angle3 = input->angle3;
  // angle4
  output->angle4 = input->angle4;
  return true;
}

signal_msg__msg__SignalDecomposed *
signal_msg__msg__SignalDecomposed__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__SignalDecomposed * msg = (signal_msg__msg__SignalDecomposed *)allocator.allocate(sizeof(signal_msg__msg__SignalDecomposed), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(signal_msg__msg__SignalDecomposed));
  bool success = signal_msg__msg__SignalDecomposed__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
signal_msg__msg__SignalDecomposed__destroy(signal_msg__msg__SignalDecomposed * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    signal_msg__msg__SignalDecomposed__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
signal_msg__msg__SignalDecomposed__Sequence__init(signal_msg__msg__SignalDecomposed__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__SignalDecomposed * data = NULL;

  if (size) {
    data = (signal_msg__msg__SignalDecomposed *)allocator.zero_allocate(size, sizeof(signal_msg__msg__SignalDecomposed), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = signal_msg__msg__SignalDecomposed__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        signal_msg__msg__SignalDecomposed__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
signal_msg__msg__SignalDecomposed__Sequence__fini(signal_msg__msg__SignalDecomposed__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      signal_msg__msg__SignalDecomposed__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

signal_msg__msg__SignalDecomposed__Sequence *
signal_msg__msg__SignalDecomposed__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__SignalDecomposed__Sequence * array = (signal_msg__msg__SignalDecomposed__Sequence *)allocator.allocate(sizeof(signal_msg__msg__SignalDecomposed__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = signal_msg__msg__SignalDecomposed__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
signal_msg__msg__SignalDecomposed__Sequence__destroy(signal_msg__msg__SignalDecomposed__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    signal_msg__msg__SignalDecomposed__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
signal_msg__msg__SignalDecomposed__Sequence__are_equal(const signal_msg__msg__SignalDecomposed__Sequence * lhs, const signal_msg__msg__SignalDecomposed__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!signal_msg__msg__SignalDecomposed__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
signal_msg__msg__SignalDecomposed__Sequence__copy(
  const signal_msg__msg__SignalDecomposed__Sequence * input,
  signal_msg__msg__SignalDecomposed__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(signal_msg__msg__SignalDecomposed);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    signal_msg__msg__SignalDecomposed * data =
      (signal_msg__msg__SignalDecomposed *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!signal_msg__msg__SignalDecomposed__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          signal_msg__msg__SignalDecomposed__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!signal_msg__msg__SignalDecomposed__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
