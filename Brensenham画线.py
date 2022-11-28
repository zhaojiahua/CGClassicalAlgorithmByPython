import maya.cmds as cmds
import math
#画点函数(这个函数是向输出设备画点的,可根据不同的开发环境修改此函数,能把点画出来就行)
def DrawPoint(inP):
	dp=cmds.duplicate("pP")[0]
	cmds.xform(dp,t=(inP[0],inP[1],0))
	cmds.setAttr(dp+'.visibility',1)

#Brensenham算法画线
def BrensenhamLine(StartP,endP):
	PointsforLine=[]
	#保证x方向从小到大
	if StartP[0]>endP[0]:
		#temp中间复制的是深拷贝,这里改变StartP或endP值不会影响原始的StartP和endP的值
		#如果直接用=赋值是浅拷贝,会修改原始的数据
		temp=StartP
		StartP=endP
		endP=temp
	PointsforLine.append([StartP[0],StartP[1]])	#这里注意不能直接添加StartP,否则会被后面的函数修改的
	#保证Y方向也从小到大,如果不是要翻转
	cpoyStartP=[StartP[0],StartP[1]]
	cpoyendP=[endP[0],endP[1]]
	flipY=False
	if StartP[1]>endP[1]:
		cpoyStartP[1]*=-1
		cpoyendP[1]*=-1
		flipY=True
	#保证斜率在0到1之间,如果不是要进行调整
	dx=cpoyendP[0]-cpoyStartP[0]
	dy=cpoyendP[1]-cpoyStartP[1]
	swapxy=False
	if dx<dy:
		cpoyStartP[0],cpoyStartP[1]=cpoyStartP[1],cpoyStartP[0]
		cpoyendP[0],cpoyendP[1]=cpoyendP[1],cpoyendP[0]
		dx,dy=dy,dx
		swapxy=True
	tempx=cpoyStartP[0]
	tempy=cpoyStartP[1]
	p=2*dy-dx
	for i in range(dx):
		if p>0:
			tempy+=1
			p-=2*dx
		tempx+=1
		p+=2*dy
		temptempx=tempx
		temptempy=tempy
		if swapxy:
			temptempx,temptempy=temptempy,temptempx
		if flipY:
			temptempy=-temptempy
		PointsforLine.append([temptempx,temptempy])
	return PointsforLine
#画线
def DrawLine(startP,endP):
	for p in BrensenhamLine(startP,endP):
		DrawPoint(p)
startPoint=[100,100]
raduis=50
'''
DrawLine(startPoint,[130,100])
DrawLine(startPoint,[100,130])
DrawLine(startPoint,[70,100])
DrawLine(startPoint,[100,70])
DrawLine(startPoint,[130,130])
DrawLine(startPoint,[70,130])
'''
for i in range(36):
	endPoint=[int(math.cos(0.01745329251994329*i*10)*raduis)+startPoint[0],int(raduis*math.sin(0.01745329251994329*i*10))+startPoint[1]]
	DrawLine(startPoint,endPoint)

