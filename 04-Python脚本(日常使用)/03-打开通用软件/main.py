# @Date : 2024/5/24 15:23
# @Author : liming

import subprocess
import time
# 定义WebStorm的路径和项目的路径
webstorm_path = r"D:\sortware\05-webstorm2023\WebStorm 2023.3.3\bin\webstorm64.exe"

# 定义文件夹路径字典
folders = {
    "1": {
        "path": r"D:\02-code-github\20-PersonalWebsite\PersonalWebsite\02-参考代码\05-2024\Shiro主题\core",
        "command": "pnpm run dev"
    },
    "2": {
        "path": r"D:\02-code-github\20-PersonalWebsite\PersonalWebsite\02-参考代码\05-2024\Shiro主题\mx-admin",
        "command": "pnpm run dev"
    },
    "3": {
        "path": r"D:\02-code-github\20-PersonalWebsite\PersonalWebsite\02-参考代码\05-2024\Shiro主题\Shiro",
        "command": "pnpm i"
    },
    # 设计模式
    "4": {
        "path": r"D:\02-code-github\29-LearnDesignPatterns\LearnDesignPatterns\01-前端设计模式\01-《JavaScript设计模式》-张容铭-书上代码手敲",
    },
    # TS
    "5": {
        "path": r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\08-TypeScript\09-千峰教育(好)",
    },
    # 你不知道的JS
    "6": {
        "path": r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\01-原生JS\06-你不知道的JS书上代码学习\02-全三册\02-中册",
    },

}

def open_folders(activities):
    # 遍历活动列表
    for activity in activities:
        try:
            # 获取与当前活动相关的文件夹列表
            activity_folder = folders.get(activity)
            if activity_folder:
                # 打开文件夹
                subprocess.Popen([webstorm_path, activity_folder["path"]])
                # 在文件夹中执行命令——有问题，执行不了，暂时注释掉
                # subprocess.Popen(activity_folder["command"], cwd=activity_folder["path"], shell=True)
                # 添加一个较长的延迟，以确保WebStorm已经打开
                time.sleep(10)
        except KeyError:
            print(f"无效的活动：{activity}")

# 获取用户的输入
user_input = input("学习shiro,打开文件夹，请输入你的选择：1-core,2-mx-admin,3-shiro,4-设计模式，5-TS-----多个选择用逗号隔开：")

# 根据用户的输入打开相应的文件夹
open_folders(user_input.split(","))