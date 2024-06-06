# @Date : 2024/5/27 8:32
# @Author : liming
import webbrowser

print("请选择要打开的网址：")
print("1. 各种官网")
print("2. https://github.com/mx-space/core")
print("3. 同时打开以上两个网址")

choice = input("请输入选择的数字：")
# 官网
if choice == '1':
    webbrowser.open_new_tab('https://cn.vitejs.dev/guide/features.html')
    webbrowser.open_new_tab('https://developer.mozilla.org/zh-CN/')
    webbrowser.open_new_tab('https://www.typescriptlang.org/docs/handbook/intro.html')
    webbrowser.open_new_tab('https://www.tslang.cn/docs/home.html')
    webbrowser.open_new_tab('https://www.naiveui.com/zh-CN/light/docs/installation')
    webbrowser.open_new_tab('https://router.vuejs.org/zh/introduction.html')
    webbrowser.open_new_tab('https://cn.bing.com/search?q=parallax%e7%bf%bb%e8%af%91&qs=SC&pq=parallaxfanyi+&sc=1-14&cvid=FD87AEC9E0B04AD79638ED6B8DF318FF&FORM=QBRE&sp=1&lq=0')
    webbrowser.open_new_tab('https://cn.vuejs.org/guide/introduction.html')
    webbrowser.open_new_tab('https://www.tailwindcss.cn/docs/installation')
    webbrowser.open_new_tab('https://typescript.p6p.net/typescript-tutorial/tsconfig.json.html')
    webbrowser.open_new_tab('')
    webbrowser.open_new_tab('')
    webbrowser.open_new_tab('')
    webbrowser.open_new_tab('')
    webbrowser.open_new_tab('')
# 个人博客
elif choice == '2':
    webbrowser.open_new_tab('https://yiyan.baidu.com/')
    webbrowser.open_new_tab('')
elif choice == '3':
    webbrowser.open_new_tab('https://github.com/mx-space/core')
    webbrowser.open_new_tab('https://github.com/Innei/Shiro')
    webbrowser.open_new_tab('https://mx-space.js.org/docs')
else:
    print("无效的选择，请输入1，2或3。")
