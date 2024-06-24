# 在 example_module.py 文件中定义了 MyClass 类
class MyClass:
    def __init__(self):
        pass

# 在另一个脚本中使用该模块
if __name__ == '__main__':
    # 创建类的实例
    obj = MyClass()

    # 访问 __module__ 属性
    print(obj.__module__)  # 输出: example_module
