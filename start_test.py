#!/usr/local/bin/ python
# -*- coding: utf-8 -*-

import atx
import time

driver = atx.connect('http://localhost:8100',platform='ios')
driver.start_app('com.netease.onmyoji')


driver.click_image(u'./images/confirm.1920x1080.png', timeout=5, safe = True)
driver.click(150,150)

driver.click_image(u'./images/cancelAnnouncement.1920x1080.png', timeout=5, safe = True)
time.sleep(10)

driver.click_image(u'./images/login.1920x1080.png', timeout=10, safe = True)

time.sleep(2)
driver.click(150,150)

