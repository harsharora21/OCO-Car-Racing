import gym
import numpy as np
from time import sleep
from pynput import keyboard 
from collections import defaultdict
import matplotlib.pyplot as plt 
from numba import jit,njit

pKeys = defaultdict(int)

def on_press(key):
    try:
        pKeys[key.char.lower()]=1
    except:
        pass

def on_release(key):
    try:
        pKeys[key.char.lower()]=0
    except:
        pass


env = gym.make("CarRacing-v0")
observation = env.reset()

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

def convImg(obs):
	obs=np.array(obs)
	def colorTr(x):
		r,g,b=x
		out = [0,0,0]
		if r>=254:
			out= [255,255,255]
		elif r<=120 and b<=120 and g<=120:
			out= [0,0,0]
		elif g>=190:
			out= [0,255,0]
		elif r>=190:
			out= [255,0,0]
		return (out)
	return list(map(lambda x: list(map(colorTr,x)),obs))
@njit
def colorTr(x):
		r,g,b=x
		out = [False,False]
		if r>=254:
			out= [False,False]
		elif r<=120 and b<=120 and g<=120:
			out= [False,True]
		elif g>=190:
			out= [True,False]
		elif r>=190:
			out= [True,True]
		return (out)

def convImg2(obs):
	obs=np.array(obs)
	z = np.array(list(map(lambda x: list(map(colorTr,x)),obs))).ravel()
	return np.concatenate([z,~z])

def ocoTrain(W,X,Y,eps=0.5):
	for i in range(W.shape[0]):
		w = W[i]
		y=Y[i]
		W[i] = (w*(np.ones(X.shape[0])- (eps*(X^y))))/sum(w)
	return W

def ocoOut(W,X):
	Y=[]
	for w in W:
		Y.append(np.random.choice(X,p=w/sum(w)))
	return np.array(Y)

obs=np.array(observation)
n=convImg2(obs).size
wts = []
for i in range(4):
	wts.append(np.ones(n)/n)
wts=np.array(wts)
print(wts.shape)
while True:
	env.render()
	obs=np.array(observation)

	movMat = np.array([[0,1,0],[0,0,1],[-1,0,0],[1,0,0]])
	if pKeys['m']:
		manualVec = np.array([[pKeys[x] for x in ['w','s','a','d']]])
		ocoTrain(wts,convImg2(obs),manualVec[0])
		curAction = 0.5*(np.matmul(manualVec,movMat)[0])
	else:
		autoVec = np.array([ocoOut(wts,convImg2(obs))+0])
		curAction = 0.5*(np.matmul(autoVec,movMat)[0])
	print(curAction)
	observation, reward, done, info = env.step(curAction)
	#print(observation)
	if pKeys['q']:
		break
	if done or pKeys['r']:
		print("Done")
		observation = env.reset()
		isReset=False
	if pKeys['x']:
		print("showing image")
		img = (np.array(convImg(observation)))
		plt.imshow(img)
		plt.show()
	
env.close()

