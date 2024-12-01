import socket
import urllib.parse
import html

PORT_NUMBER = 5698
image_list_1 = ["peers", "peer to peer", "p2p", "peer", "peers to peers", "/photos/p2p.jpg", "peer-to-peer communication", "peer-to-peer file sharing", "p2p file sharing", "p2p network images", "distributed networks", "peer-based communication", "decentralized systems", "p2p system architecture", "/photos/p2p_network.png", "./photos/p2p_diagram.jpg" ,"./photos/p2p.jpg"]
image_list_1_ar=[
"النظير" ,"النظير لنظير","النظير النظير","النظير الى النظير", "النظائر","النظير للنظير","النظراء" ,"./photos/p2p.jpg"]
video_list_1 = [

    "peers", "peer to peer", "p2p", "peer", "peers to peers", "what is peer",
    "what is p2p", "what is peer to peer", "./Videos/What_Is_p2p.mp4",
    "introduction to p2p", "what is a p2p network", "p2p explained", "peer-to-peer basics",
    "p2p file sharing tutorial", "p2p networking overview", "how to use p2p",
    "applications of peer-to-peer", "understanding peer-based systems",
    "./Videos/What_Is_p2p.mp4"]
video_list_1_ar=[  "النظير" ,
    "الأقران", "من نظير إلى نظير", "بي تو بي", "نظير", "الأقران إلى الأقران", "ما هو النظير",
    "ما هو بي تو بي", "ما هو من نظير إلى نظير",
    "مقدمة إلى بي تو بي", "ما هو شبكة بي تو بي", "شرح بي تو بي", "أساسيات نظير إلى نظير",
    "دورة تبادل الملفات بي تو بي", "نظرة عامة على الشبكات من نظير إلى نظير", "كيفية استخدام بي تو بي",
    "تطبيقات الشبكات من نظير إلى نظير", "فهم الأنظمة المعتمدة على الأقران",
    "./فيديوهات/ما_هو_بي_تو_بي.mp4",
    "النظير للنظير", "النظير لنظير", "النظير إلى نظير",
    "./Videos/What_Is_p2p.mp4"
]
video_list_2 = ["how p2p work", "how p2p works", "how peer to peer work", "how peer to peer works", "./Videos/How_peer_to_peer_works.mp4", "peer-to-peer working principles", "p2p system operation", "how p2p networks function", "explaining peer-to-peer functionality", "distributed network operations", "real-world examples of p2p", "peer-to-peer communication protocol", "how p2p file sharing works", "how decentralized networks operate", "peer-based data exchange", "./Videos/How_peer_to_peer_works.mp4"]
video_list_2_ar = [
    "كيف تعمل الشبكات النظير للنظير",
    "كيفية عمل الشبكات النظير للنظير",
    "شرح طريقة عمل الشبكات الند للند",
    "مبادئ عمل شبكات الند للند",
    "./Videos/How_peer_to_peer_works.mp4",
    "كيفية تشغيل أنظمة الند للند",
    "طريقة عمل شبكات p2p",
    "شرح تشغيل الشبكات اللامركزية",
    "وظائف الشبكات الموزعة",
    "أمثلة عملية على الشبكات النظير للنظير",
    "بروتوكول الاتصال بين الند للند",
    "كيف تعمل مشاركة الملفات عبر P2P",
    "كيفية تشغيل الشبكات اللامركزية",
    "تبادل البيانات بين النظير للنظير",
    "./Videos/How_peer_to_peer_works.mp4"

]
# if the request method was "GET"
def get_request(client_socket, requested_path):
    if requested_path == "/" or requested_path == "/index.html" or requested_path == "/en" or requested_path =="/main_en.html": # if in current path
        try:
            with open("main_en.html", "r") as html_file:
                html_data = html_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += f"Content-Length: {len(html_data)}\r\n"
            response += "\r\n"
            response += html_data
            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")

        except FileNotFoundError: # if html file not found
            response = "HTTP/1.1 404 Not Found\r\n\r\nHTML file not found."
            client_socket.sendall(response.encode())
    elif requested_path == "/ar" or requested_path =="/main_ar.html":
        try:
            with open("main_ar.html", "r", encoding="utf-8") as html_file:
                html_data = html_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html; charset=utf-8\r\n"
            response += f"Content-Length: {len(html_data.encode('utf-8'))}\r\n"
            response += "\r\n"
            response += html_data
            try:
                client_socket.sendall(response.encode("utf-8"))
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")


        except FileNotFoundError:  # if html file not found
            response = "HTTP/1.1 404 Not Found\r\n\r\nHTML file not found."
            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")
    elif requested_path.endswith(".css"):  # If the request was CSS file
        try:
            with open(requested_path.split("/")[1], "r") as css_file:
                css_data = css_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/css\r\n"
            response += f"Content-Length: {len(css_data)}\r\n"
            response += "\r\n"
            response += css_data

            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")


        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\n\r\nCSS file not found."
            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")


    elif requested_path.endswith(".png") or requested_path.endswith(".jpg"):  # if the request was image (jpg, png)
        try:
            file_name = requested_path.lstrip("/")
            with open(file_name, "rb") as image_file:
                image_data = image_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: image/jpeg\r\n"
            response += f"Content-Length: {len(image_data)}\r\n"
            response += "\r\n"

            try:
                client_socket.sendall(response.encode())
                client_socket.sendall(image_data)
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")


        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\n\r\nImage file not found."

            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")

    elif requested_path.endswith(".mp4"): # if The requested file was Video
        try:
            file_name = requested_path.lstrip("/")
            with open(file_name, "rb") as video_file:
                video_data = video_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: video/mp4\r\n"
            response += f"Content-Length: {len(video_data)}\r\n"
            response += "\r\n"
            try:
                client_socket.sendall(response.encode())
                client_socket.sendall(video_data)
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")

        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\n\r\nImage file not found."
            client_socket.sendall(response.encode())

    elif requested_path.endswith("supporting_material_ar.html"):
        file_name = requested_path.lstrip("/")
        with open("supporting_material_ar.html", "r", encoding="utf-8") as html_file:
            html_data = html_file.read()

        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=utf-8\r\n"
        response += f"Content-Length: {len(html_data.encode('utf-8'))}\r\n"
        response += "\r\n"
        response += html_data
        client_socket.sendall(response.encode("utf-8"))
        try:
            client_socket.sendall(response.encode("utf-8"))
        except ConnectionAbortedError:
            print("Client aborted the connection.")
        except Exception as e:
            print(f"An error occurred: {e}")



    elif requested_path.endswith(".html"):
        try:
            file_name = requested_path.lstrip("/")
            with open(file_name, "r") as html_file:
                html_data = html_file.read()

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += f"Content-Length: {len(html_data)}\r\n"
            response += "\r\n"
            response += html_data

            try:
                client_socket.sendall(response.encode())
                client_socket.sendall(html_data.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")

        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\n\r\nHTML file not found."
            try:
                client_socket.sendall(response.encode())
            except ConnectionAbortedError:
                print("Client aborted the connection.")
            except Exception as e:
                print(f"An error occurred: {e}")


    else: # If the path is unknown
        response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found."
        try:
            client_socket.sendall(response.encode())
        except ConnectionAbortedError:
            print("Client aborted the connection.")
        except Exception as e:
            print(f"An error occurred: {e}")


def image_post_directly(client_socket ,client_topic):
    img_url=""
    if client_topic in image_list_1 or "peer" in client_topic: # if the server has the image
        img_url = image_list_1[-1]
    elif client_topic in image_list_1_ar or "النظير" in client_topic:
        img_url = image_list_1_ar[-1]

    else:
        image_post_redirect(client_socket,client_topic)
    if client_topic in image_list_1 or "peer" in client_topic:
        image_request = f"""
                    <html>
                    <head>
                        <title>Response</title>
                    </head>
                    <body>
                        <h1>Topic: {client_topic.replace("+", " ")} Type:  Image</h1>
                        <img width="640" height="360" class="photos" src="{img_url}" alt="P2P" class="P2P" target="_blank"> />
                    </body>
                    </html>
                    """
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(image_request)}\r\n"
        response += "\r\n"
        response += image_request
        client_socket.sendall(response.encode("utf-8"))
        client_socket.sendall(image_request.encode())
    elif  client_topic in image_list_1_ar or "النظير" in client_topic:
        image_request = f"""
                            <html lang="ar" dir="rtl">
                            <html>
                            <head>
                                <meta charset="UTF-8">
                                <title>Response</title>
                            </head>
                            <body>
                                <h1> النوع: صورة
                                </h1>
                                <h1>العنوان: {client_topic}</h1>
                                <img width="640" height="360" class="photos" src="{img_url}" alt="P2P" class="P2P" target="_blank"> />
                            </body>
                            </html>
                            """
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(image_request)}\r\n"
        response += "\r\n"
        response += image_request
        client_socket.sendall(response.encode("utf-8"))


# if the user asked for videos locally saved
def video_post_directly(client_socket ,client_topic):
    if client_topic in video_list_1:
        video_url = video_list_1[-1]
    elif client_topic in video_list_2:
        video_url = video_list_2[-1]
    elif client_topic in video_list_1_ar:
        video_url = video_list_1_ar[-1]
    elif client_topic in video_list_2_ar:
        video_url = video_list_2_ar[-1]
    else:
        return None
    if  client_topic in video_list_1 or client_topic in video_list_2:
        video_request = f"""
                    <html>
                    <head>
                    
                        <title>Response</title>
                    </head>
                    <body>
                        <h1>Topic: {client_topic.replace("+", " ")} Type:  Video</h1>
                        <video width="640" height="360" controls>
                            <source src="{video_url}">
                            Your browser does not support the video tag.
                        </video>
                    </body>
                    </html>
                    """
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(video_request)}\r\n"
        response += "\r\n"
        response += video_request
        client_socket.sendall(response.encode())
    elif client_topic in video_list_1_ar or client_topic in video_list_2_ar:
        video_request = f"""
                               <html lang="ar" dir="rtl">
                               <html>
                               <head>
                                    <meta charset="UTF-8">
                                   <title>Response</title>
                               </head>
                               <body>
                                  <h1>النوع : فيديو
                                  </h1>
                                  <h1>العنوان: {client_topic}</h1>
                                   <video width="640" height="360" controls>
                                       <source src="{video_url}">
                                       Your browser does not support the video tag.
                                   </video>
                               </body>
                               </html>
                               """
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(video_request)}\r\n"
        response += "\r\n"
        response += video_request
        client_socket.sendall(response.encode())


def image_post_redirect(client_socket, client_topic):
    # Construct the Google search URL
    img_url = f"https://www.google.com/search?q={client_topic.replace(' ', '+')}&udm=2"

    # HTML content to automatically redirect (no link displayed, just opens the page)
    image_request = f"""
    <html>
    <head>
        <title>Redirecting...</title>
        <meta http-equiv="refresh" content="0; url={img_url}" />
    </head>
    <body>
        <!-- The page redirects automatically, no link needed -->
        <p>If you are not redirected, <a href="{img_url}" target="_blank">click here</a>.</p>
    </body>
    </html>
    """

    # Calculate the content length correctly
    content_length = len(image_request.encode('utf-8'))

    # Construct the HTTP response
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {content_length}\r\n"
        "\r\n"
        f"{image_request}"
    )

    # Send the response to the client
    client_socket.sendall(response.encode('utf-8'))



def video_post_redirect(client_socket ,client_topic):
    video_url = f"https://www.youtube.com/results?search_query={client_topic.replace(' ', '+')}"
    video_request = f"""
                        <html>
                        <head>
                            <title>Response</title>
                             <meta http-equiv="refresh" content="0; url={video_url}">
                        </head>
                        </html>
                        """
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n"
    response += f"Content-Length: {len(video_request)}\r\n"
    response += "\r\n"
    response += video_request
    client_socket.sendall(response.encode())

# if the request method was "POST"
def post_request(client_socket, request, requested_path):
    request2 = request

    client_request = request.strip().split("\n")[-1].split("=")
    client_topic = "".join(client_request[1].strip().split("&")[0])
    client_type = "".join(client_request[2].strip())

    client_topic = client_topic.replace("+", " ").lower()
    client_topic = " ".join(client_topic.split())

    decoded_text = urllib.parse.unquote(client_topic)
    client_topic = html.unescape(decoded_text)
    decoded_text = urllib.parse.unquote(client_type)
    client_type = html.unescape(decoded_text)


    if client_type == "Image" or client_type =="صورة":
        if image_post_directly(client_socket, client_topic) is None:
            image_post_redirect(client_socket, client_topic)

    elif client_type == "Video" or client_type == "فيديو":
        if video_post_directly(client_socket, client_topic) is None:
            video_post_redirect(client_socket, client_topic)


def handle_client(client_socket):
    try :
        request = client_socket.recv(1024 * 2).decode()
        request_line = request.splitlines()[0]
        requested_path = request_line.split()[1]
        print("===============================================================================================")
        print(requested_path)
        print("========================================================================================================")
    except Exception:
        return None
    if "GET" in request_line:
        get_request(client_socket, requested_path)

    elif "POST" in request_line:
        post_request(client_socket, request, requested_path)


    print(request)
    client_socket.close()

def protocol_listener():
    try :
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', PORT_NUMBER))
        server_socket.listen(10)
    except Exception:
        print("full listen error")
        return None

    print(f"Server running on port {PORT_NUMBER}...")

    while True: # keep listen
        client_socket, addr = server_socket.accept()
        print("Got connection from", addr)
        handle_client(client_socket)

if __name__ == "__main__":
    protocol_listener()