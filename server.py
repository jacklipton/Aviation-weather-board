import socket
import time
import AviationWeatherServer
import light_control

def run_server():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP and port
    s.bind(('', 80))

    # Listen for incoming connections
    s.listen(5)


    last_action_time = time.time()
    status = True

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)

        buttonA = request.find('/?buttonA')
        buttonB = request.find('/?buttonB')

        if buttonA == 6:
            print('Button A was pressed')
            # Add your action here
            status = True
            AviationWeatherServer.AvWeather()
            last_action_time = current_time


        if buttonB == 6:
            print('Button B was pressed')
            # Add your action here
            status = False
            light_control.turnOff()

        current_time = time.time()
        if current_time - last_action_time >= 15 * 60 and status:  # 15 minutes in seconds
            print('15 minutes have passed, performing action')
            # Add your action here
            AviationWeatherServer.AvWeather()
            last_action_time = current_time

        response = """HTTP/1.1 200 OK
    Content-Type: text/html

    <!DOCTYPE HTML>
    <html>
    <body>
    <button onclick="location.href='/?buttonA'">Button A</button>
    <button onclick="location.href='/?buttonB'">Button B</button>
    </body>
    </html>
    """
        conn.send(response)
        conn.close()