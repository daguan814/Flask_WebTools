
# python环境
FROM python

# 设置工作目录
WORKDIR /app

# 复制应用程序文件到容器中
COPY . /app

# 安装应用程序依赖(清华源)
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 定义启动命令
CMD ["python", "app.py"]
# pip freeze > requirements.txt 打包requirements.txt
# docker build -t my-flask-app .
# docker run -d -p 9000:9000 my-flask-app  后台运行
# docker logs -f <容器名称或ID>    查看日志