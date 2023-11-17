# initialize_test_tree.py
# 根据项目结构自动创建一致的test结构和空的test文件

import os

src_directory = 'app/'  # 你的源代码目录
tests_directory = 'tests/'  # 你的测试代码目录

# 遍历源代码目录
for root, dirs, files in os.walk(src_directory):
    for file in files:
        if file.endswith('.py') and not file.startswith('__init__'):
            # 获取源代码文件的相对路径
            relative_path = os.path.relpath(root, src_directory)
            test_file_directory = os.path.join(tests_directory, relative_path)

            # 确保目标目录存在
            if not os.path.exists(test_file_directory):
                os.makedirs(test_file_directory)

            # 创建一个对应的测试文件
            test_file_path = os.path.join(test_file_directory, 'test_' + file)
            with open(test_file_path, 'w') as f:
                f.write(f"# Tests for {file}\n")
                f.write("\n\n")
                # 你还可以在这里添加一些默认的导入语句或测试模板
