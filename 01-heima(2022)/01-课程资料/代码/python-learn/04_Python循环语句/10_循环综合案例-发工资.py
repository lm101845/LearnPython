age = int(input("请输入您的年龄："))
if age >= 18:
    if age < 30:
        print("年龄满足继续判断")
        if int(input("请输入您入职已有多少年：")) > 2:
            print("年龄符合且入职超过2年，满足条件，可以领取")
            exit()
        else:
            print("入职时间不满足继续判断")
        if int(input("请输入您的职位级别：")) > 3:
            print("年龄符合且级别超过3级，满足条件，可以领取")
        else:
            print("不好意思，您不满足领取条件")
    else:
        print("不好意思，年龄大于30岁，不满足领取条件。")
else:
    print("不好意思，年龄小于18岁，不满足领取条件。")