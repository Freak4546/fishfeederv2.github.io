from flask import Flask, request, jsonify
import snowflake.connector
from flask_cors import CORS
import serial
import socket
import time

# Configure the serial port
arduino_ip = "192.168.0.167"  # IP address of Arduino on your network
arduino_port = 80  # Port number you set on the Arduino

# Establish TCP/IP connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




# Wait for the Arduino to initialize
time.sleep(2)

app = Flask(__name__)
CORS(app)

# Snowflake connection configuration
snowflake_config = {
    'user' : 'SATHISHAZURE',
    'password' : 'sat@APR30',
    'account' : 'ujsdhkh-li55973',
    'role' : 'skr_role',
    'warehouse' : 'skr_wh',
    'database' : 'skr_db',
    'schema' : 'skr_schema'
}


# Establish Snowflake connection
conn = snowflake.connector.connect(**snowflake_config)

@app.route('/update', methods=['POST'])
def update_data():
    try:
        data = request.json
        cursor = conn.cursor()
        query = f"update FISHFEED set Active='{data['column1']}'"   #column2 = '{data['column2']}' WHERE condition_column = '{data['condition']}'"

        # query = f"UPDATE your_table SET column1 = '{data['column1']}', column2 = '{data['column2']}' WHERE condition_column = '{data['condition']}'"
        cursor.execute(query)
        conn.commit()
      
        if (data['column1'] == '1'):
         #   serial_port = serial.serial_for_url('socket://192.168.0.167:80')  # Replace with Arduino IP address
         #   client_socket.connect((arduino_ip, arduino_port))
            serial_port = serial.serial_for_url('socket://192.168.0.167:80')  # Replace with Arduino IP address
            client_socket.connect((arduino_ip, arduino_port))
            print("Active data" ,data['column1'])
        #else:
         #   serial_port.close()
        #while (data['column1'] == '1'):
            # Create a virtual serial connection using pyserial
            #client_socket.connect((arduino_ip, arduino_port))
         #   print("Fish Feeding Started" , data['column1'])
        #else: 
        #    client_socket.close()
        #serial_port.close()
        #print("Serial connection closed", data['column1'])
        # Send data to Arduino
        # message = "Hello Arduino!"
        #print("sending data to Arduino")
        #client_socket.sendall(message.encode())
        #print("sent data to Arduino")
        #response = client_socket.recv(1024)
        #print("Response from Arduino:", response.decode())

        # Wait for a response from Arduino
        #arduino_response = ser.readline() #.decode().strip()
        #print("Arduino Response:", arduino_response)
        return jsonify({'message': 'Data updated successfully'})
        #return render_template('index.html', title="page", jsonfile=json.dumps('Success'))
    except Exception as e:
        #if serial_port.
        serial_port.close()
        print("EX : Serial connection closed")
        return jsonify({'error': str(e)}), 500
#finally:
        # Close the socket connection
        client_socket.close()

if __name__ == '__main__':
    app.run(debug=True)
