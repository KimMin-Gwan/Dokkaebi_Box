# Python 3.x
import http.server
import socketserver

# 포트 번호 설정
port = 8000

# 웹 서버 실행
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), Handler) as httpd:
    print("서버는 포트", port, "에서 실행 중...")
    httpd.serve_forever()
    