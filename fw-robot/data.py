import os
import json

print("========请为配置你的邮箱========")
user_email = input("请输入你的网易邮箱：")
user_passwd = input("请输入你的邮箱密码(应为SMTP秘钥)：")
# TODO: 将数据添加到json文件->data.json中
data_dict = {
	'user':{
		'user_email': user_email,
		'user_passwd': user_passwd,
	},
}
data = json.dumps(data_dict)
#print(data)