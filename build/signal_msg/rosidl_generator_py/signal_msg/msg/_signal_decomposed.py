# generated from rosidl_generator_py/resource/_idl.py.em
# with input from signal_msg:msg/SignalDecomposed.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SignalDecomposed(type):
    """Metaclass of message 'SignalDecomposed'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('signal_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'signal_msg.msg.SignalDecomposed')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__signal_decomposed
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__signal_decomposed
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__signal_decomposed
            cls._TYPE_SUPPORT = module.type_support_msg__msg__signal_decomposed
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__signal_decomposed

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SignalDecomposed(metaclass=Metaclass_SignalDecomposed):
    """Message class 'SignalDecomposed'."""

    __slots__ = [
        '_path',
        '_distance1',
        '_distance2',
        '_distance3',
        '_distance4',
        '_angle1',
        '_angle2',
        '_angle3',
        '_angle4',
    ]

    _fields_and_field_types = {
        'path': 'int32',
        'distance1': 'float',
        'distance2': 'float',
        'distance3': 'float',
        'distance4': 'float',
        'angle1': 'float',
        'angle2': 'float',
        'angle3': 'float',
        'angle4': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.path = kwargs.get('path', int())
        self.distance1 = kwargs.get('distance1', float())
        self.distance2 = kwargs.get('distance2', float())
        self.distance3 = kwargs.get('distance3', float())
        self.distance4 = kwargs.get('distance4', float())
        self.angle1 = kwargs.get('angle1', float())
        self.angle2 = kwargs.get('angle2', float())
        self.angle3 = kwargs.get('angle3', float())
        self.angle4 = kwargs.get('angle4', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.path != other.path:
            return False
        if self.distance1 != other.distance1:
            return False
        if self.distance2 != other.distance2:
            return False
        if self.distance3 != other.distance3:
            return False
        if self.distance4 != other.distance4:
            return False
        if self.angle1 != other.angle1:
            return False
        if self.angle2 != other.angle2:
            return False
        if self.angle3 != other.angle3:
            return False
        if self.angle4 != other.angle4:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def path(self):
        """Message field 'path'."""
        return self._path

    @path.setter
    def path(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'path' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'path' field must be an integer in [-2147483648, 2147483647]"
        self._path = value

    @builtins.property
    def distance1(self):
        """Message field 'distance1'."""
        return self._distance1

    @distance1.setter
    def distance1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance1' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'distance1' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._distance1 = value

    @builtins.property
    def distance2(self):
        """Message field 'distance2'."""
        return self._distance2

    @distance2.setter
    def distance2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance2' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'distance2' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._distance2 = value

    @builtins.property
    def distance3(self):
        """Message field 'distance3'."""
        return self._distance3

    @distance3.setter
    def distance3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance3' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'distance3' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._distance3 = value

    @builtins.property
    def distance4(self):
        """Message field 'distance4'."""
        return self._distance4

    @distance4.setter
    def distance4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance4' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'distance4' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._distance4 = value

    @builtins.property
    def angle1(self):
        """Message field 'angle1'."""
        return self._angle1

    @angle1.setter
    def angle1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angle1' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angle1' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angle1 = value

    @builtins.property
    def angle2(self):
        """Message field 'angle2'."""
        return self._angle2

    @angle2.setter
    def angle2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angle2' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angle2' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angle2 = value

    @builtins.property
    def angle3(self):
        """Message field 'angle3'."""
        return self._angle3

    @angle3.setter
    def angle3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angle3' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angle3' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angle3 = value

    @builtins.property
    def angle4(self):
        """Message field 'angle4'."""
        return self._angle4

    @angle4.setter
    def angle4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angle4' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angle4' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angle4 = value
