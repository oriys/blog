# Git Pro V2 Note

## Git 基础

安装 git

```bash
#centos
sudo yum install git

#debian
sudo apt install git

#archlinux
sudo pcaman -S git
```

配置用户名，邮箱和编辑器

```bash
#全局
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor emacs

#系统级别
git config --system user.name "John Doe"
git config --system user.email johndoe@example.com
git config --system core.editor emacs

#项目级别
git config user.name "John Doe"
git config user.email johndoe@example.com
git config core.editor emacs
```

查看配置信息

```bash
#全部配置
git config --list

#某一项配置
git config x.y
```

初始化 git 仓库

```bash
git init
```

把文件加入暂存区

```bash
git add filename
```

提交到版本库

```bash
git commit -m "commit message"
```

克隆仓库

```bash
git clone https://github.com/libgit2/libgit2
```

检查当前文件状态

```bash
git status
```

.ignore 规范

```bash
￼# no .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
￼
```

查看修改

```bash
#未暂存部分修改
git diff

#已暂存部分修改
git diff --stage
```

移除文件

```bash
#从仓库和本地删除文件
git rm filename

#仅仅从仓库删除
git rm filename --cache
```

移动和重命名文件

```bash
git mv file_from file_to
git mv old_name new_name
```

查看提交历史

```bash
#查看详细历史
git log

#查看差异
git log -p

#查看近两次差异
git log -p -2

#查看简短日志
git log --stat

#单行显示日志
git log --pretty=oneline

#格式化日志
git log --pretty=format:"%h - %an, %ar : %s"

#ASCII字符显示分支合并历史
git log --graph

#限制日志范围
git log --pretty="%h - %s" --since="2008-10-01"  --before="2008-11-01" --no-merges

#搜索特定关键字提交
git log -Skeywork
```

修改上次 commit

```bash
git commit --amend
```

取消文件暂存

```bash
git reset HEAD filename
```

撤销对文件的修改

```bash
git checkout -- filename
```
