import atx

driver = atx.connect('http://localhost:8100',platform='ios')

driver.start_app('com.netease.onmyoji')