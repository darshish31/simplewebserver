# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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

```



## OUTPUT:
![Screenshot 2024-11-03 115911](https://github.com/user-attachments/assets/d49a368d-4fe4-459f-8b58-77a6da9d2211)
![Screenshot 2024-11-03 115946](https://github.com/user-attachments/assets/53c956c9-7120-448d-93e2-183718f9e28b)

## RESULT:
The program for implementing simple webserver is executed successfully.
