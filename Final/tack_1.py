import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

yandex_disk_token = input("Enter your Yandex Disk OAuth token: ").strip()


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FileServerHandler)
    print("Server started at http://localhost:8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


def get_uploaded_files():
    headers = {
        "Authorization": f"OAuth {yandex_disk_token}"
    }
    url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    params = {
        "limit": 100
    }

    all_files = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            all_files.extend(data.get("items", []))
            url = data.get("_links", {}).get("next", None)
        else:
            print(f"Error: {response.status_code}, {response.text}")
            break

    return all_files


class FileServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            uploaded_files = get_uploaded_files()
            file_names = {file["name"] for file in uploaded_files}

            html_content = "<html><head><title>Uploaded Files</title></head><body>"
            html_content += "<h1>Uploaded Files</h1><ul>"

            local_files = ["file1.txt", "file2.txt", "file3.txt"]

            for file in local_files:
                if file in file_names:
                    html_content += f'<li style="background-color: rgba(200, 200, 0, 0.25);">{file}</li>'
                else:
                    html_content += f'<li>{file}</li>'

            html_content += "</ul></body></html>"

            self.wfile.write(html_content.encode())
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    run()
