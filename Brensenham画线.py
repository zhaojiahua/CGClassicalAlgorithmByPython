import maya.cmds as cmds
import math
#���㺯��(���������������豸�����,�ɸ��ݲ�ͬ�Ŀ��������޸Ĵ˺���,�ܰѵ㻭��������)
def DrawPoint(inP):
	dp=cmds.duplicate("pP")[0]
	cmds.xform(dp,t=(inP[0],inP[1],0))
	cmds.setAttr(dp+'.visibility',1)

#Brensenham�㷨����
def BrensenhamLine(StartP,endP):
	PointsforLine=[]
	#��֤x�����С����
	if StartP[0]>endP[0]:
		#temp�м临�Ƶ������,����ı�StartP��endPֵ����Ӱ��ԭʼ��StartP��endP��ֵ
		#���ֱ����=��ֵ��ǳ����,���޸�ԭʼ������
		temp=StartP
		StartP=endP
		endP=temp
	PointsforLine.append([StartP[0],StartP[1]])	#����ע�ⲻ��ֱ�����StartP,����ᱻ����ĺ����޸ĵ�
	#��֤Y����Ҳ��С����,�������Ҫ��ת
	cpoyStartP=[StartP[0],StartP[1]]
	cpoyendP=[endP[0],endP[1]]
	flipY=False
	if StartP[1]>endP[1]:
		cpoyStartP[1]*=-1
		cpoyendP[1]*=-1
		flipY=True
	#��֤б����0��1֮��,�������Ҫ���е���
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
#����
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

