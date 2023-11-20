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

function submitDC(event) {
    // 阻止表单默认提交行为
    event.preventDefault();
    // 获取输入的文件名或取件码
    var file_code = document.getElementById("file_code").value;

    // 使用 Fetch API 发送请求
    fetch("/upload/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({file_code: file_code})
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // 在这里处理从后端返回的 JSON 数据
            console.log(data);
            // 可以根据需要执行其他操作，例如更新页面内容
            alert(data.message)
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });


}