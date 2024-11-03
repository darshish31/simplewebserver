from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>LAPTOP CONFIGURATION</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        table {
            border-collapse: collapse;
            margin: auto;
            width: 80%;
            background-color: beige;
        }
        th, td {
            border: 3px solid #333;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #d3d3d3;
        }
    </style>
</head>
<body>
    <h2>LAPTOP CONFIGURATION</h2>
    <table>
        <tr>
            <th>ITEM</th>
            <th>VALUE</th>
        </tr>
        <tr>
            <td>OS Name</td>
            <td>Microsoft Windows 11 Home</td>
        </tr>
        <tr>
            <td>Version</td>
            <td>10.0.22631 Build 22631</td>
        </tr>
        <tr>
            <td>Other OS Description</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>OS Manufacturer</td>
            <td>Microsoft Corporation</td>
        </tr>
        <tr>
            <td>System Name</td>
            <td>DESKTOP-MOHHBTU</td>
        </tr>
        <tr>
            <td>System Manufacturer</td>
            <td>LENOVO</td>
        </tr>
        <tr>
            <td>System Model</td>
            <td>21JQS7VC00</td>
        </tr>
        <tr>
            <td>System Type</td>
            <td>x64-based PC</td>
        </tr>
        <tr>
            <td>System SKU</td>
            <td>LENOVO_MT_21JQQ_BU_Think_FM_ThinkPad E16 Gen1</td>
        </tr>
        <tr>
            <td>Processor</td>
            <td>13th Gen Intel(R) Core(TM) i5-1335U, 1300 Mhz, 10 Core(s),12 Logical processor</td>
        </tr>
        <tr>
            <td>BIOS Version/Date</td>
            <td>LENOVO R2AET57W(1.32),4/25/2024</td>
        </tr>
    </table>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()
