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
	//标志Hash表中单元的状态。Active：保存结点。Empty：单元为空。Deleted：保存的结点已被删除
	HashTable();//构造
	~HashTable(){delete[] Arr;}//析构
	HashTable & operator = ( HashTable & R);
	int Insert ( string &X);//插入X
	int Remove( string &X);//删除X
	int Find ( string &X);
	//查找成功，返回结点数据值。可用函数WasFound确定查找是否成功
	int IsFound ( string &X) ;//测试X是否存在，存在返回1，否则为0
	int WasFound () ;//最近一次查找成功则返回1
	int IsEmpty () ; //Hash表为空，返回1，否则为0
	void MakeEmpty ();//清空Hash表
	unsigned int FindPos (string &X);
	//查找值为X的结点在散列表中的单元地址
private:
	struct HashCell
	{
		string Element;//保存结点数据值
		KindofCell info;//标志单元状态
		HashCell ():info(Empty){}
		HashCell (string &E,KindofCell i = Empty):Element(E),info(i){}
	};
	enum { DefaultSize = 100000};
	unsigned int ArrSize;//散列表用的所在的单元个数
	int CurrentSize;//散列表中当前保存的结点个数
	int LastFindOk;//最后一次查找成功则为1
	HashCell *Arr;//保存散列表用的数组
	void AllocateArr ();//创建一个数组
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

//二次探测法的查找、插入和删除操作
unsigned int HashTable::FindPos(string &X)
{
	string index = DisperseNumber(X);
	unsigned int k = 0;//用于记录探测失败的次数
	unsigned int CurrentPos = atoi(index.c_str());
	while(Arr[CurrentPos].info != Empty /*&& Arr[CurrentPos].Element != X*/)
	{
		CurrentPos += 2 * ++k -1;//二次探测法
		/*CurrentPos ++;*/
		while(CurrentPos >= ArrSize)
			CurrentPos -= ArrSize;
	}
	return CurrentPos;
}

 int HashTable::Find( string &X)
{
	string index = DisperseNumber(X);
	unsigned int k = 0;//用于记录探测失败的次数
	unsigned int CurrentPos = atoi(index.c_str());
	while(Arr[CurrentPos].Element != X)
	{
		CurrentPos += 2 * ++k -1;//二次探测法
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
		return 0;//已经存在，插入失败
	Arr[CurrentPos] = HashCell(X,Active);
	return 1;
}

#endif