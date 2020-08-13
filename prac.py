# # # # # # # # # from abc import ABC,abstractmethod
# # # # # # # # # class A (ABC):
# # # # # # # # #     @abstractmethod
# # # # # # # # #     def printarea(self):
# # # # # # # # #         return 0
# # # # # # # # # class sub(A):
# # # # # # # # #     def __init__(self):
# # # # # # # # #         self.a=2
# # # # # # # # #         self.b=2
# # # # # # # # #     def printarea(self):
# # # # # # # # #         return self.a + self.b
# # # # # # # # # a = sub()
# # # # # # # # # print(a.printarea())
# # # # # # # # r="Rakesh"
# # # # # # # # f=["Rakesh", "college", "Hello"]
# # # # # # # # for i in f:
# # # # # # # #     if i=="Rakesh":
# # # # # # # #         f.remove(r)
# # # # # # # #     else:
# # # # # # # #         continue
# # # # # # # class A:
# # # # # # #     __a=1


# # # # # # # z=A()
# # # # # # # print(z._A__a)
# # # # # # f1 = open("f4.txt")
# # # # # # if "TO Rakesh ," in f1:
# # # # # #     print("Present")
# # # # # # else :
# # # # # #     print("Not Present")
# # # # # # 'DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode',
# # # # # # 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat',
# # # # # # 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ',
# # # # # # 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']

# # # # # import os

# # # # # # print(dir(os))
# # # # # print(os.getcwd())
# # # # # # print(os.mkdir("rakesh.txt"))
# # # # # print(dir(os.read))
# # # # # # print(os.)





# # # # import argparse
# # # # import sys
# # # a=111
# # # b='221'
# # # print(b[::-1])
# # # print(-151515+152251)

# # a={'rakesh':'rakesh'}
# # a={'rakesh':'rakesh'}
# # a['rocky']='rocky'
# # print(a)
# # z=[]
# # a={1:2, 3:4, 5:6}
# # for k, v in a.items():
# #     z.append(k)
# # print(z)
# a = {'1':'2', '3':'4'}
# print(a(1))
# b = a.get(a[1])
# print(b)

import speech_recognition as sr
r = sr.Recognizer()
print(dir(sr))


