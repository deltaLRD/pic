import os

strs = []
for file_name in sorted(os.listdir()):
    if (file_name.find('.jpg') is not -1) or (file_name.find('.png') is not -1):
        strs.append('<li><a href="https://delta_lrd.gitee.io/pic/'+file_name+'">'+file_name+'</a></li>\n')
    pass

str_html = \
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>pics bed</title>
</head>
'''
for i in strs:
    str_html  = str_html + i
str_html = str_html + \
'''
</html>
'''
print(str_html)
with open('index.html','w') as file:
    file.write(str_html)