import urllib.request

url = "https://mm.taobao.com/search_tstar_model.htm?spm=5679.126488.640745.2.43fb155eqK2Ony";
ph = -1;
temp = '"<img src=""';
# 打开url页面
up = urllib.request.urlopen(url);
# 读取整个html的代码
cont = str(up.read());
head = "<img src";
tail = ".jpg";
# 图片链接
ph = cont.find(head);
pj = cont.find(tail, ph);
img = cont[ph + len(temp):pj + len(tail)];
print(cont[ph + len(temp):pj + len(tail)])
urllib.request.urlretrieve("https://img.alicdn.com/tps/i1/TB1RMh1IFXXXXa7XXXXWp6r0pXX-425-380.png_450x10000q90.jpg", "aa.jpg")
# <img src="//img.alicdn.com/tps/i1/TB1RMh1IFXXXXa7XXXXWp6r0pXX-425-380.png_450x10000q90.jpg" alt="斯方圆">
# 网页链接
ahref = "<a href";
target = "target=\"_blank\" class=\"item-link\"";
mh = cont.find(ahref);
print(mh);
mt = cont.find(target);
print(mt);
print(cont[mh:mt]);
#  target="_blank" class="item-link"
