输入：训练集，k的大小
输出：投影矩阵
function Topca(data,numberofk)
	meandata<--mean(data)
	dataminusmean<--data-meandata
	covdata<--cov(dataminusmean,rowvar=0)//对每列求协方差
	evals,evects<--linalg.eig(covdata)//求相应特征值特征向量
	evalsex<--argsort(evals)   //对特征值从小到大排序
	evalsex<--evalsex[-1:-(numberofk+1):-1]  //取最大的前k个特征值
	evectsex<--evects[:,evalsex]   //取与特征值相应的前k个特征向量
	return evectsex        //返回训练集的投影矩阵
end function



输入：训练集，k的大小
输出：投影矩阵
function ToSVD(data,numberofk):
	dataU,datasigma,datav<--linalg.svd(data)  //应用linalg包进行svd处理
	for x in dataU do   //选择前k列
		temu<--x[:numberofk]
		selectu<--temu
	selectsigma<--datasigma[:numberofk]   //选择前k个sigma
	selectv<--datav[:numberofk]   //选择前k行
	finalv<--selectv.T
	return finalv  //返回训练集的投影矩阵
end function
