# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_curvefs')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_curvefs')
    _curvefs = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_curvefs', [dirname(__file__)])
        except ImportError:
            import _curvefs
            return _curvefs
        if fp is not None:
            try:
                _mod = imp.load_module('_curvefs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _curvefs = swig_import_helper()
    del swig_import_helper
else:
    import _curvefs
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

CURVE_INODE_DIRECTORY = _curvefs.CURVE_INODE_DIRECTORY
CURVE_INODE_PAGEFILE = _curvefs.CURVE_INODE_PAGEFILE
CURVEINODE_APPENDFILE = _curvefs.CURVEINODE_APPENDFILE
CURVE_INODE_APPENDECFILE = _curvefs.CURVE_INODE_APPENDECFILE
CURVE_ERROR_OK = _curvefs.CURVE_ERROR_OK
CURVE_ERROR_EXISTS = _curvefs.CURVE_ERROR_EXISTS
CURVE_ERROR_FAILED = _curvefs.CURVE_ERROR_FAILED
CURVE_ERROR_DISABLEIO = _curvefs.CURVE_ERROR_DISABLEIO
CURVE_ERROR_AUTHFAIL = _curvefs.CURVE_ERROR_AUTHFAIL
CURVE_ERROR_DELETING = _curvefs.CURVE_ERROR_DELETING
CURVE_ERROR_NOTEXIST = _curvefs.CURVE_ERROR_NOTEXIST
CURVE_ERROR_UNDER_SNAPSHOT = _curvefs.CURVE_ERROR_UNDER_SNAPSHOT
CURVE_ERROR_NOT_UNDERSNAPSHOT = _curvefs.CURVE_ERROR_NOT_UNDERSNAPSHOT
CURVE_ERROR_DELETE_ERROR = _curvefs.CURVE_ERROR_DELETE_ERROR
CURVE_ERROR_NOT_ALLOCATE = _curvefs.CURVE_ERROR_NOT_ALLOCATE
CURVE_ERROR_NOT_SUPPORT = _curvefs.CURVE_ERROR_NOT_SUPPORT
CURVE_ERROR_NOT_EMPTY = _curvefs.CURVE_ERROR_NOT_EMPTY
CURVE_ERROR_NO_SHRINK_BIGGER_FILE = _curvefs.CURVE_ERROR_NO_SHRINK_BIGGER_FILE
CURVE_ERROR_SESSION_NOTEXISTS = _curvefs.CURVE_ERROR_SESSION_NOTEXISTS
CURVE_ERROR_FILE_OCCUPIED = _curvefs.CURVE_ERROR_FILE_OCCUPIED
CURVE_ERROR_PARAM_ERROR = _curvefs.CURVE_ERROR_PARAM_ERROR
CURVE_ERROR_INTERNAL_ERROR = _curvefs.CURVE_ERROR_INTERNAL_ERROR
CURVE_ERROR_CRC_ERROR = _curvefs.CURVE_ERROR_CRC_ERROR
CURVE_ERROR_INVALID_REQUEST = _curvefs.CURVE_ERROR_INVALID_REQUEST
CURVE_ERROR_DISK_FAIL = _curvefs.CURVE_ERROR_DISK_FAIL
CURVE_ERROR_NO_SPACE = _curvefs.CURVE_ERROR_NO_SPACE
CURVE_ERROR_NOT_ALIGNED = _curvefs.CURVE_ERROR_NOT_ALIGNED
CURVE_ERROR_BAD_FD = _curvefs.CURVE_ERROR_BAD_FD
CURVE_ERROR_LENGTH_NOT_SUPPORT = _curvefs.CURVE_ERROR_LENGTH_NOT_SUPPORT
CURVE_ERROR_UNKNOWN = _curvefs.CURVE_ERROR_UNKNOWN
CURVE_OP_READ = _curvefs.CURVE_OP_READ
CURVE_OP_WRITE = _curvefs.CURVE_OP_WRITE
CLUSTERIDMAX = _curvefs.CLUSTERIDMAX
class AioContext_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AioContext_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AioContext_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["offset"] = _curvefs.AioContext_t_offset_set
    __swig_getmethods__["offset"] = _curvefs.AioContext_t_offset_get
    if _newclass:
        offset = _swig_property(_curvefs.AioContext_t_offset_get, _curvefs.AioContext_t_offset_set)
    __swig_setmethods__["length"] = _curvefs.AioContext_t_length_set
    __swig_getmethods__["length"] = _curvefs.AioContext_t_length_get
    if _newclass:
        length = _swig_property(_curvefs.AioContext_t_length_get, _curvefs.AioContext_t_length_set)
    __swig_setmethods__["ret"] = _curvefs.AioContext_t_ret_set
    __swig_getmethods__["ret"] = _curvefs.AioContext_t_ret_get
    if _newclass:
        ret = _swig_property(_curvefs.AioContext_t_ret_get, _curvefs.AioContext_t_ret_set)
    __swig_setmethods__["op"] = _curvefs.AioContext_t_op_set
    __swig_getmethods__["op"] = _curvefs.AioContext_t_op_get
    if _newclass:
        op = _swig_property(_curvefs.AioContext_t_op_get, _curvefs.AioContext_t_op_set)
    __swig_setmethods__["cb"] = _curvefs.AioContext_t_cb_set
    __swig_getmethods__["cb"] = _curvefs.AioContext_t_cb_get
    if _newclass:
        cb = _swig_property(_curvefs.AioContext_t_cb_get, _curvefs.AioContext_t_cb_set)
    __swig_setmethods__["buf"] = _curvefs.AioContext_t_buf_set
    __swig_getmethods__["buf"] = _curvefs.AioContext_t_buf_get
    if _newclass:
        buf = _swig_property(_curvefs.AioContext_t_buf_get, _curvefs.AioContext_t_buf_set)

    def __init__(self):
        this = _curvefs.new_AioContext_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _curvefs.delete_AioContext_t
    __del__ = lambda self: None
AioContext_t_swigregister = _curvefs.AioContext_t_swigregister
AioContext_t_swigregister(AioContext_t)

class UserInfo_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UserInfo_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UserInfo_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["owner"] = _curvefs.UserInfo_t_owner_set
    __swig_getmethods__["owner"] = _curvefs.UserInfo_t_owner_get
    if _newclass:
        owner = _swig_property(_curvefs.UserInfo_t_owner_get, _curvefs.UserInfo_t_owner_set)
    __swig_setmethods__["password"] = _curvefs.UserInfo_t_password_set
    __swig_getmethods__["password"] = _curvefs.UserInfo_t_password_get
    if _newclass:
        password = _swig_property(_curvefs.UserInfo_t_password_get, _curvefs.UserInfo_t_password_set)

    def __init__(self):
        this = _curvefs.new_UserInfo_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _curvefs.delete_UserInfo_t
    __del__ = lambda self: None
UserInfo_t_swigregister = _curvefs.UserInfo_t_swigregister
UserInfo_t_swigregister(UserInfo_t)

class FileInfo_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileInfo_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileInfo_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["id"] = _curvefs.FileInfo_t_id_set
    __swig_getmethods__["id"] = _curvefs.FileInfo_t_id_get
    if _newclass:
        id = _swig_property(_curvefs.FileInfo_t_id_get, _curvefs.FileInfo_t_id_set)
    __swig_setmethods__["parentid"] = _curvefs.FileInfo_t_parentid_set
    __swig_getmethods__["parentid"] = _curvefs.FileInfo_t_parentid_get
    if _newclass:
        parentid = _swig_property(_curvefs.FileInfo_t_parentid_get, _curvefs.FileInfo_t_parentid_set)
    __swig_setmethods__["filetype"] = _curvefs.FileInfo_t_filetype_set
    __swig_getmethods__["filetype"] = _curvefs.FileInfo_t_filetype_get
    if _newclass:
        filetype = _swig_property(_curvefs.FileInfo_t_filetype_get, _curvefs.FileInfo_t_filetype_set)
    __swig_setmethods__["length"] = _curvefs.FileInfo_t_length_set
    __swig_getmethods__["length"] = _curvefs.FileInfo_t_length_get
    if _newclass:
        length = _swig_property(_curvefs.FileInfo_t_length_get, _curvefs.FileInfo_t_length_set)
    __swig_setmethods__["ctime"] = _curvefs.FileInfo_t_ctime_set
    __swig_getmethods__["ctime"] = _curvefs.FileInfo_t_ctime_get
    if _newclass:
        ctime = _swig_property(_curvefs.FileInfo_t_ctime_get, _curvefs.FileInfo_t_ctime_set)
    __swig_setmethods__["filename"] = _curvefs.FileInfo_t_filename_set
    __swig_getmethods__["filename"] = _curvefs.FileInfo_t_filename_get
    if _newclass:
        filename = _swig_property(_curvefs.FileInfo_t_filename_get, _curvefs.FileInfo_t_filename_set)
    __swig_setmethods__["owner"] = _curvefs.FileInfo_t_owner_set
    __swig_getmethods__["owner"] = _curvefs.FileInfo_t_owner_get
    if _newclass:
        owner = _swig_property(_curvefs.FileInfo_t_owner_get, _curvefs.FileInfo_t_owner_set)

    def __init__(self):
        this = _curvefs.new_FileInfo_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _curvefs.delete_FileInfo_t
    __del__ = lambda self: None
FileInfo_t_swigregister = _curvefs.FileInfo_t_swigregister
FileInfo_t_swigregister(FileInfo_t)

class DirInfos_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DirInfos_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DirInfos_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dirpath"] = _curvefs.DirInfos_t_dirpath_set
    __swig_getmethods__["dirpath"] = _curvefs.DirInfos_t_dirpath_get
    if _newclass:
        dirpath = _swig_property(_curvefs.DirInfos_t_dirpath_get, _curvefs.DirInfos_t_dirpath_set)
    __swig_setmethods__["userinfo"] = _curvefs.DirInfos_t_userinfo_set
    __swig_getmethods__["userinfo"] = _curvefs.DirInfos_t_userinfo_get
    if _newclass:
        userinfo = _swig_property(_curvefs.DirInfos_t_userinfo_get, _curvefs.DirInfos_t_userinfo_set)
    __swig_setmethods__["dirsize"] = _curvefs.DirInfos_t_dirsize_set
    __swig_getmethods__["dirsize"] = _curvefs.DirInfos_t_dirsize_get
    if _newclass:
        dirsize = _swig_property(_curvefs.DirInfos_t_dirsize_get, _curvefs.DirInfos_t_dirsize_set)
    __swig_setmethods__["fileinfo"] = _curvefs.DirInfos_t_fileinfo_set
    __swig_getmethods__["fileinfo"] = _curvefs.DirInfos_t_fileinfo_get
    if _newclass:
        fileinfo = _swig_property(_curvefs.DirInfos_t_fileinfo_get, _curvefs.DirInfos_t_fileinfo_set)

    def __init__(self):
        this = _curvefs.new_DirInfos_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _curvefs.delete_DirInfos_t
    __del__ = lambda self: None
DirInfos_t_swigregister = _curvefs.DirInfos_t_swigregister
DirInfos_t_swigregister(DirInfos_t)


def Init(path):
    return _curvefs.Init(path)
Init = _curvefs.Init

def Open4Qemu(filename):
    return _curvefs.Open4Qemu(filename)
Open4Qemu = _curvefs.Open4Qemu

def Open(filename, info):
    return _curvefs.Open(filename, info)
Open = _curvefs.Open

def Create(filename, info, size):
    return _curvefs.Create(filename, info, size)
Create = _curvefs.Create

def Read(fd, buf, offset, length):
    return _curvefs.Read(fd, buf, offset, length)
Read = _curvefs.Read

def Write(fd, buf, offset, length):
    return _curvefs.Write(fd, buf, offset, length)
Write = _curvefs.Write

def AioRead(fd, aioctx):
    return _curvefs.AioRead(fd, aioctx)
AioRead = _curvefs.AioRead

def AioWrite(fd, aioctx):
    return _curvefs.AioWrite(fd, aioctx)
AioWrite = _curvefs.AioWrite

def StatFile4Qemu(filename, finfo):
    return _curvefs.StatFile4Qemu(filename, finfo)
StatFile4Qemu = _curvefs.StatFile4Qemu

def StatFile(filename, info, finfo):
    return _curvefs.StatFile(filename, info, finfo)
StatFile = _curvefs.StatFile

def ChangeOwner(filename, owner, info):
    return _curvefs.ChangeOwner(filename, owner, info)
ChangeOwner = _curvefs.ChangeOwner

def Close(fd):
    return _curvefs.Close(fd)
Close = _curvefs.Close

def Rename(info, oldpath, newpath):
    return _curvefs.Rename(info, oldpath, newpath)
Rename = _curvefs.Rename

def Extend(filename, info, size):
    return _curvefs.Extend(filename, info, size)
Extend = _curvefs.Extend

def Unlink(filename, info):
    return _curvefs.Unlink(filename, info)
Unlink = _curvefs.Unlink

def DeleteForce(filename, info):
    return _curvefs.DeleteForce(filename, info)
DeleteForce = _curvefs.DeleteForce

def Listdir(dirpath, info):
    return _curvefs.Listdir(dirpath, info)
Listdir = _curvefs.Listdir

def Mkdir(dirpath, info):
    return _curvefs.Mkdir(dirpath, info)
Mkdir = _curvefs.Mkdir

def Rmdir(dirpath, info):
    return _curvefs.Rmdir(dirpath, info)
Rmdir = _curvefs.Rmdir

def UnInit():
    return _curvefs.UnInit()
UnInit = _curvefs.UnInit

def GetClusterId(buf=None, len=0):
    return _curvefs.GetClusterId(buf, len)
GetClusterId = _curvefs.GetClusterId
# This file is compatible with both classic and new-style classes.


