import atx

d = atx.connect('http://localhost:8100',platform='ios')
d.start_app('com.netease.onmyoji')
d(xpath=u"//TextField").set_text("")
d(xpath=u"//SecureTextField").set_text("11111111")
elem = d(class_name="Button")[0].click();