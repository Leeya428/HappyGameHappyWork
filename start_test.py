#!/usr/local/bin/ python
# -*- coding: utf-8 -*-

import atx
import time
import os

driver = atx.connect('http://localhost:8100',platform='ios')
driver.start_app('com.netease.onmyoji')

driver.image_path = ['.', './images']

driver.click_image('./images/confirm.1920x1080.png', timeout=5, safe = True)
driver.click(150,150)

driver.click_image(u'cancelAnnouncement.1920x1080.png', timeout=5, safe = True)

time.sleep(10)
driver.click_image(u'login.1920x1080.png', timeout=5, safe = True)

time.sleep(2)
driver.click(150,150)

print ("已进入庭院")

driver.click_image(u'explore.1920x1080.png', timeout=10, safe = True)
print ("进入探索界面")

#####################御魂##########################

x, y = driver.match('./images/myself.1920x1080.png')
x1, y1 = driver.match('./images/miwen.1920x1080.png')

driver.swipe(x,y,x1,y1,1.0)
driver.click_image(u'./images/yuhun.1920x1080.png', timeout=5, safe = True)

#
# #####################探索##########################
# # 定义一下章节和图片名字
# Level = 12
# image_name = './images/Level' + str(Level) + '.1920x1080.png'
#
#
# # 获取屏幕坐标
# screen_width, screen_length = sorted(driver.display)
#
# driver.keep_screen();
#
# x, y = driver.match('./images/find_monster.1920x1080.png', offset=(0, 1))[0]
# exploreList_top = (x,y)
# exploreList_botton = (x, y + 4 * (screen_length - x))  #list的最后一个离屏幕底还有大概一个宽度的距离。。就减去x吧
# driver.free_screen();
#
#
#
