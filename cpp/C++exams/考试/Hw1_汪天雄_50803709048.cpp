//汪天雄 F0903702 5083709048
//String concatenation
#include <iostream>
#include <string>
using namespace std;
void main()
{
	cout<<"Input:\n";
	string str1,str2;
	cin>>str1>>str2;
	while (str1.size()>50||str1.size()<1||str2.size()>50||str2.size()<1)
	{
		cout<<"1<=length<=50"<<endl;
		cout<<"Input:\n";
		cin>>str1>>str2;
	}
	string result;//最后的结果

	//首先考虑一个string是否为另一个string的一部分
	if (str1.find(str2)>=0&&str1.find(str2)<str1.size())
	{
		result=str1.substr(0,str1.find(str2))+str2+str1.substr(str1.find(str2)+str2.size(),str1.size()-str2.size());
	}
	else if (str2.find(str1)>=0&&str2.find(str1)<str2.size())
	{
		result=str2.substr(0,str2.find(str1))+str1+str2.substr(str2.find(str1)+str1.size(),str2.size()-str1.size());
	}

	//再考虑一个string不是另一个的一部分的情况
	else
	{
		int size=str1.size()<str2.size()?str1.size():str2.size();
		int pos1=0,pos2=0;

		//原理：将第二个string逐一减去最后一个字符，再与第一个string比较。直到第二个string剩下的部分为第一个string的一部分
		for (int i=0;i<str2.size();i++)
		{
			if (str1.size()+i<str2.size())//需要考虑第二个string长于第一个的情况
			{
				;
			}
			else if (str1.find(str2.substr(0,str2.size()-i))!=str1.size()-str2.size()+i)
			{
				pos1++;//每当第二个string的剩余部分与第一个string不匹配，position加一。这样我们就知道何时他们匹配了。
			}
			else
				break;
		}

		//将第一第二个string反一反，同理比较
		for (int i=0;i<str1.size();i++)
		{
			if (str2.size()+i<str1.size())
			{
				;
			}
			else if (str2.find(str1.substr(0,str1.size()-i))!=str2.size()-str1.size()+i)
			{
				pos2++;
			}
			else
				break;
		}
		string result1=str1.substr(0,str1.size()-size+pos1)+str2;
		string result2=str2.substr(0,str2.size()-size+pos2)+str1;
		result=result1.size()<=result2.size()?result1:result2;//选择最短的结果
	}
	cout<<"\nOutput:\n"<<result;
	system("pause");
}
