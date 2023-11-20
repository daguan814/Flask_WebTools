function login() {
    // 获取用户名和密码
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // 构建要发送的 JSON 数据
    var data = {
        username: username,
        password: password
    };

    // 定义请求的URL
    var baseUrl = window.location.origin; // 获取当前页面的域名部分
    var relativeUrl = '/flashTrans/login'; // 相对路径
    var url = baseUrl + relativeUrl; // 构建完整的请求 URL

// 定义请求的配置
    var requestOptions = {
        method: 'POST', // 指定请求方法为POST
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json' // 添加 Accept 头部
        },
        body: JSON.stringify(data)
    };

// 使用fetch函数发起POST请求
    fetch(url, requestOptions)
        .then(function (response) {
            // 检查响应是否成功
            if (!response.ok) {
                return response.json().then(function (data) {
                    alert(data.message);
                    throw new Error('请求出错，状态码为 ' + response.status);
                });
            }

            // 将响应转换为JSON格式
            return response.json();
        })
        .then(function (data) {
            // 处理JSON格式的响应数据
            alert(data.message);
            console.log(data);
            window.location.href = baseUrl + '/flashTrans';
        })
        .catch(function (error) {
            // 处理错误
            alert('发生错误: ' + error.message);
            console.error('发生错误:', error);
        });


}
