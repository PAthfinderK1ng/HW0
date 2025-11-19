# jvm_check.py
import sys
import jpype as jp

print("Python exe:", sys.executable)
if not jp.isJVMStarted():
    jp.startJVM()  # 脚本里直接启动即可；脚本退出时会随进程结束
print("JVM started:", jp.isJVMStarted())
