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