//f0903704	5090379141	张恒 第一次作业
//题目:构造字符串  使其包含给出的两个字符串  并要求长度最短 以第一句字符串开头优先
//思路:本题用依次首尾匹配 来缩短字符串长度 并在过程中决定优先级 其表观复杂度为O(n)
#include<iostream>
#include<string>
using namespace std;
bool judge(string l1,string l2,int i){						//用于判断l1的尾部开始和l2首部开始i个字符是否匹配
	int len=i;												//用于保存匹配长度
	if (len>l2.length()){									//如果长度大于后面字符串长度  则修改长度
		len=l2.length();
	}
	return 
		(l1.substr(l1.length()-i,len)==l2.substr(0,len));
};
void main(){
	string s1,s2,s3;
	cin>>s1;
	cin>>s2;
	int i,irecord(0);										//irecord用于保存第一优先级的最大匹配长度
	s3=s1+s2;												//以最坏情况建立初值
	for(i=1;i<=s1.length();i++){							//第一优先级:s1为首.s2为尾  开始匹配	
		if(judge(s1,s2,i)){
			if (i>s2.length())								//特殊情况处理:包含情况
				s3=s1;
			else
				s3=s1+s2.substr(i,s2.length()-i);			//一般情况处理:接尾
			irecord=i;										//匹配成功后修改保存的最大值  此处匹配程度递增
		}
	}
	for(i=1;i<=s2.length();i++){							//第二优先级:s2为首.s1为尾  开始匹配 后面部分处理同上
		if(judge(s2,s1,i)&&(i>irecord)){					//和已获得的匹配方案比较匹配程度
			if (i>s1.length())
				s3=s2;
			else
				s3=s2+s1.substr(i,s2.length()-i);
		}
	}
	cout<<s3<<endl;											
}