import os
from bs4 import BeautifulSoup
from t02test import PageWork

# cmd = 'adb shell uiautomator dump /sdcard/ui.xml'
# # cmd = 'adb shell uiautomator dump E:/Test/ui.xml'     # 反正就是不能直接写
# os.system(cmd)
# os.system(r'adb pull /sdcard/ui.xml E:\Workplace\Workplace_Python\wp_project\pyGreat\application\ctrlmobile')
# with open('E:/Test/ui.xml', encoding='utf8') as f:
#     # soup = BeautifulSoup(f.read(), 'lxml')
obj = PageWork()
print(obj.content)
# obj.tapNode(attrs={'resource-id':'com.strategyapp:id/tt_video_ad_close_layout'})
# print(obj.getPos('立即领取'))
obj.tapNode(attrs={'class':"android.widget.ImageView"})

