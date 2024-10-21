# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# main.py
from submit import submit
from progress import progress
from sync import sync_vivogpt
import time

def main():
    content = sync_vivogpt()
    print(content)
    if content:# 判断是否为空
        task_id = submit(content)  # 调用submit函数并获取任务ID和进度查询URI
    if task_id:
        print(f"Task ID: {task_id}")
        time.sleep(20)  # 等待一段时间，让任务有时间开始处理，时间可根据实际情况调整
        progress(task_id)  # 调用progress函数，传入任务ID和URI

if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
