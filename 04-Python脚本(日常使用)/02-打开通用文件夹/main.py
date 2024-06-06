import os

# 定义文件夹路径字典
folders = {
    # Shrio
    "1": [
        r"D:\02-code-github\20-PersonalWebsite\PersonalWebsite\02-参考代码\05-2024\Shiro主题",
        r"D:\02-code-github\20-PersonalWebsite\PersonalWebsite\03-code\02-new\项目笔记",
    ],
    # 简书
    "2": [
        r"D:\01-file\04-简书图片待上传\简书图片\Pictures\简书",
        r"D:\01-file\00-自我完善\自我完善.xlsx"
    ],
    # 数据结构PAT
    "3": [
        r"D:\02-code-github\13-LearnDatastructureAndAlgorithms\LearnDatastructureAndAlgorithms\03-PAT",
    ],
    # 你不知道的JS
    "4": [
        r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\01-原生JS\06-你不知道的JS书上代码学习",
        r"D:\08-book\之前电脑\01-前端书籍\你不知道的JavaScript（中卷).pdf",
    ],
    # TS
    "5": [
        r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\08-TypeScript",
        r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\08-TypeScript\TypeScript笔记.md",
        r"D:\02-code-github\05-LearnJavaScript\LearnJavaScript\08-TypeScript\09-千峰教育(好)\01-课程资料\课程笔记\TypeScript学习指南-学习笔记V1.0.pdf",
    ],
    # 设计模式
    "6": [
        r"D:\02-code-github\29-LearnDesignPatterns\LearnDesignPatterns\01-前端设计模式",
        r"D:\02-code-github\29-LearnDesignPatterns\LearnDesignPatterns\01-前端设计模式\JavaScript设计模式(国内).pdf",
    ],
    # Node
    "7": [
        r"D:\08-book\之前电脑\01-前端书籍\深入浅出Node.js.pdf",
        r"D:\02-code-github\32-LearnNode\LearnNode\01-Node学习笔记(黑马笔记不在这里)",
    ],
}

def open_folders(activities):
    # 遍历活动列表
    for activity in activities:
        try:
            # 获取与当前活动相关的文件夹列表
            activity_folders = folders.get(activity)
            if activity_folders:
                # 遍历文件夹列表，打开每个文件夹
                for folder in activity_folders:
                    os.startfile(folder)
        except KeyError:
            print(f"无效的活动：{activity}")

# 获取用户的输入
user_input = input("请输入你的选择（1-shiro,2-简书,3:-PAT,4:你不知JS和设计模式,5:TS）：")

# 根据用户的输入打开相应的文件夹
open_folders(user_input.split(","))
