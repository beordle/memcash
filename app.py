#!/usr/bin/env xcrun python
# coding:utf-8
from mapper import Sandbox,Sandboxs

from flask import *
from pyquery import PyQuery as pq
app = Flask(__name__)
# i'm aimly
#@cache
# 原則
# 這個項目叫 Aimly, 所以以實現的美觀為前提
# 所有緩存都是使用裝飾器實現的
# 图片将是无损的,保留任何可能的积极
# zip压缩占用空间极少,装饰器可随时去除
# 页面也同时有生存期比较长的缓存
# 流式发布
# 無版本控制(認為任何改動都是你自己意願的結果)
# search_for('person','name',1)
# search_for('group','name'.2)
# 通過用戶名和文章名稱找到melting pot中對應的文件.
# melting pot結構

# hash
# person/hash

# hashval
# hashval.extkkk

# hashval


# 存儲後端是扁平化的
# 流式輸出 團隊視圖 團隊流
# 個人視圖 個人流

@app.route('/favicon.ico')
def favicon():
    return ""


@app.route('/')
def index():
    pageindex = int(request.args.get('p', '1')) - 1
    num=10
    all_posts=Sandboxs(path='src').all().values()
    #all_posts.sort(Sandboxs.sort)
    posts=all_posts[pageindex * 10:pageindex * 10 + 10]
    has_more= pageindex * 10+10 < len(all_posts)
    _=request.headers.get('X-Pjax-Container')
    html=render_template('category.html', **locals())
    if _:
        return  pq(html)("#main").html()
     
    return html

@app.route('/about')
def about():

    return render_template('about.html', **locals())

@app.route('/<string:key>')
def singlepage(key):
    # assert date pass
    sandbox = Sandboxs(path='src').all()[key]
    html=render_template('single.html', **locals())
    _=request.headers.get('X-Pjax-Container')
    if _:
        return  pq(html)("#main").html()
     
    return html


app.run(port=8800, debug=True)

