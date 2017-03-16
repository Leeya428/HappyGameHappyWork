#!/usr/local/bin/ python
# -*- coding: utf-8 -*-

import atx

driver = atx.connect('http://localhost:8100',platform='ios')
sid = str(driver.start_app('com.netease.onmyoji'))
fl = open('session_id_ios', 'wb')
fl.write(sid[16:52])
fl.close()
print("session id 已记录")

driver.click_image('confirm.1920x1080.png', timeout=8, safe = True)