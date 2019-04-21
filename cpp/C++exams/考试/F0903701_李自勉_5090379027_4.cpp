//F0903701 5090379027 李自勉
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
ifstream fin;

struct OsAccount
{
	string name;
	string passwd;
	string UID;
	string GID;
	string homeDirectory;
	string shell;
};

int main( )
{
	string user,number;
	OsAccount account;
	cout << "INPUT: Name of a password file." << endl
		 << "USAGE:" << endl
		 << "$ exercise4 passwd.file" << endl;
	
	fin.open("D:\$ exercise4 passwd.file.txt");
	if( fin.fail( ))
	{
		cout << "The file doesn't exist!";
		exit(1);
	}
	//用vector读入并存储文件中所有的数据
	vector<string> text;
	char next;
	fin.get(next);
	while( !fin.fail( ))
	{
		string temp;
		temp.insert(temp.begin(),next);
		text.push_back(temp);
		fin.get(next);
	}
	fin.close();
	while(cin)
	{
		cout << "Please enter user name or user ID:";
		cin >> user >> number;
		vector<string>::iterator p = text.begin( );
		string file;
		int sizef;
		int e = 0;
		while( p != text.end( ))
		{
			file = "";
			for( ;*p != "\n" && p < text.end( ) - 1 ; p++)
				file = file + *p;
			sizef = file.size( );
			//将每行的数据分别赋值给结构内的每一数据，再逐个进行条件比较
			if( sizef == 76)
			{
				account.name = file.substr(0,5);
				account.passwd = file.substr(6,34);
				account.UID = file.substr(41,3);
				account.GID = file.substr(45,3);
				account.homeDirectory = file.substr(50,16);
				account.shell = file.substr(67,9);
			}
			else
			{
				account.name = file.substr(0,5);
				account.passwd = file.substr(6,34);
				account.UID = file.substr(41,3);
				account.GID = file.substr(45,3);
				account.homeDirectory = file.substr(50,20);
				account.shell = file.substr(71,9);
			}
			if( user[0] == 'n')
			{
				if( number == account.name)
				{
					cout << number 
						 << ":encrypted password is " 
						<< (char)34 << account.passwd << (char)34
						 << ",UID " << account.UID
						 << ",GID " << account.GID
						 << ",Home " << account.homeDirectory
						 << ",Shell " << account.shell <<"."
						 << endl;
					e = 1;
					break;
					//找到相应数据就直接跳出循环
				}

			}
			else if( user[0] == 'U'||'u')
			{
				if( number == account.UID)
				{
					cout << user << " " << number
						 << ": user name is "
						 << account.name << ","
						 << ":encrypted password is " 
						 << (char)34 << account.passwd << (char)34
						 << ",GID " << account.GID
						 << ",Home " << account.homeDirectory
						 << ",Shell " << account.shell <<"."
						 << endl;
					e = 1;
					break;
				}

			}
			p++;
		}
		if( e == 0)
		{
			if( user[0] == 'n')
				cout << number << " doesn't exist." << endl;
			else if( user[0] == 'U'||'u')
				cout << user << " " << number << " is not used." << endl;
		}
	}
	return 0;
}











	