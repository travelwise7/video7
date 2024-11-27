from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phone Camera Stream</title>
</head>
<body>
    <h1>Phone Camera Stream</h1>
    <video id="camera" autoplay playsinline style="width: 100%; max-width: 600px;"></video>

    <script>
        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                const video = document.getElementById('camera');
                video.srcObject = stream;
            } catch (err) {
                alert('Error accessing the camera: ' + err.message);
            }
        }
        startCamera();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
