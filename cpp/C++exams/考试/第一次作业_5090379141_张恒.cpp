//f0903704	5090379141	�ź� ��һ����ҵ
//��Ŀ:�����ַ���  ʹ����������������ַ���  ��Ҫ�󳤶���� �Ե�һ���ַ�����ͷ����
//˼·:������������βƥ�� �������ַ������� ���ڹ����о������ȼ� ���۸��Ӷ�ΪO(n)
#include<iostream>
#include<string>
using namespace std;
bool judge(string l1,string l2,int i){						//�����ж�l1��β����ʼ��l2�ײ���ʼi���ַ��Ƿ�ƥ��
	int len=i;												//���ڱ���ƥ�䳤��
	if (len>l2.length()){									//������ȴ��ں����ַ�������  ���޸ĳ���
		len=l2.length();
	}
	return 
		(l1.substr(l1.length()-i,len)==l2.substr(0,len));
};
void main(){
	string s1,s2,s3;
	cin>>s1;
	cin>>s2;
	int i,irecord(0);										//irecord���ڱ����һ���ȼ������ƥ�䳤��
	s3=s1+s2;												//������������ֵ
	for(i=1;i<=s1.length();i++){							//��һ���ȼ�:s1Ϊ��.s2Ϊβ  ��ʼƥ��	
		if(judge(s1,s2,i)){
			if (i>s2.length())								//�����������:�������
				s3=s1;
			else
				s3=s1+s2.substr(i,s2.length()-i);			//һ���������:��β
			irecord=i;										//ƥ��ɹ����޸ı�������ֵ  �˴�ƥ��̶ȵ���
		}
	}
	for(i=1;i<=s2.length();i++){							//�ڶ����ȼ�:s2Ϊ��.s1Ϊβ  ��ʼƥ�� ���沿�ִ���ͬ��
		if(judge(s2,s1,i)&&(i>irecord)){					//���ѻ�õ�ƥ�䷽���Ƚ�ƥ��̶�
			if (i>s1.length())
				s3=s2;
			else
				s3=s2+s1.substr(i,s2.length()-i);
		}
	}
	cout<<s3<<endl;											
}