title:GIGABYTE Brix Pro 4570R UEFI安装黑苹果笔记
date:2014-08-03-12-22
---
<h1>起因</h1>

<p>最近入手了个 Brix Pro 4570R. 说实话在入手时我就有安装黑苹果的打算 这货现在可以认为是RMB3800. 免费送配件的钱另算.</p>

<p>我入手是4300 但是京东送了个手柄 4GB低电压内存,</p>

<ul>
<li><p>另外还有一个http://item.jd.com/1109008.html无线模块.这个无线模块咋一看好高大上.理论速度100MB/S,可是.. wifi 是在 mac 下是没有驱动的..</p></li>
<li><p>蓝牙倒是10.9.3下直接免驱.但是经常开机找不到</p></li>
<li><p>这种机器你必须配一个 ssd 才行.要不他的能量得不到发挥.我是使用了他的 msata 口,因为我的 sata 需要接入我之前笔记本的750GB HDD.三星840EVO 600块..真心是很贵了..不过做到了10秒开机,很开心</p></li>
<li><p>内存的话,我提醒一下必须是1.35v的低电压 否则点不亮机器.但是可以插一个1.35v一个1.5v的 这个没有问题.只是每次开机都要按 F1.非常蛋疼..这个BIOS提示应该是无法取消的. 我现在的配置是750GB HDD+120GB SSD+12G 1600 RAM+3.2 Turbo i5.</p></li>
</ul>

<h1>安装</h1>

<p>安装黑苹果现在的主流是 Clover 这个东西需要使用 UEFI 启动.那什么是 UEFI 启动呢?</p>

<p>其实我只用几句话就可以说明白.这个在其他地方好像都没有讲解的.. 就是BIOS搜索所有分区的 efi 文件夹(只是对于技嘉主板而言.技嘉主板甚至支持 NTFS分区下的 EFI.一般主板可能至搜索特定分区).这个文件夹就相当于 liunx 的 +x , windows 的 exe.</p>

<!--more-->

<h2>在装黑苹果的时候,我遇到了一个大坑..安装总是在最后一分钟失败.</h2>

<p>后来先拆掉HDD,只保留 SSD 就安装成功了.这个要注意点..</p>

<p>另外 BIOS 的那个 CPU的最后一个选项必须关闭(忘了叫什么了). 具体的安装可以看这个人的博客. http://eexe1.wordpress.com/2014/04/06/install-os-x-10-9-mavericks-and-window-8-1-in-gigabyte-brix-pro-tutorial/</p>

<ul>
<li><p>跟他不一样的是,我是先装的 win8.装好 mac 后 ,一个必装的是 Parallels Desktop 虚拟机.可以用 Bootcamp 选项 导入已经安装好的同盘 win8.</p></li>
<li><p>也就是说 这个 win8既可以开机启动 也可以在 mac 下虚拟.这个虚拟机的性能如何呢?我在虚拟机下玩古剑奇谭2竟然只比直接启动 win8 少30的 FPS%</p></li>
<li><p>也就是说对于 hd5200来说 在虚拟机下玩win 3D 游戏也是绰绰有余的,非常满意.</p></li>
</ul>
