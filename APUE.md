## UNIX 标准及实现

### 背景

虽然 UNIX 程序在不同的 UNIX 系统之间移植很容易，但是 80 年代以来 UNIX 版本种类剧增以及他们之间的差距的扩大，将 UNIX 标准化的呼声越来越大。

## UNIX 标准化

1. ISO C
   由 ISO/IEC 的 C 程序设计语言国际标准工作组开发和维护。ISO C 的标准意图提供 C 程序的可移植化，使其能适合于大量不同的操作系统，而不只是适合 UNIX 系统，此标准不仅定义了 C 程序设计语言的语法和语义，还定义了其标准库。

2. IEEE POSIX
   由[IEEE](https://en.wikipedia.org/wiki/Institute_of_Electrical_and_Electronics_Engineers)主导，该标准的目的是提升应用程序在各种 UNIX 系统之间的可移植性。它定义了**符合 POSIX 的**操作系统所必需提供的各种服务。该标准已经被很多计算机制造商采用。虽然该标准以 UNIX 为基础，但是它不仅限于 UNIX 和 UNIX 类的系统。
   该标准说明了一套接口而不是实现，所以并不区分系统调用和库函数，所有在标准中的例程都被称为函数。
   POSIX1.1 现在由 Austin Group 开放工作组维护。

3. Single UNIX Specification
   SUS 是 POSIX1.1 的一个超集，它定义了一组附加接口扩展 POSIX1.1 规范提供的功能。SUS 是 Open Group 的出版物，而 Open Group 是由两个工业社团 X/Open 和开发系统软件基金会在 1996 年合并构成的。而且 Open Group 拥有 UNXI 商标，他们使用 SUS 定义了一系列接口。一个系统想要被称为 UNIX 系统必须实现这些接口。UNIX 系统提供商必须以文件形式提供符合行生命，并且通过验证，才能获得使用 UNIX 商标的许可证。

4. FIPS
   FIPS 代表联邦信息处理标准（Federal Information Processing Standard），由美国政府发布，并由美国政府用于计算机系统的采购。该标准基于 IEEE 和 ASNI C 标准草案。部分在 POSIX 中的可选实现，在该标准中是必选。

## UNIX 系统实现

上述列举了几个不同的 UNIX 标准，标准需要有具体的实现与现实世界关联。UNIX 的各版本都起源于 PDP-11 系统上运行的 UNIX 分时系统，并从上演化出三个分支：

- AT&T，由此引出了系统 III 和系统 V
- BSD 分支，由此引出 4.xBSD 实现
- 由 AT&T 不断开发的 UNIX 研究版本，由此引出的 UNIX 分时系统第 8，9，10 版。

1. SVR4
   SVR4(UNIX System V Release 4)是 AT&T 的 UNIX 系统实验室的产品，符合 POSIX1003.1 和 X/Open XPG3 标准。

2. 4.4BSD
   由加州伯克利的计算机系统研究组开发和分发。最初的 BSD 包含 AT&T 的商用代码，后来被逐渐去除。最早机遇 PDP-11 开发，后来移植到 VAX 小型机上，接着转移到工作站，在 20 世纪 90 年代伯克利在 80386 上开发 BSD 版本，产生了 386BSD。

3. FreeBSD
   基于 BSD4.4-Lite，在加州伯克利的 CSRG 种植其在 UNIX 的 BSD 版本研发工作，而 386BSD 又被搁置了很久之后，为了继续 BSD 的开发形成了 FreeBSD 项目。类似的项目还有更重视可移植性 NetBSD 和更注重安全的 OpenBSD。

4. Linux
   Linux 是一种提供类似于 UNIX 的丰富编程环境的系统。在 GPL 的指导下，Linux 是免费使用的。

5. Mac OS X
   其核心操作系统为 Darwin，基于 Mach 内核、FreeBSD 操作系统以及具有面向对象框架的驱动和其他内核扩展的结合。Max OS X 10.5 的 Intel 部分被验证为是一个 UNIX 系统。

6. Solaris
   由 SUN 开发的 UNIX 版本。基于 SRV4，是唯一商业成功的 SRV4 后裔，并被认证成为 UNIX 系统。

7. Others

- AIX，IBM 版本的 UNIX
- HP-UX，HP 版本的 UNIX
- IRIX，Silicon Graphics 版的 UNIX
- UnixWare，SVR4 派生的 UNIX

## 标准和实现的关系

标准定了任一世纪系统的子集。一个特定实现的功能有些是 UNIX 系统必须的，但是在 POSIX 中是可选的。

## 限制

1. 编译时限制
2. 与文件或目录无关的运行时限制
3. 与文件或目录有关的运行时限制

#### ISO C 限制

ISO C 定义的限制都列在头文件<limits.h>中。这些限制在一个给定系统中不会改变。

#### POSIX 限制

- 数值限制：LONG_BIT，SSIZE_MAX，WORD_BIT
- 最小值
- 最大值：\_POSIX_CLOCKRES_MIN
- 运行时可以增加的值：CHARCLASS_NAME_MAX，COLL_WEIGHTS_MAX，LINE_MAX，NGROUPS_MAX，RE_DUP_MAX
- 运行时不变值
- 路径名可变值
- 这些限制和常量，有些在<limits.h>中，其余则按照具体条件定义。

#### XSI 限制

- 最小值
- 运行时不变值

#### sysconf, pathconf,fpathconf

运行时限制与文件或目录有关，所以可以通过上述函数来获得。
