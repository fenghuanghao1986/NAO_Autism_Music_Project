#ifndef HASH_H
#define HASH_H
#include<string>
#include<sstream>
using namespace std;
stringstream ss;

string DisperseNumber(string name)
{
	stringstream ss1;
	int lengthOfName = name.size();
	int tempNumber_1;
	tempNumber_1 = (int)name[0] + (int)name[1]*3 + (int)name[2]*5 + (int)name[3]*7 + (int)name[4]*11;
	int tempNumber_2 = (tempNumber_1 * tempNumber_1)%100003;
	string number;
	ss1 << tempNumber_2;
	ss1 >> number;
	return number;
}
class HashTable
{
public:
	enum KindofCell {Active,Empty,Delete};
	//��־Hash���е�Ԫ��״̬��Active�������㡣Empty����ԪΪ�ա�Deleted������Ľ���ѱ�ɾ��
	HashTable();//����
	~HashTable(){delete[] Arr;}//����
	HashTable & operator = ( HashTable & R);
	int Insert ( string &X);//����X
	int Remove( string &X);//ɾ��X
	int Find ( string &X);
	//���ҳɹ������ؽ������ֵ�����ú���WasFoundȷ�������Ƿ�ɹ�
	int IsFound ( string &X) ;//����X�Ƿ���ڣ����ڷ���1������Ϊ0
	int WasFound () ;//���һ�β��ҳɹ��򷵻�1
	int IsEmpty () ; //Hash��Ϊ�գ�����1������Ϊ0
	void MakeEmpty ();//���Hash��
	unsigned int FindPos (string &X);
	//����ֵΪX�Ľ����ɢ�б��еĵ�Ԫ��ַ
private:
	struct HashCell
	{
		string Element;//����������ֵ
		KindofCell info;//��־��Ԫ״̬
		HashCell ():info(Empty){}
		HashCell (string &E,KindofCell i = Empty):Element(E),info(i){}
	};
	enum { DefaultSize = 100000};
	unsigned int ArrSize;//ɢ�б��õ����ڵĵ�Ԫ����
	int CurrentSize;//ɢ�б��е�ǰ����Ľ�����
	int LastFindOk;//���һ�β��ҳɹ���Ϊ1
	HashCell *Arr;//����ɢ�б��õ�����
	void AllocateArr ();//����һ������
};

void HashTable::AllocateArr()
{
	Arr = new HashCell[ArrSize];
}

HashTable::HashTable():ArrSize(DefaultSize)
{
	AllocateArr();
	CurrentSize = 0;
}

void HashTable::MakeEmpty()
{
	CurrentSize = 0;
	for(int k = 0;k < ArrSize;k++)
		Arr[k].info = Empty;
}

HashTable &
HashTable::operator = (HashTable &R)
{
	if(this != &R)
	{
		delete[] Arr;
		ArrSize = R.ArrSize;
		AllocateArr();
		for(int k = 0;k < ArrSize;k ++)
			Arr[k] = R.Arr[k];
		CurrentSize = R.CurrentSize;
	}
	return *this;
}

//����̽�ⷨ�Ĳ��ҡ������ɾ������
unsigned int HashTable::FindPos(string &X)
{
	string index = DisperseNumber(X);
	unsigned int k = 0;//���ڼ�¼̽��ʧ�ܵĴ���
	unsigned int CurrentPos = atoi(index.c_str());
	while(Arr[CurrentPos].info != Empty /*&& Arr[CurrentPos].Element != X*/)
	{
		CurrentPos += 2 * ++k -1;//����̽�ⷨ
		/*CurrentPos ++;*/
		while(CurrentPos >= ArrSize)
			CurrentPos -= ArrSize;
	}
	return CurrentPos;
}

 int HashTable::Find( string &X)
{
	string index = DisperseNumber(X);
	unsigned int k = 0;//���ڼ�¼̽��ʧ�ܵĴ���
	unsigned int CurrentPos = atoi(index.c_str());
	while(Arr[CurrentPos].Element != X)
	{
		CurrentPos += 2 * ++k -1;//����̽�ⷨ
		/*CurrentPos ++;*/
		while(CurrentPos >= ArrSize)
			CurrentPos -= ArrSize;
	}
	return CurrentPos;
}

int HashTable::WasFound()
{
	return LastFindOk;
}

int HashTable::IsFound(string &X)
{
	int CurrentPos = FindPos(X);
	return Arr[CurrentPos].info == Active;
}

int HashTable::Remove(string &X)
{
	unsigned int CurrentPos = FindPos(X);
	if(Arr[CurrentPos].info != Active)
		return 0;
	Arr[CurrentPos].info = Delete;
		return 1;
}

int HashTable::Insert(string &X)
{
	unsigned int CurrentPos = FindPos(X);
	if(Arr[CurrentPos].info == Active)
		return 0;//�Ѿ����ڣ�����ʧ��
	Arr[CurrentPos] = HashCell(X,Active);
	return 1;
}

#endif