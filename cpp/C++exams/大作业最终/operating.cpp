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

user Admin("Zerma","aaaaa","bbbbb","ccccc","ddddd","eeeee","fffff","ggggg","1");//内置的一个管理员账号
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
	cout << "欢迎登陆掌上交易平台！" << endl;
	cout << "0--登录" << endl
		 << "1--注册" << endl
		 << "2--退出" << endl;
	cin >> choice_1;
	system("cls");
	if( 0 == choice_1 )
	{
		cout << "请输入您的用户名：";
		cin >> ID;
		cout << "请输入您的密码：";
		cin >> cipher;
		theUser.set(ID,cipher,"","","","","","","");
		out_2 = 0;
		if( 0 == UserDB.Find(theUser))
		{
			cout << "用户名或密码错误" << endl;
			exit(0);
		}
	}
	else if( 1 == choice_1 )
	{
		int isUsed = 1;
		while( 1 == isUsed )
		{
			cout << "请输入您的用户名：";
			cin >> ID;
			isUsed = 0;
			if( 1 == UserDB.FindID(ID))
				isUsed = 1;
			if( 1 == isUsed )
				cout << "用户名已被使用，请更换用户名" << endl;
		}
		cout << "请输入您的密码：";
		cin >> cipher;
		string tempCipher = "";
		int isSame = 0;
		while( 0 == isSame)
		{
			if( cipher == tempCipher)
				isSame = 1;
			else
			{
				cout << "请确认您的密码：";
				cin >> tempCipher;
			}
		}
		theUser.set(ID,cipher,"","","","","","","0");
		if( 0 == UserDB.Insert(theUser))
			exit(0);
		out_2 = 0;
		cout << "恭喜您已成功注册！" << endl;
	}
	else if( 2 == choice_1)
		exit(0);
}
void options()
{
	if( (1 == choice_1)||( 0 == choice_1 && "0" == theUser.getIsAdmin()) )
	{
		cout << "0--修改注册信息" << endl
			<< "1--浏览商品" << endl
			<< "2--订购商品" << endl
			<< "3--浏览订购商品" << endl
			<< "4--退出" << endl;
	}
	else if( 0 == choice_1 && "1" == theUser.getIsAdmin())
	{
		cout << "0--修改注册信息" << endl
			<< "1--浏览商品" << endl
			<< "2--订购商品" << endl
			<< "3--浏览订购商品" << endl
			<< "4--退出" << endl
			<< "5--修改商品信息（管理员权限）" << endl
			<< "6--修改用户信息（管理员权限）" << endl;
	}
}
void changeInformation()
{
	cout << "请选择您要修改的信息：" << endl
		<< "1--密码" << endl
		<< "2--姓名" << endl
		<< "3--年龄" << endl
		<< "4--地址" << endl
		<< "5--电话" << endl
		<< "6--兴趣爱好" << endl;
	cin >> choice_3;
	string tempInput;
	cout << endl;
	cout << "请输入修改后的内容：";
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
	cout << "请输入您的关键词(商品名）：";
	cin >> tempInput;
	cout << "商品名:" << "商品类别:" << "产地:" << "型号:" << "厂家:" << "生产日期:" << "单价:" << "库存数量:" << "评分:" << endl;
	ProductDB.Find(tempInput);
}

void buyProduct()
{
	string tempInput;
	cout << "请输入您的关键词(商品名）：";
	cin >> tempInput;
	cout << "商品名:" << "商品类别:" << "产地:" << "型号:" << "厂家:" << "生产日期:" << "单价:" << "库存数量:" << "评分:" << endl;
	ProductDB.Find(tempInput);
	string buyID,buyName,buyPrice,buyNumber,buyDate,buyScore;
	cout << "请输入你确认要订购的商品的信息以提交订单" << endl;
	cout << "商品名：";
	cin >> buyName;
	cout << "单价：";
	cin >> buyPrice;
	cout << "订购数量：";
	cin >> buyNumber;
	cout << "订购日期：";
	cin >> buyDate;
	buyScore = "0";
	buyID = theUser.getID();
	buy newBuy(buyID,buyName,buyPrice,buyNumber,buyDate,buyScore);
	BuyDB.Insert(newBuy);
	cout << "请问您是否还想继续订购？（若需要，请输入y，否则输入n）" << endl;
	cin >> wantToContinue;
}


void buyOperate()
{
	cout << "商品名\t" << "单价\t" << "数量\t" << "订购日期\t" << "评分\t" << endl;
	BuyDB.Find(theUser.getID());
	cout << "请选择想要进行的操作：" << endl;
	cout << "0--退订商品" << endl
		<< "1--修改订购商品的数量" << endl
		<< "2--给商品评分" << endl;
	cin >> choice_3;
	string tempInput;
	if( 0 == choice_3)
	{
		cout << "请输入您想退订的商品：" ;
		cin >> tempInput;
		buy theBuy("",tempInput,"","","","");
		BuyDB.Delete(theBuy);
	}
	else if( 1 == choice_3)
	{
		string newNumber;
		cout << "请输入您想修改的商品：";
		cin >> tempInput;
		cout << "请输入您想修改的数量：";
		cin >> newNumber;
		buy theBuy(theUser.getID(),tempInput,"",newNumber,"","");
		BuyDB.Modify(theBuy);
	}
	else if( 2 == choice_3)
	{
		string newScore;
		cout << "请输入您想评分的商品：";
		cin >> tempInput;
		cout << "请输入您的评分（0-9）：";
		cin >> newScore;
		buy theBuy(theUser.getID(),tempInput,"","","",newScore);
		BuyDB.Modify(theBuy);
	}
}

void AdminProduct()
{
	cout << "请选择您想对商品进行的操作："<<endl
		<< "0--增加商品" << endl
		<< "1--删除商品" << endl
		<< "2--修改商品信息" << endl;
	cin >> choice_3;
	string name,sort,place,model,factory,date,price,number,score;
	if( 0 == choice_3)
	{
		cout << "请输入下列商品信息" << endl;
		cout << "商品名：";
		cin >> name;
		cout << "商品类别：";
		cin >> sort;
		cout << "产地：";
		cin >> place;
		cout << "型号：";
		cin >> model;
		cout << "厂家：";
		cin >> factory;
		cout << "生产日期：";
		cin >> date;
		cout << "单价：";
		cin >> price;
		cout << "库存数量：";
		cin >> number;
		score = "NULL";
		product newProduct(name,sort,place,model,factory,date,price,number,score);
		ProductDB.Insert(newProduct);
	}
	if( 2 == choice_3 )
	{
		cout << "请输入想要修改的商品名：";
		cin >> name;
		cout << "请输入要修改的信息"
			<< "商品类别：";
		cin >> sort;
		cout << "产地：";
		cin >> place;
		cout << "型号：";
		cin >> model;
		cout << "厂家：";
		cin >> factory;
		cout << "生产日期：";
		cin >> date;
		cout << "单价：";
		cin >> price;
		cout << "库存数量：";
		cin >> number;
		cout << "评分：";
		cin >> score;
		product newProduct(name,sort,place,model,factory,date,price,number,score);
		ProductDB.Modify(newProduct);
	}
	if( 1 == choice_3 )
	{
		cout << "请输入想要删除的商品的相关信息" << endl;
		cout << "商品名：";
		cin >> name;
		cout << "商品类别：";
		cin >> sort;
		cout << "产地：";
		cin >> place;
		cout << "型号：";
		cin >> model;
		cout << "厂家：";
		cin >> factory;
		product theProduct(name,sort,place,model,factory,"","","","");
		ProductDB.Delete(theProduct);
	}
}
void AdminUser()
{
	cout << "请选择您要对用户进行的操作" << endl
		<< "0--添加用户" << endl
		<< "1--删除用户" << endl
		<< "2--修改用户信息" << endl;
	cin >> choice_3;
	string ID,cipher,name,sex,age,address,phone,interest,judgeAdmin,isAdmin;
	if( 0 == choice_3)
	{
		cout << "请输入下列用户信息" << endl;
		cout << "账号：";
		cin >> ID;
		cout << "密码：";
		cin >> cipher;
		cout << "姓名：";
		cin >> name;
		cout << "性别：";
		cin >> sex;
		cout << "年龄：";
		cin >> age;
		cout << "地址：";
		cin >> address;
		cout << "电话：";
		cin >> phone;
		cout << "兴趣爱好：";
		cin >> interest;
		cout << "管理员权限（y/n）：";
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
		cout << "请输入删除用户的相关信息" << endl;
		cout << "账号：";
		cin >> ID;
		user theUser(ID,"","","","","","","","");
		UserDB.Delete(theUser);
	}
	else if( 2 == choice_3)
	{
		cout << "请输入修改用户的相关信息" << endl;
		cout << "账号：";
		cin >> ID;
		cout << "请输入要修改的用户信息" << endl;
		cout << "密码：";
		cin >> cipher;
		cout << "姓名：";
		cin >> name;
		cout << "性别：";
		cin >> sex;
		cout << "年龄：";
		cin >> age;
		cout << "地址：";
		cin >> address;
		cout << "电话：";
		cin >> phone;
		cout << "兴趣爱好：";
		cin >> interest;
		cout << "管理员权限（y/n）：";
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
			cout << "生成数据插入出错" << endl;
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
			cout << "生成数据插入出错" << endl;
	}
}
int main()
{
	cout << "正在创建测试数据，请耐心等待" << endl;
	clock_t t = clock();
	CreateUser();
	CreateProduct();
	t = clock() - t;
	system("cls");
	cout << "生成数据所花费时间为" << (double)t/CLOCKS_PER_SEC << "秒" << endl;
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
						cout << "以下是修改以后的信息：" << endl;
						theUser.output();
						cout << "还想继续修改吗？（y/n）" << endl;
						cin >> wantToContinue;
					}
				}
			}
			else if( 1 == choice_2 )
			{
				while( "y" == wantToContinue )
				{
					cout << "请选择浏览方式：" << endl
						<< "0--全部浏览" << endl
						<< "1--按属性浏览" << endl;
					cin >> choice_3;
					system("cls");
					if( 0 == choice_3)
						ProductDB.Print();
					else if( 1 == choice_3 )
						browseByWord();
					cout << "还想继续浏览吗？(y/n)" << endl;
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
					cout << "还想继续操作吗？（y/n）" << endl;
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
					cout << "还想继续操作吗？（y/n）" << endl;
					cin >> wantToContinue;
				}
			}
			else if( 6 == choice_2 && "1" == theUser.getIsAdmin())
			{
				while( "y" == wantToContinue)
				{
					AdminUser();
					cout << "还想继续操作吗？（y/n）" << endl;
					cin >> wantToContinue;
				}
			}
		}
	}
	return 0;
}		


