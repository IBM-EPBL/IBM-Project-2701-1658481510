import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization="lz4nll"
deviceType="Child"
deviceId="12345"
authMethod="token"
authToken="12345678" 

try:
    deviceOptions={"org": organization,"type": deviceType,"id": deviceId,"auth-method": authMethod,"auth-token": authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
    print("caught exception connecting device:%s" % str(e))
    sys.exit()
 
deviceCli.connect()
while True:
          #in data
          name="kishor"
          #lattitude=11.663579;
          #longtitude=78.146254;

          #out data
          lattitude=12.7345;
          longtitude=13.2020;
          
          data={'lat':lattitude,'lon':longtitude,'name':name}
          def myOnPublishCallback():
            print("published lattitude=%d" %lattitude,"longtitude=%d" %longtitude,"to ibm watson")
          
        
          success=deviceCli.publishEvent("IotSensor","json",data,qos=0,on_publish=myOnPublishCallback)
          if not success:
              print("Not connected to IoTF")
          time.sleep(3)
deviceCli.disconnect()










 









                
