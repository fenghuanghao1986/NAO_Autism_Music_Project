//������ F0903702 5083709048
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
	string result;//���Ľ��

	//���ȿ���һ��string�Ƿ�Ϊ��һ��string��һ����
	if (str1.find(str2)>=0&&str1.find(str2)<str1.size())
	{
		result=str1.substr(0,str1.find(str2))+str2+str1.substr(str1.find(str2)+str2.size(),str1.size()-str2.size());
	}
	else if (str2.find(str1)>=0&&str2.find(str1)<str2.size())
	{
		result=str2.substr(0,str2.find(str1))+str1+str2.substr(str2.find(str1)+str1.size(),str2.size()-str1.size());
	}

	//�ٿ���һ��string������һ����һ���ֵ����
	else
	{
		int size=str1.size()<str2.size()?str1.size():str2.size();
		int pos1=0,pos2=0;

		//ԭ�����ڶ���string��һ��ȥ���һ���ַ��������һ��string�Ƚϡ�ֱ���ڶ���stringʣ�µĲ���Ϊ��һ��string��һ����
		for (int i=0;i<str2.size();i++)
		{
			if (str1.size()+i<str2.size())//��Ҫ���ǵڶ���string���ڵ�һ�������
			{
				;
			}
			else if (str1.find(str2.substr(0,str2.size()-i))!=str1.size()-str2.size()+i)
			{
				pos1++;//ÿ���ڶ���string��ʣ�ಿ�����һ��string��ƥ�䣬position��һ���������Ǿ�֪����ʱ����ƥ���ˡ�
			}
			else
				break;
		}

		//����һ�ڶ���string��һ����ͬ��Ƚ�
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
		result=result1.size()<=result2.size()?result1:result2;//ѡ����̵Ľ��
	}
	cout<<"\nOutput:\n"<<result;
	system("pause");
}
