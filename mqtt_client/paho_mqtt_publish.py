import paho.mqtt.publish as publish
import time

HOST = "172.16.210.150"
PORT = 1883


if __name__ == '__main__':
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    publish.single("devcloud/code/hub", "This an MQTT publisher", qos=1, hostname=HOST, port=PORT, client_id=client_id,
                   auth={'username': "admin", 'password': "public"})
