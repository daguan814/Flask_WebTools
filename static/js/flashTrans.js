function uploadFile() {
    var input = document.getElementById('fileInput');

    // 检查是否选择了文件
    if (!input.files || input.files.length === 0) {
        alert('请选择文件');
        return;
    }

    // 创建 FormData 对象
    var formData = new FormData(document.getElementById('uploadForm'));

    // 发送请求
    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
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
        }).then(function (data) {
        // 处理JSON格式的响应数据
        if (data.status === 200) {
            alert(data.message);
        }

    })
        .catch(error => console.error('上传失败:', error));
}