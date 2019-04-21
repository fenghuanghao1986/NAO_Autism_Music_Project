#ifndef DATABASE_H
#define DATABASE_H
#include<fstream>
#include<iostream>
#include<string>
#include"hash.h"
#include"user.h"
#include"product.h"
#include"buy.h"
using namespace std;

ifstream UserDatFin,UserIdxFin,ProductDatFin,ProductIdxFin,BuyDatFin,BuyIdxFin;
ofstream UserDatFout,UserIdxFout,ProductDatFout,ProductIdxFout,BuyDatFout,BuyIdxFout;

class UserDataBase//�洢�û���Ϣ�����ݿ�
{
public:
	UserDataBase();//�������ݿ��ļ�
	int Find(user &theUser);//ͨ���ؼ�������ĳ���ݣ��ɹ�����1�����򷵻�0
	int FindID(string key);//�����û���
	int Insert(user theUser);//��dat�ļ��в���ĳ�û����ݣ��ɹ�����1�����򷵻�0
	int Delete(user theUser);//��idx�ļ���ɾ��ĳ�û����ݣ��ɹ�����1�����򷵻�0
	int Modify(user theUser);//��dat�ļ����޸�ĳ�û����ݣ��ɹ�����1�����򷵻�0
private:
	HashTable UserHash;
	int DataMove;//��¼���һ�����ݵ��ļ�ƫ����
};

UserDataBase::UserDataBase():DataMove(0)
{
	HashTable UserHash;
	UserDatFout.open("D:\\Trading Platform\\User.dat");
	UserIdxFout.open("D:\\Trading Platform\\User.idx");
	UserDatFout.close();
	UserIdxFout.close();
}

int UserDataBase::FindID(string key)
{

	UserIdxFin.open("D:\\Trading Platform\\User.idx");
	if(UserIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		return 0;
	}
	int FindNumber;
	FindNumber = UserHash.FindPos(key);
	UserIdxFin.seekg(20*FindNumber,ios::beg);
	//if( 0 == UserHash.WasFound())
	//	return 0;
	string temp_1;
	UserIdxFin >> temp_1;
	if(temp_1[1] != '/0')
	{
		UserIdxFin.close();
		return 0;
	}
	else
	{
		UserIdxFin.close();
		return 1;
	}
	
}

int UserDataBase::Find(user &theUser)
{
	string key = theUser.getID();
	UserIdxFin.open("D:\\Trading Platform\\User.idx");
	if(UserIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		return 0;
	}
	int FindNumber;
	FindNumber = UserHash.Find(key);
	UserIdxFin.seekg(20*FindNumber,ios::beg);
	/*if( 0 == UserHash.WasFound())
		return 0;*/
	string temp_1;
	UserIdxFin >> temp_1;
	cout << temp_1 << endl;
	string name,dataMove,dataLength;
	string temp_2 = "";
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			else if( colonNumber == 2)
				dataLength = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	int dataMoveNumber = atoi(dataMove.c_str());
	UserIdxFin.close();
	UserDatFin.open("D:\\Trading Platform\\User.dat");
	UserDatFin.seekg(dataMoveNumber,ios::beg);
	string temp_3;
	UserDatFin >> temp_3;
	string temp_4 = "";
	int length3 = temp_3.size();
	UserDatFin.close();
	colonNumber = 0;
	string ID,cipher,name2,sex,age,address,phone,interest;
	for( int i = 0; i < length3; i ++)
	{
		if( temp_3[i] == ':'|| i == length3 - 1 )
		{
			if(colonNumber == 0)
				ID = temp_4;
			else if(colonNumber == 1)
				cipher = temp_4;
			else if(colonNumber == 2)
				name2 = temp_4;
			else if(colonNumber == 3)
				sex = temp_4;
			else if(colonNumber == 4)
				age = temp_4;
			else if(colonNumber == 5)
				address = temp_4;
			else if(colonNumber == 6)
				phone = temp_4;
			else if(colonNumber == 7)
				interest = temp_4;
			temp_4 = "";
			colonNumber ++;
		}
		else
			temp_4 += temp_3[i];
	}
	string temp_5 = "";
	temp_5 += temp_3[length3-1];
	if( cipher == theUser.getCipher())
	{
		theUser.changeName(name2);
		theUser.changeSex(sex);
		theUser.changeAge(age);
		theUser.changeAddress(address);
		theUser.changePhone(phone);
		theUser.changeInterest(interest);
		theUser.changeIsAdmin(temp_5);
		return 1;
	}
	else
		return 0;
}

int	UserDataBase::Insert(user theUser)
{
	int FindNumber = UserHash.FindPos(theUser.getID());
	if( 0 == UserHash.Insert(theUser.getID()))
		return 0;
	UserIdxFout.open("D:\\Trading Platform\\User.idx",ios::in|ios::ate);
	UserIdxFout.seekp(20*FindNumber,ios::beg);//20Ϊ�趨��ÿ��������ռ�ַ�������
	UserIdxFout << theUser.getID() << ":" << DataMove << ":" << theUser.UserLength();
	string strDataMove;
	ss << DataMove;
	ss >> strDataMove;
	string strUserLength;
	ss << theUser.UserLength();
	ss >> strUserLength;
	int IndexSize = theUser.getID().size() + strDataMove.size() + strUserLength.size() + 2;
	for( int i = 0; i < 20 - IndexSize; i ++)
		UserIdxFout << " ";
	DataMove += theUser.UserLength();
	UserIdxFout.close();
	UserDatFout.open("D:\\Trading Platform\\User.dat",ios::app);
	UserDatFout << theUser.getID() <<":"<< theUser.getCipher() <<":"<< theUser.getName() <<":"<< theUser.getSex() <<":"<< theUser.getAge() 
		<<":"<< theUser.getAddress() <<":"<< theUser.getPhone() <<":"<< theUser.getInterest() <<":"<< theUser.getIsAdmin() << endl;
	UserDatFout.close();
	return 1;
}

int UserDataBase::Modify(user theUser)
{
	string key = theUser.getID();
	UserIdxFin.open("D:\\Trading Platform\\User.idx");
	if(UserIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		return 0;
	}
	string IndexNumber;
	int FindNumber;
	FindNumber = UserHash.Find(key);
	UserIdxFin.seekg(20*FindNumber,ios::beg);
	/*if( 0 == UserHash.WasFound())
		return 0;*/
	string temp_1;
	UserIdxFin >> temp_1;
	string name,dataMove,dataLength;
	string temp_2 = "";
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	dataLength = "51";
	int dataMoveNumber = atoi(dataMove.c_str());
	UserIdxFin.close();
	UserDatFout.open("D:\\Trading Platform\\User.dat",ios::in);
	UserDatFout.seekp(dataMoveNumber,ios::beg);
	UserDatFout << theUser.getID() <<":"<< theUser.getCipher() <<":"<< theUser.getName() <<":"<< theUser.getSex() <<":"<< theUser.getAge()
		<<":"<< theUser.getAddress() <<":"<< theUser.getPhone() <<":"<< theUser.getInterest() <<":"<< theUser.getIsAdmin() << endl;
	UserDatFout.close();
	return 1;
}

int UserDataBase::Delete(user theUser)
{
	string key = theUser.getID();
	int FindNumber;
	FindNumber = UserHash.Find(key);
	UserIdxFout.open("D:\\Trading Platform\\User.idx",ios::in);
	UserIdxFout.seekp(20*FindNumber,ios::beg);
	for(int i = 0; i < 19;i ++)
		UserIdxFout << " ";
	UserIdxFout << endl;
	UserIdxFout.close();
	if( 1 == UserHash.Remove(key))
		return 1;
	else
		return 0;
}


class ProductDataBase//�洢��Ʒ��Ϣ�����ݿ�
{
public:
	ProductDataBase();//�������ݿ��ļ�
	void Find(string key);//ͨ����Ʒ������ĳ��Ʒ�����������
	int Insert(product theProduct);//��dat�ļ��в���ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
	int Delete(product theProduct);//��idx�ļ���ɾ��ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
	int Modify(product theProduct);//��dat�ļ����޸�ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
	void Print();//��Ļ���
private:
	HashTable ProductHash;
	int DataMove;//��¼���һ�����ݵ��ļ�ƫ����
};

ProductDataBase::ProductDataBase():DataMove(0)
{
	HashTable ProductHash;
	ProductDatFout.open("D:\\Trading Platform\\Product.dat");
	ProductIdxFout.open("D:\\Trading Platform\\Product.idx");
	ProductDatFout.close();
	ProductIdxFout.close();
}

void ProductDataBase::Find(string key)
{
	ProductIdxFin.open("D:\\Trading Platform\\Product.idx");
	if(ProductIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		exit(0);
	}
	int FindNumber;
	FindNumber = ProductHash.Find(key);
	ProductIdxFin.seekg(20*FindNumber,ios::beg);
	string temp_1;
	ProductIdxFin >> temp_1;
	string name,dataMove,dataLength;
	string temp_2 = "";
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			else if( colonNumber == 2)
				dataLength = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	int dataMoveNumber = atoi(dataMove.c_str());
	ProductIdxFin.close();
	ProductDatFin.open("D:\\Trading Platform\\Product.dat");
	ProductDatFin.seekg(dataMoveNumber,ios::beg);
	string temp_3;
	ProductDatFin >> temp_3;
	string temp_4 = "";
	int length3 = temp_3.size();
	colonNumber = 0;
	string name2,sort,place,model,factory,date,price,number,score;
	for( int i = 0; i < length3; i ++)
	{
		if( temp_3[i] == ':' )
		{
			if(colonNumber == 0)
				name2 = temp_4;
			else if(colonNumber == 1)
				sort = temp_4;
			else if(colonNumber == 2)
				place = temp_4;
			else if(colonNumber == 3)
				model = temp_4;
			else if(colonNumber == 4)
				factory = temp_4;
			else if(colonNumber == 5)
				date = temp_4;
			else if(colonNumber == 6)
				price = temp_4;
			else if(colonNumber == 7)
				number = temp_4;
			temp_4 = "";
			colonNumber ++;
		}
		else
			temp_4 += temp_3[i];
	}
	string temp_5 = "";
	temp_5 += temp_3[length3-1];
	score = temp_5;
	cout << name2 <<":"<< sort <<":"<< place <<":"<< model <<":"
		<< factory <<":"<< date <<":"<< price <<":"<< number <<":"<< score << endl;
	ProductDatFin.close();
}

int ProductDataBase::Insert(product theProduct)
{
	int FindNumber = ProductHash.FindPos(theProduct.getName());
	if( 0 == ProductHash.Insert(theProduct.getName()))
		return 0;
	ProductIdxFout.open("D:\\Trading Platform\\Product.idx",ios::in|ios::ate);
	ProductIdxFout.seekp((20*FindNumber),ios::beg);//20Ϊ�趨��ÿ��������ռ�ַ�������
	ProductIdxFout << theProduct.getName() << ":" << DataMove << ":" << theProduct.ProductLength();
	string strDataMove;
	ss << DataMove;
	ss >> strDataMove;
	string strProductLength;
	ss << theProduct.ProductLength();
	ss >> strProductLength;
	int IndexSize = theProduct.getName().size() + strDataMove.size() + strProductLength.size() + 2;
	for( int i = 0; i < 18 - IndexSize; i ++)
		ProductIdxFout << " ";
	ProductIdxFout << endl;
	DataMove += theProduct.ProductLength();
	ProductIdxFout.close();
	ProductDatFout.open("D:\\Trading Platform\\Product.dat",ios::app);
	ProductDatFout << theProduct.getName() <<":"<< theProduct.getSort() <<":"<< theProduct.getPlace() <<":"<< theProduct.getModel() <<":"<< theProduct.getFactory() 
		<<":"<< theProduct.getDate() <<":"<< theProduct.getPrice() <<":"<< theProduct.getNumber() <<":"<< theProduct.getScore() << endl;
	ProductDatFout.close();
	return 1;
}

int ProductDataBase::Modify(product theProduct)
{
	string key = theProduct.getName();
	ProductIdxFin.open("D:\\Trading Platform\\Product.idx");
	if(ProductIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		return 0;
	}
	string IndexNumber;
	int FindNumber;
	FindNumber = ProductHash.Find(key);
	ProductIdxFin.seekg(20*FindNumber,ios::beg);
	if( 0 == ProductHash.WasFound())
		return 0;
	string temp_1;
	ProductIdxFin >> temp_1;
	string name,dataMove,dataLength;
	string temp_2;
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			else if( colonNumber == 2)
				dataLength = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	int dataMoveNumber = atoi(dataMove.c_str());
	ProductIdxFin.close();
	ProductDatFout.open("D:\\Trading Platform\\Product.dat",ios::in);
	ProductDatFout.seekp(dataMoveNumber,ios::beg);
	ProductDatFout << theProduct.getName() <<":"<< theProduct.getSort() <<":"<< theProduct.getPlace() <<":"<< theProduct.getModel() <<":"<< theProduct.getFactory() 
		<<":"<< theProduct.getDate() <<":"<< theProduct.getPrice() <<":"<< theProduct.getNumber() <<":"<< theProduct.getScore() << endl;
	ProductDatFout.close();
	return 1;
}

int ProductDataBase::Delete(product theProduct)
{
	string key = theProduct.getName();
	int FindNumber;
	FindNumber = ProductHash.Find(key);
	ProductIdxFout.open("D:\\Trading Platform\\Product.idx",ios::in);
	ProductIdxFout.seekp(20*FindNumber,ios::beg);
	for(int i = 0; i < 19;i ++)
		ProductIdxFout << " ";
	ProductIdxFout << endl;
	ProductIdxFout.close();
	if( 1 == ProductHash.Remove(key))
		return 1;
	else
		return 0;
}

void ProductDataBase::Print()
{
	cout << "��Ʒ��:" << "��Ʒ���:" << "����:" << "�ͺ�:" << "����:" << "��������:" << "����:" << "�������:" << "����:" << endl;
	ProductDatFin.open("D:\\Trading Platform\\Product.dat");
	string oneProduct;
	ProductDatFin >> oneProduct;
	int i = 0;
	string wantToContinue = "y";
	while(!ProductDatFin.eof())
	{
		if( i >= 10 && i%10 == 0 )
		{
			cout << "�Ƿ�����������һҳ�����ǣ�������y,����������n��" << endl;
			cin >> wantToContinue;
			if( "n" == wantToContinue )
				break;
		}
		cout << oneProduct;
		cout << endl;
		ProductDatFin >> oneProduct;
		i ++;
		wantToContinue = "n";
	}
}

class BuyDataBase//�洢������Ʒ��Ϣ�����ݿ�
{
public:
	BuyDataBase();//�������ݿ��ļ�
	void Find(string key);//ͨ���û�ID����������Ϣ
	int Insert(buy theBuy);//��dat�ļ��в���ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
	int Delete(buy theBuy);//��idx�ļ���ɾ��ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
	int Modify(buy theBuy);//��dat�ļ����޸�ĳ��Ʒ���ݣ��ɹ�����1�����򷵻�0
private:
	HashTable BuyHash;
	int DataMove;//��¼���һ�����ݵ��ļ�ƫ����
};

BuyDataBase::BuyDataBase():DataMove(0)
{
	HashTable BuyHash;
	BuyDatFout.open("D:\\Trading Platform\\Buy.dat");
	BuyIdxFout.open("D:\\Trading Platform\\Buy.idx");
	BuyDatFout.close();
	BuyIdxFout.close();
}
void BuyDataBase::Find(string key)
{
	BuyIdxFin.open("D:\\Trading Platform\\Buy.idx");
	if(BuyIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		exit(0);
	}
	string IndexNumber;
	int FindNumber;
	FindNumber = BuyHash.Find(key);
	BuyIdxFin.seekg(20*FindNumber,ios::beg);
	string temp_1;
	BuyIdxFin >> temp_1;
	string name,dataMove,dataLength;
	string temp_2 = "";
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			else if( colonNumber == 2)
				dataLength = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	int dataMoveNumber = atoi(dataMove.c_str());
	BuyIdxFin.close();
	BuyDatFin.open("D:\\Trading Platform\\Buy.dat");
	BuyDatFin.seekg(dataMoveNumber,ios::beg);
	string temp_3;
	BuyDatFin >> temp_3;
	string temp_4 = "";
	int length3 = temp_3.size();
	colonNumber = 0;
	string ID,name2,price,number,date,score;
	for( int i = 0; i < length3; i ++)
	{
		if( temp_3[i] == ':' )
		{
			if(colonNumber == 0)
				ID = temp_4;
			else if(colonNumber == 1)
				name2 = temp_4;
			else if(colonNumber == 2)
				price = temp_4;
			else if(colonNumber == 3)
				number = temp_4;
			else if(colonNumber == 4)
				date = temp_4;
			else if(colonNumber == 5)
				score = temp_4;
			temp_4 = "";
			colonNumber ++;
		}
		else
			temp_4 += temp_3[i];
	}
	cout << name2 <<":"<< price <<":"<< number <<":"<< date <<":"<< score <<endl;
	BuyDatFin.close();
}

int BuyDataBase::Insert(buy theBuy)
{
	int FindNumber = BuyHash.FindPos(theBuy.getID());
	if( 0 == BuyHash.Insert(theBuy.getID()))
		return 0;

	BuyIdxFout.open("D:\\Trading Platform\\Buy.idx",ios::in|ios::ate);
	BuyIdxFout.seekp(20*FindNumber,ios::beg);//20Ϊ�趨��ÿ��������ռ�ַ�������
	BuyIdxFout << theBuy.getID() << ":" << DataMove << ":" << theBuy.BuyLength();
	string strDataMove;
	ss << DataMove;
	ss >> strDataMove;
	string strBuyLength;
	ss << theBuy.BuyLength();
	ss >> strBuyLength;
	int IndexSize = theBuy.getID().size() + strDataMove.size() + strBuyLength.size() + 3;
	for( int i = 0; i < 18 - IndexSize; i ++)
		BuyIdxFout << " ";
	BuyIdxFout << endl;
	DataMove += theBuy.BuyLength();
	BuyIdxFout.close();
	BuyDatFout.open("D:\\Trading Platform\\Buy.dat",ios::app);
	BuyDatFout << theBuy.getID() <<":"<< theBuy.getName() <<":"<< theBuy.getPrice() <<":"<< theBuy.getNumber() 
		<<":"<< theBuy.getDate() <<":"<< theBuy.getScore() <<endl;
	BuyDatFout.close();
	return 1;
}

int BuyDataBase::Modify(buy theBuy)
{
	string key = theBuy.getName();
	BuyIdxFin.open("D:\\Trading Platform\\Buy.idx");
	if(BuyIdxFin.fail())
	{
		cout << "�û������ļ��򿪳���" << endl;
		return 0;
	}
	string IndexNumber;
	int FindNumber;
	FindNumber = BuyHash.Find(key);
	BuyIdxFin.seekg(20*FindNumber,ios::beg);
	if( 0 == BuyHash.WasFound())
		return 0;
	string temp_1;
	BuyIdxFin >> temp_1;
	string name,dataMove,dataLength;
	string temp_2;
	int colonNumber = 0;
	int length = temp_1.size();
	for( int i = 0; i < length; i ++)
	{
		if( temp_1[i] == ':')
		{
			if( colonNumber == 0)
				name = temp_2;
			else if( colonNumber == 1)
				dataMove = temp_2;
			else if( colonNumber == 2)
				dataLength = temp_2;
			temp_2 = "";
			colonNumber ++;
		}
		else
			temp_2 += temp_1[i];
	}
	int dataMoveNumber = atoi(dataMove.c_str());
	BuyIdxFin.close();
	BuyDatFout.open("D:\\Trading Platform\\Buy.dat",ios::in);
	BuyDatFout.seekp(dataMoveNumber,ios::beg);
	BuyDatFout << theBuy.getID() <<":"<< theBuy.getName() <<":"<< theBuy.getPrice() <<":"<< theBuy.getNumber() 
		<<":"<< theBuy.getDate() <<":"<< theBuy.getScore() <<endl;
	BuyDatFout.close();
	return 1;
}

int BuyDataBase::Delete(buy theBuy)
{
	string key = theBuy.getName();
	int FindNumber;
	FindNumber = BuyHash.Find(key);
	BuyIdxFout.open("D:\\Trading Platform\\Buy.idx",ios::in|ios::ate);
	BuyIdxFout.seekp(20*FindNumber,ios::beg);
	for(int i = 0; i < 19;i ++)
		BuyIdxFout << " ";
	BuyIdxFout << endl;
	BuyIdxFout.close();
	if(1 == BuyHash.Remove(key))
		return 1;
	else
		return 0;
}
#endif
