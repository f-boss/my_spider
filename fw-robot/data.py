import os
import json

print("==============请为配置你的邮箱=============")
user_name = input("请输入你的名字: ")
user_email = input("请输入你的网易邮箱：")
user_passwd = input("请输入你的邮箱密码(应为SMTP秘钥)：")
receivers = input("请输入接受者的邮件(多个用户请使用逗号隔开):\n")
receivers = receivers.split(",")
# TODO: 将数据添加到json文件->data.json中
data_dict = {
    'user':{
	'user_name': user_name,
	'user_email': user_email,
	'user_passwd': user_passwd,
	},
    'receivers': receivers,
}
with open('./data.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False)
