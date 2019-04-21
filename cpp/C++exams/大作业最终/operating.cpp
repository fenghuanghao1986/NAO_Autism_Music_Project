#include<iostream>
#include<string>
#include<list>
#include<ctime>
#include"database.h"
#include"user.h"
#include"product.h"
#include"buy.h"
#define createSize 5
using namespace std;

user Admin("Zerma","aaaaa","bbbbb","ccccc","ddddd","eeeee","fffff","ggggg","1");//���õ�һ������Ա�˺�
int choice_1,choice_2,choice_3,choice_4;
string ID,cipher;
string wantToContinue = "y";
int out_1 = 0;
int out_2 = 0;
user theUser;
UserDataBase UserDB;
ProductDataBase ProductDB;
BuyDataBase BuyDB;
void log()
{
	cout << "��ӭ��½���Ͻ���ƽ̨��" << endl;
	cout << "0--��¼" << endl
		 << "1--ע��" << endl
		 << "2--�˳�" << endl;
	cin >> choice_1;
	system("cls");
	if( 0 == choice_1 )
	{
		cout << "�����������û�����";
		cin >> ID;
		cout << "�������������룺";
		cin >> cipher;
		theUser.set(ID,cipher,"","","","","","","");
		out_2 = 0;
		if( 0 == UserDB.Find(theUser))
		{
			cout << "�û������������" << endl;
			exit(0);
		}
	}
	else if( 1 == choice_1 )
	{
		int isUsed = 1;
		while( 1 == isUsed )
		{
			cout << "�����������û�����";
			cin >> ID;
			isUsed = 0;
			if( 1 == UserDB.FindID(ID))
				isUsed = 1;
			if( 1 == isUsed )
				cout << "�û����ѱ�ʹ�ã�������û���" << endl;
		}
		cout << "�������������룺";
		cin >> cipher;
		string tempCipher = "";
		int isSame = 0;
		while( 0 == isSame)
		{
			if( cipher == tempCipher)
				isSame = 1;
			else
			{
				cout << "��ȷ���������룺";
				cin >> tempCipher;
			}
		}
		theUser.set(ID,cipher,"","","","","","","0");
		if( 0 == UserDB.Insert(theUser))
			exit(0);
		out_2 = 0;
		cout << "��ϲ���ѳɹ�ע�ᣡ" << endl;
	}
	else if( 2 == choice_1)
		exit(0);
}
void options()
{
	if( (1 == choice_1)||( 0 == choice_1 && "0" == theUser.getIsAdmin()) )
	{
		cout << "0--�޸�ע����Ϣ" << endl
			<< "1--�����Ʒ" << endl
			<< "2--������Ʒ" << endl
			<< "3--���������Ʒ" << endl
			<< "4--�˳�" << endl;
	}
	else if( 0 == choice_1 && "1" == theUser.getIsAdmin())
	{
		cout << "0--�޸�ע����Ϣ" << endl
			<< "1--�����Ʒ" << endl
			<< "2--������Ʒ" << endl
			<< "3--���������Ʒ" << endl
			<< "4--�˳�" << endl
			<< "5--�޸���Ʒ��Ϣ������ԱȨ�ޣ�" << endl
			<< "6--�޸��û���Ϣ������ԱȨ�ޣ�" << endl;
	}
}
void changeInformation()
{
	cout << "��ѡ����Ҫ�޸ĵ���Ϣ��" << endl
		<< "1--����" << endl
		<< "2--����" << endl
		<< "3--����" << endl
		<< "4--��ַ" << endl
		<< "5--�绰" << endl
		<< "6--��Ȥ����" << endl;
	cin >> choice_3;
	string tempInput;
	cout << endl;
	cout << "�������޸ĺ�����ݣ�";
	cin >> tempInput;
	switch (choice_3)
	{
	case 1:
		theUser.changeCipher(tempInput);
		break;
	case 2:
		theUser.changeName(tempInput);
		break;
	case 3:
		theUser.changeAge(tempInput);
		break;
	case 4:
		theUser.changeAddress(tempInput);
		break;
	case 5:
		theUser.changePhone(tempInput);
		break;
	case 6:
		theUser.changeInterest(tempInput);
		break;
	}
	if( 0 == UserDB.Modify(theUser))
		exit(0);
	cout << endl;
}
void browseByWord()
{
	string tempInput;
	cout << "���������Ĺؼ���(��Ʒ������";
	cin >> tempInput;
	cout << "��Ʒ��:" << "��Ʒ���:" << "����:" << "�ͺ�:" << "����:" << "��������:" << "����:" << "�������:" << "����:" << endl;
	ProductDB.Find(tempInput);
}

void buyProduct()
{
	string tempInput;
	cout << "���������Ĺؼ���(��Ʒ������";
	cin >> tempInput;
	cout << "��Ʒ��:" << "��Ʒ���:" << "����:" << "�ͺ�:" << "����:" << "��������:" << "����:" << "�������:" << "����:" << endl;
	ProductDB.Find(tempInput);
	string buyID,buyName,buyPrice,buyNumber,buyDate,buyScore;
	cout << "��������ȷ��Ҫ��������Ʒ����Ϣ���ύ����" << endl;
	cout << "��Ʒ����";
	cin >> buyName;
	cout << "���ۣ�";
	cin >> buyPrice;
	cout << "����������";
	cin >> buyNumber;
	cout << "�������ڣ�";
	cin >> buyDate;
	buyScore = "0";
	buyID = theUser.getID();
	buy newBuy(buyID,buyName,buyPrice,buyNumber,buyDate,buyScore);
	BuyDB.Insert(newBuy);
	cout << "�������Ƿ������������������Ҫ��������y����������n��" << endl;
	cin >> wantToContinue;
}


void buyOperate()
{
	cout << "��Ʒ��\t" << "����\t" << "����\t" << "��������\t" << "����\t" << endl;
	BuyDB.Find(theUser.getID());
	cout << "��ѡ����Ҫ���еĲ�����" << endl;
	cout << "0--�˶���Ʒ" << endl
		<< "1--�޸Ķ�����Ʒ������" << endl
		<< "2--����Ʒ����" << endl;
	cin >> choice_3;
	string tempInput;
	if( 0 == choice_3)
	{
		cout << "�����������˶�����Ʒ��" ;
		cin >> tempInput;
		buy theBuy("",tempInput,"","","","");
		BuyDB.Delete(theBuy);
	}
	else if( 1 == choice_3)
	{
		string newNumber;
		cout << "�����������޸ĵ���Ʒ��";
		cin >> tempInput;
		cout << "�����������޸ĵ�������";
		cin >> newNumber;
		buy theBuy(theUser.getID(),tempInput,"",newNumber,"","");
		BuyDB.Modify(theBuy);
	}
	else if( 2 == choice_3)
	{
		string newScore;
		cout << "�������������ֵ���Ʒ��";
		cin >> tempInput;
		cout << "�������������֣�0-9����";
		cin >> newScore;
		buy theBuy(theUser.getID(),tempInput,"","","",newScore);
		BuyDB.Modify(theBuy);
	}
}

void AdminProduct()
{
	cout << "��ѡ���������Ʒ���еĲ�����"<<endl
		<< "0--������Ʒ" << endl
		<< "1--ɾ����Ʒ" << endl
		<< "2--�޸���Ʒ��Ϣ" << endl;
	cin >> choice_3;
	string name,sort,place,model,factory,date,price,number,score;
	if( 0 == choice_3)
	{
		cout << "������������Ʒ��Ϣ" << endl;
		cout << "��Ʒ����";
		cin >> name;
		cout << "��Ʒ���";
		cin >> sort;
		cout << "���أ�";
		cin >> place;
		cout << "�ͺţ�";
		cin >> model;
		cout << "���ң�";
		cin >> factory;
		cout << "�������ڣ�";
		cin >> date;
		cout << "���ۣ�";
		cin >> price;
		cout << "���������";
		cin >> number;
		score = "NULL";
		product newProduct(name,sort,place,model,factory,date,price,number,score);
		ProductDB.Insert(newProduct);
	}
	if( 2 == choice_3 )
	{
		cout << "��������Ҫ�޸ĵ���Ʒ����";
		cin >> name;
		cout << "������Ҫ�޸ĵ���Ϣ"
			<< "��Ʒ���";
		cin >> sort;
		cout << "���أ�";
		cin >> place;
		cout << "�ͺţ�";
		cin >> model;
		cout << "���ң�";
		cin >> factory;
		cout << "�������ڣ�";
		cin >> date;
		cout << "���ۣ�";
		cin >> price;
		cout << "���������";
		cin >> number;
		cout << "���֣�";
		cin >> score;
		product newProduct(name,sort,place,model,factory,date,price,number,score);
		ProductDB.Modify(newProduct);
	}
	if( 1 == choice_3 )
	{
		cout << "��������Ҫɾ������Ʒ�������Ϣ" << endl;
		cout << "��Ʒ����";
		cin >> name;
		cout << "��Ʒ���";
		cin >> sort;
		cout << "���أ�";
		cin >> place;
		cout << "�ͺţ�";
		cin >> model;
		cout << "���ң�";
		cin >> factory;
		product theProduct(name,sort,place,model,factory,"","","","");
		ProductDB.Delete(theProduct);
	}
}
void AdminUser()
{
	cout << "��ѡ����Ҫ���û����еĲ���" << endl
		<< "0--����û�" << endl
		<< "1--ɾ���û�" << endl
		<< "2--�޸��û���Ϣ" << endl;
	cin >> choice_3;
	string ID,cipher,name,sex,age,address,phone,interest,judgeAdmin,isAdmin;
	if( 0 == choice_3)
	{
		cout << "�����������û���Ϣ" << endl;
		cout << "�˺ţ�";
		cin >> ID;
		cout << "���룺";
		cin >> cipher;
		cout << "������";
		cin >> name;
		cout << "�Ա�";
		cin >> sex;
		cout << "���䣺";
		cin >> age;
		cout << "��ַ��";
		cin >> address;
		cout << "�绰��";
		cin >> phone;
		cout << "��Ȥ���ã�";
		cin >> interest;
		cout << "����ԱȨ�ޣ�y/n����";
		cin >> judgeAdmin;
		if( "y" == judgeAdmin )
			isAdmin = "1";
		else
			isAdmin = "0";
		user newUser(ID,cipher,name,sex,age,address,phone,interest,isAdmin);
		UserDB.Insert(newUser);
	}
	else if( 1 == choice_3)
	{
		cout << "������ɾ���û��������Ϣ" << endl;
		cout << "�˺ţ�";
		cin >> ID;
		user theUser(ID,"","","","","","","","");
		UserDB.Delete(theUser);
	}
	else if( 2 == choice_3)
	{
		cout << "�������޸��û��������Ϣ" << endl;
		cout << "�˺ţ�";
		cin >> ID;
		cout << "������Ҫ�޸ĵ��û���Ϣ" << endl;
		cout << "���룺";
		cin >> cipher;
		cout << "������";
		cin >> name;
		cout << "�Ա�";
		cin >> sex;
		cout << "���䣺";
		cin >> age;
		cout << "��ַ��";
		cin >> address;
		cout << "�绰��";
		cin >> phone;
		cout << "��Ȥ���ã�";
		cin >> interest;
		cout << "����ԱȨ�ޣ�y/n����";
		cin >> judgeAdmin;
		if( "y" == judgeAdmin )
			isAdmin = "1";
		else
			isAdmin = "0";
		user theUser(ID,cipher,name,sex,age,address,phone,interest,isAdmin);
		UserDB.Modify(theUser);
	}
}

void CreateUser()
{
	string ID,cipher,name,sex,age,address,phone,interest;
	for(int i = 0; i < createSize; i ++)
	{
		ID = "";
		cipher = "";
		name = "";
		sex = "";
		age = "";
		address = "";
		phone = "";
		interest = "";
		for( int j = 0; j < 5; j ++)
		{
			ID = ID + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			cipher = cipher + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			name = name + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			sex = sex + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			age = age + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			address = address + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			phone = phone + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			interest = interest + (char)(97+rand()%26);
		}
		user newUser(ID,cipher,name,sex,age,address,phone,interest,"0");
		if(0 ==UserDB.Insert(newUser))
			cout << "�������ݲ������" << endl;
	}
}
void CreateProduct()
{
	string name,sort,place,model,factory,date,price,number,score;
	for(int i = 0; i < createSize; i ++)
	{
		name = "";
		sort = "";
		place = "";
		model = "";
		factory = "";
		date = "";
		price = "";
		number = "";
		score = "";
		for( int j = 0; j < 5; j ++)
		{
			name = name + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			sort = sort + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			place = place + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			model = model + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			factory = factory + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			date = date + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			price = price + (char)(97+rand()%26);
		}
		for( int j = 0; j < 5; j ++)
		{
			number = number + (char)(97+rand()%26);
		}
		score = (char)(48+rand()%10);
		product newProduct(name,sort,place,model,factory,date,price,number,score);
		if(0 == ProductDB.Insert(newProduct))
			cout << "�������ݲ������" << endl;
	}
}
int main()
{
	cout << "���ڴ����������ݣ������ĵȴ�" << endl;
	clock_t t = clock();
	CreateUser();
	CreateProduct();
	t = clock() - t;
	system("cls");
	cout << "��������������ʱ��Ϊ" << (double)t/CLOCKS_PER_SEC << "��" << endl;
	UserDB.Insert(Admin);
	while( out_2 == 0 )
	{
		log();
		while( 0 == out_1)
		{
			system("cls");
			options();
			cin >> choice_2;
			system("cls");
			wantToContinue = "y";
			if( 0 == choice_2 )
			{
				while( "y" == wantToContinue )
				{
					theUser.output();
					cout << endl;
					while( "y" == wantToContinue)
					{
						changeInformation();
						cout << "�������޸��Ժ����Ϣ��" << endl;
						theUser.output();
						cout << "��������޸��𣿣�y/n��" << endl;
						cin >> wantToContinue;
					}
				}
			}
			else if( 1 == choice_2 )
			{
				while( "y" == wantToContinue )
				{
					cout << "��ѡ�������ʽ��" << endl
						<< "0--ȫ�����" << endl
						<< "1--���������" << endl;
					cin >> choice_3;
					system("cls");
					if( 0 == choice_3)
						ProductDB.Print();
					else if( 1 == choice_3 )
						browseByWord();
					cout << "������������(y/n)" << endl;
					cin >> wantToContinue;
				}
			}
			else if( 2 == choice_2 )
			{
				while( "y" == wantToContinue )
					buyProduct();
			}
			else if( 3 == choice_2)
			{
				while( "y" == wantToContinue )
				{
					buyOperate();
					cout << "������������𣿣�y/n��" << endl;
					cin >> wantToContinue;
				}
			}
			else if( 4 == choice_2 )
				out_1 = 1;
			else if( 5 == choice_2 && "1" == theUser.getIsAdmin())
			{
				while( "y" == wantToContinue)
				{
					AdminProduct();
					cout << "������������𣿣�y/n��" << endl;
					cin >> wantToContinue;
				}
			}
			else if( 6 == choice_2 && "1" == theUser.getIsAdmin())
			{
				while( "y" == wantToContinue)
				{
					AdminUser();
					cout << "������������𣿣�y/n��" << endl;
					cin >> wantToContinue;
				}
			}
		}
	}
	return 0;
}		


