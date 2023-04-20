
    # Notification(
    #     title="Battery Low",
    #     description=str(percent) + "Battery remains!",
    #     duration=5,
    #     urgency='URGENCY_CRITICAL',
    # ).send()


#https://www.cnblogs.com/mafu/p/15419951.html
#https://pypi.org/project/py-notifier/
#发通知https://blog.csdn.net/qq_51865683/article/details/123314046
#
# import ssl
# import smtplib
#
# from pynotifier import NotificationClient, Notification
# from pynotifier.backends import platform, smtp
#
# smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
#
# c = NotificationClient()
#
# c.register_backend(platform.Backend())
# c.register_backend(smtp.Backend(server=smtp_server,
#                                 name='My Organization',
#                                 email='sender@organization.com',
#                                 password='super_password'))
#
# filenames = [
#   'path/to/file1.json',
#   'path/to/file2.txt',
#   # ...
# ]
#
# attachments = []
# for filename in filenames:
# 	attachments.append(smtp.Attachment(open(filename, 'rb'), filename))
#
# smtp_config = smtp.NotificationConfig(emails=['receiver_1@email.com', 'receiver_2@email.com'],
#                                       attachments=attachments)
# notification = Notification(title='Hello', message='World', smtp=smtp_config)
#
# c.notify_all(notification)

#打包成exe：pyinstaller -F xxx.py
#加-w不带控制台
#Pyinstaller -F -i xx.ico setup.py 打包指定exe图标打包
#设置开机自启动:shell:startup
#设置防火墙信任
import psutil
# import win32api,win32gui
# from pynotifier import Notification
from win10toast import ToastNotifier
from time import sleep

# ct=win32api.GetConsoleTitle()
# hd=win32gui.FindWindow(0,ct)
# win32gui.ShowWindow(hd,0)

TN=ToastNotifier()


battery=psutil.sensors_battery()
# print(battery)
plugged=battery.power_plugged
percent=battery.percent
while True:
    sleep(30)
    if percent < 5 and plugged == False:
        TN.show_toast("电量低", str(percent) + "%请及时充电", icon_path="batterylow.ico", duration=10, threaded=False)
