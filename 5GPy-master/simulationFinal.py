import simpy
import random
from Algorithm import FuzzyLogic
from Algorithm2 import IrrigationIoT

#--------------------------------------------------------------5GAgroSim------------------------------------------------------------------------------
# This is a simulator for agro environments supported by 5G networks

#this class represents a base sensor
class BaseSensor(object):
	def __init__(self, env, aId, aType, iotGateway, generationInterval, sendInterval):
		self.env = env
		self.aId = aId#id of this sensor
		self.aType = aType#type of this sensor
		self.packets = []#keeps the generated data/packets in this sensor
		self.start = self.env.process(self.run())#put the self.run() into a simpy process
		self.sendUp = self.env.process(self.sendData(sendInterval))#put the self.sendData() into a simpy process
		self.iotGateway = iotGateway#the iot gateway element to whom this sensor will communicate
		self.generationInterval = generationInterval#time interval to generate data

	#put the sensor to run
	def run(self):
		packetId = 0#counter to identify each generated packet in this sensor
		while True:
			yield self.env.timeout(self.generationInterval)#wait a given time to generate another packet/data
			packet = BasePacket(packetId, self.aId, "Normal", 120)#120  is a value in kb for the size of the packet 
			print("Sensor {} of Type {} generated Packet: ID {} Type {} Size {} at moment {}\n".format(self.aId, self.aType, packet.aId, packet.aType, 
																	packet.aSize, self.env.now))#self.env.now is the current time of the simulation run
			self.packets.append(packet)#append to its list of generated packets
			packetId+=1#increment the counter of packets

	#this method periodically sends the stored data to the iot gateway
	def sendData(self, sendTime):
		packetId = 0#counter to identify each generated "iot" packet in this sensor
		while True:
			yield self.env.timeout(sendTime)
			if self.packets:#verify if there is data/packets to send
				#create a "iot" packet containing all generated data/packets so far
				iotPkt = iotPacket(packetId, self.aId, "IoT", len(self.packets)*120, self.packets.copy())#120  is a value in kb for the size of the packet 
				self.iotGateway.aggregatedData.put(iotPkt)#"send" it to the iot gateway connected to this sensor
				packetId += 1#increment the counter of packets
				self.packets = []#clean the stored packets in this sensor


#this class represents a base data packet
class BasePacket(object):
	def __init__(self, aId, source, aType, aSize):
		self.aId = aId#id of this packet
		self.source = source#source id of the sensor that generated this packet
		self.aType = aType#type of this packet
		self.aSize = aSize#size of this packet in kb

#this class represents a packet that aggregates several packets from a sensor
class iotPacket(BasePacket, object	):
	def __init__(self, aId, source, aType, aSize, packets):
		super().__init__(aId, source, aType, aSize)
		self.packets = packets

#this class represents a network iot gateway of sensors data/packets
class BaseIoTGateway(object):
	def __init__(self, env, aId):
		self.env = env
		self.aId = aId
		self.aggregatedData = simpy.Store(self.env)#each packet sent from the sensor is firstly stored here
		self.sensorsPackets = []#put the received packets
		self.connectedSensors = []#aggregation of the sensors connected to it 
		self.start = self.env.process(self.run())#put the self.run() into a simpy process
		self.totalIotPackets = 0#counts the received IoT packets
		self.totalSinglePackets = 0#counts the total data packets aggregated/received
		self.capacity = 256 # capacity of lorawan antenna
		self.transmissionRate = self.env.timeout(self.totalSinglePackets/self.capacity)
	#put the iotGateway to run
	def run(self):
		print("...IoT Gateway {} is running and receiving data from sensors...")
		while True:
			#waits to receive data from a sensor
			p = yield self.aggregatedData.get()
			self.transmissionRate
			print("Data reaching  from IoT gateway at moment {}\n".format(self.env.now)) 
			print("Received data from sensor {}".format(p.source))
			self.sensorsPackets.append(p)
			self.connectedSensors.append(p)
			self.totalIotPackets += 1
			self.totalSinglePackets += len(p.packets)
			FuzzyLogic.run() #Run fuzzy Logic irrigation algorithm
			# IrrigationIoT.run() # tradicional irrigation algorithm

class antenna5gGateway(BaseIoTGateway,object):
	def __init__(self, env, aId):
			super().__init__(env, aId)
			self.capacity = 2684354560 #capacity of 5G antenna
			self.transmissionRate = self.env.timeout(self.totalSinglePackets/self.capacity)
	def run(self):
			print("...5G  gateway {} is running and receiving data from sensors...")
			while True:
				#waits to receive data from a sensor
				z = yield self.aggregatedData.get()
				self.transmissionRate
				print("Data reaching  from 5G gateway at moment {}\n".format(self.env.now))
				print("Received data from sensor {}".format(z.source))
				self.sensorsPackets.append(z)
				self.connectedSensors.append(z)
				self.totalIotPackets += 1
				self.totalSinglePackets += len(z.packets)
				FuzzyLogic.run() #Run fizzy Logic irrigation algorithm
				# IrrigationIoT.run() # tradicional irrigation algorithm

#this class repreents a basic network/processing node - it will be inherited for the creation of processing and networking nodes
class BaseNode(object):
	def __init__(self, env, packetId, aType, neighbours):
		self.env = env
		self.packetId = packetId
		self.aType = aType
		self.neighbours = neighbours#adjacent nodes

	#put the processing node to run
	def run(self):
		pass

	#send data to some adjacency
	def sendData(self):
		pass

class SoilTemperatureSensor(BaseSensor, object):

	def _init_(self, env, aId, aType, iotGateway, generationInterval, sendInterval):
		super()._init_(env, aId, aType, iotGateway, generationInterval, sendInterval)
	#put the sensor to run
	def run(self):
		packetId = 0#counter to identify each generated packet in this sensor
		while True:
			self.setTemperature = random.randrange(0,40)
			yield self.env.timeout(self.generationInterval)#wait a given time to generate another packet/data
			packet = BasePacket(packetId, self.aId, "Temperature", 120)#120  is a value in kb for the size of the packet 
			print("Sensor {} of Type {} generated Packet: ID {} Type {} Size {} at moment {} and the value {}\n".format(self.aId, self.aType, packet.aId, packet.aType, 
																	packet.aSize, self.env.now, self.setTemperature))#self.env.now is the current time of the simulation run
			self.packets.append(packet)#append to its list of generated packets
			packetId+=1#increment the counter of packets

	#this method periodically sends the stored data to the iot gateway
	def sendData(self, sendTime):
		packetId = 0#counter to identify each generated "iot" packet in this sensor
		while True:
			yield self.env.timeout(sendTime)
			if self.packets:#verify if there is data/packets to send
				#create a "iot" packet containing all generated data/packets so far
				iotPkt = iotPacket(packetId, self.aId, "IoT", len(self.packets)*120, self.packets.copy())#120  is a value in kb for the size of the packet 
				self.iotGateway.aggregatedData.put(iotPkt)#"send" it to the iot gateway connected to this sensor
				packetId += 1#increment the counter of packets
				self.packets = []#clean the stored packets in this sensor

class HumididtySensor(BaseSensor, object):

	def _init_(self, env, aId, aType, iotGateway, generationInterval, sendInterval ):
		super()._init_(env, aId, aType, iotGateway, generationInterval, sendInterval)
	#put the sensor to run
	def run(self):
		packetId = 0#counter to identify each generated packet in this sensor
		while True:
			self.setHumidity = random.randrange(0,60) # fuzzy logic range  
			# self.setHumidity = random.randrange(0,100) # tradicional Iot range 
			yield self.env.timeout(self.generationInterval)#wait a given time to generate another packet/data
			packet = BasePacket(packetId, self.aId, "Humididty", 120)#120  is a value in kb for the size of the packet 
			print("Sensor {} of Type {} generated Packet: ID {} Type {} Size {} at moment {} and the value {}\n".format(self.aId, self.aType, packet.aId, packet.aType, 
																	packet.aSize, self.env.now, self.setHumidity))#self.env.now is the current time of the simulation run
			self.packets.append(packet)#append to its list of generated packets
			packetId+=1#increment the counter of packets

	#this method periodically sends the stored data to the iot gateway
	def sendData(self, sendTime):
		packetId = 0#counter to identify each generated "iot" packet in this sensor
		while True:
			yield self.env.timeout(sendTime)
			if self.packets:#verify if there is data/packets to send
				#create a "iot" packet containing all generated data/packets so far
				iotPkt = iotPacket(packetId, self.aId, "IoT", len(self.packets)*120, self.packets.copy())#120  is a value in kb for the size of the packet 
				self.iotGateway.aggregatedData.put(iotPkt)#"send" it to the iot gateway connected to this sensor
				packetId += 1#increment the counter of packets
				self.packets = []#clean the stored packets in this sensor

class WaterLevelSensor(BaseSensor, object):

	def _init_(self, env, aId, aType, iotGateway, generationInterval, sendInterval):
		super()._init_(env, aId, aType, iotGateway, generationInterval, sendInterval)
	#put the sensor to run
	def run(self):
		packetId = 0#counter to identify each generated packet in this sensor
		while True:
			self.setWaterLevel = random.randrange(0,14)
			yield self.env.timeout(self.generationInterval)#wait a given time to generate another packet/data
			packet = BasePacket(packetId, self.aId, "WaterLevel", 120)#120  is a value in kb for the size of the packet 
			print("Sensor {} of Type {} generated Packet: ID {} Type {} Size {} at moment {} and the value {}\n".format(self.aId, self.aType, packet.aId, packet.aType, 
																	packet.aSize, self.env.now, self.setWaterLevel))#self.env.now is the current time of the simulation run
			self.packets.append(packet)#append to its list of generated packets
			packetId+=1#increment the counter of packets

	#this method periodically sends the stored data to the iot gateway
	def sendData(self, sendTime):
		packetId = 0#counter to identify each generated "iot" packet in this sensor
		while True:
			yield self.env.timeout(sendTime)
			if self.packets:#verify if there is data/packets to send
				#create a "iot" packet containing all generated data/packets so far
				iotPkt = iotPacket(packetId, self.aId, "IoT", len(self.packets)*120, self.packets.copy())#120  is a value in kb for the size of the packet 
				self.iotGateway.aggregatedData.put(iotPkt)#"send" it to the iot gateway connected to this sensor
				packetId += 1#increment the counter of packets
				self.packets = []#clean the stored packets in this sensor


class ProcessingNode(BaseNode, object):
	
		def __init__(self, env, aId,aType,iotGateway,algorithm):
			self.env = env
			self.aType = aType
			self.aId = aId
			self.algorithm = algorithm
			self.iotGateway = iotGateway
			self.aggregatedData = simpy.Store(self.env)#each packet sent from the sensor is firstly stored here	
			self.gatewayPackets = []#put the received packets
			self.start = self.env.process(self.run())#put the self.run() into a simpy process
			self.totalGatewaysPackets = 0#counts the received Gateways packets
			self.totalSinglePackets = 0#counts the total data packets aggregated/received
	
	#put the ProcessingNode to run
		def run(self):
			print("...Processing Node {} is running and receiving data from IoT Gateway...")
			
			while True:
				
				#waits to receive data from a sensor
				w = yield self.aggregatedData.get()
				print("Received data from Iot Gateway {}".format(w.source))
				self.gatewayPackets.append(w)
				self.totalGatewayPackets += 1
				self.totalSingleGatewayPackets += len(w.packets)




#---------------------------------------------------------------Running the simulation----------------------------------------------------------------
env = simpy.Environment()#sets the simpy environment
generationInterval = 100#time interval for a sensor to generate a single data packet
sendInterval = 500#time interval for a sensor to send its aggregated data to its iot gateway

iotGateway1 = BaseIoTGateway(env, "iotGateway 1")
# antenna5gGateway = antenna5gGateway(env, "5G")

#to see the sensors in  5G gateway, just uncomment this part
# soil_sensor_Temperature = SoilTemperatureSensor(env, 0, "Temperature",antenna5gGateway,generationInterval,sendInterval,)#create temperature sensor
# sensor_Humidity = HumididtySensor(env, 0, "Humidity", antenna5gGateway, generationInterval, sendInterval)
# sensor_Water_Level = WaterLevelSensor(env, 0, "WaterLevel", antenna5gGateway, generationInterval, sendInterval)

#to see tradicional Iot just uncomment this part
soil_sensor_Temperature = SoilTemperatureSensor(env, 0, "Temperature",iotGateway1,generationInterval,sendInterval,)#create temperature sensor
sensor_Humidity = HumididtySensor(env, 0, "Humidity", iotGateway1, generationInterval, sendInterval)
sensor_Water_Level = WaterLevelSensor(env, 0, "WaterLevel", iotGateway1, generationInterval, sendInterval)

#to see the ProcesingNode in  5G gateway, just uncomment this part

ProcessingNode = ProcessingNode(env, 0, "Cloud",iotGateway1,IrrigationIoT)
# ProcessingNode = ProcessingNode(env, 0, "Cloud",antenna5gGateway,FuzzyLogic)


print("---------------------------------------------Starting simulation---------------------------------------------")
env.run(5000)#sets the simulation to run for 3600 units of time (we can consider it as seconds) and starts the simulation
print("----------------------------------------------Ending simulation----------------------------------------------")
print("Total generated data: {} Mb".format(((iotGateway1.totalSinglePackets*120)/1000)/8))
# print("Total generated data: {} Mb".format(((antenna5gGateway.totalSinglePackets*120)/1000)/8))
#