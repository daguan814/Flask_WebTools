# Flask_WebTools
使用flask前后端不分离加上python脚本来实现一些日常生活中实用的网页

### 部署方法：

docker(无法获取请求者的ip地址)
部署方法直接根据Dockerfile

##### **直接使用虚拟环境（venv不可以使用，需要重建一个）**

pip freeze > requirements.txt  #打包requirements.txt
然后删除项目中自带的venv
创建一个新的虚拟环境,需要部署的机器上自带python
python -m venv venv

激活虚拟环境
source venv/bin/activate  # macOS 或 Linux 

安装依赖
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

创建计划任务，运行sh脚本,只有进入了虚拟环境才能python
chmod +x run.sh
bash /var/services/homes/shuijing/Flask_Code/Flask_WebTools/run.sh

查看端口占用
netstat -tuln | grep 9000
查看进程id
ps -ef | grep "python app.py"


##### 1.项目设计结构
主体采用MVC架构，将所有业务代码放入MVC文件夹
static用来存放项目的一些文件，包括图片，用户上传的文件
templates模版文件夹用来存放项目的html、css文件等网页文件
app.py用来启动项目，配置项目的config
exps.py用来存放扩展工具
补充：在controller每个里面都使用蓝图，用来分离项目

##### 2.迁移命令
如果flask文件找不到就pip重新安装flask，没有pip python3.10 -m pip install --upgrade pip
切记要在Controller导入from MVC.Dao.UserDao import User，不然就没办法迁移，只能把数据库的东西导出来，不能把代码生成数据库
先要
pip install pymysql
flask db init    
flask db migrate 改变模型后先用这个生成版本，再更改
flask db upgrade
flask db downgrade



