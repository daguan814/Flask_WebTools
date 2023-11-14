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
    .then(response => {
        if (response.ok) {
            console.log('上传成功');
        } else {
            console.error('上传失败');
        }
    })
    .catch(error => console.error('上传失败:', error));
}