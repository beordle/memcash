# memcash
一个设想中的理想静态博客生成工具

MemCash

* 使用插件机制
* 每个文章是一个文件夹,内含所有渲染所需(包括图片)
* 无权限管理
* 目录是任意的,文章的标签或者是分类,我认为是要"文章自己定义自己",其父目录与"分类"并无任何联系
* 因为我有好几年的博客 有的时候有一个看什么时候写的需求..这个怎么办呢..或者用command? 貌似是可行的办法
* filter.py 2012 to 2013 

---
根据之前的教训,有一个设想中的内部实现

这个工具可以是静态博客,可以是动态博客
但本质上是动态的,可以有另一个进程去抓取博客,所以能到到静态的效果...
或者本质上是静态的,有一个文件系统监视器?

本身维护一个sqlite memory

两层 一层是和文件系统打交道的  一个是和 server 打交道的?
也许..这样可以写出 plugins... 对 很不错..hook sqlite 语句就好了



