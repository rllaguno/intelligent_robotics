// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from signal_msg:msg/SignalDecomposed.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "signal_msg/msg/detail/signal_decomposed__struct.h"
#include "signal_msg/msg/detail/signal_decomposed__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool signal_msg__msg__signal_decomposed__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[51];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("signal_msg.msg._signal_decomposed.SignalDecomposed", full_classname_dest, 50) == 0);
  }
  signal_msg__msg__SignalDecomposed * ros_message = _ros_message;
  {  // path
    PyObject * field = PyObject_GetAttrString(_pymsg, "path");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->path = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // distance1
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance1 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // distance2
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance2 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // distance3
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance3 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // distance4
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance4 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angle1
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angle1 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angle2
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angle2 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angle3
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angle3 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angle4
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angle4 = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * signal_msg__msg__signal_decomposed__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SignalDecomposed */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("signal_msg.msg._signal_decomposed");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SignalDecomposed");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  signal_msg__msg__SignalDecomposed * ros_message = (signal_msg__msg__SignalDecomposed *)raw_ros_message;
  {  // path
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->path);
    {
      int rc = PyObject_SetAttrString(_pymessage, "path", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angle1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angle2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angle3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angle4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
