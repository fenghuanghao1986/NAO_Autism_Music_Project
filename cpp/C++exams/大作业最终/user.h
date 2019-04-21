#ifndef USER_H
#define USER_H
#include<string>
#include<iostream>
#include<sstream>
using namespace std;

class user
{
private:
	string ID;//用户名
	string cipher;//密码
	string name;//姓名
	string sex;//性别
	string age;//年龄
	string address;//地址
	string phone;//电话
	string interest;//兴趣爱好
	string isAdmin;
public:
	user(string ID,string cipher,string name,string sex,string age,string address,string phone,string interest,string isAdmin)
		:ID(ID),cipher(cipher),name(name),sex(sex),age(age),address(address),phone(phone),interest(interest),isAdmin(isAdmin){}
	user():ID(""),cipher(""),name(""),sex(""),age(""),address(""),phone(""),interest(""),isAdmin(""){}
	void set(string ID,string cipher,string name,string sex,string age,string address,string phone,string interest,string isAdmin);
	string getID(){return ID;}
	string getCipher(){return cipher;}
	string getName(){return name;}
	string getSex(){return sex;}
	string getAge(){return age;}
	string getAddress(){return address;}
	string getPhone(){return phone;}
	string getInterest(){return interest;}
	string getIsAdmin(){return isAdmin;}
	int UserLength();//返回各项属性的字符串长度之和
	void changeID(string newID){ID = newID;}
	void changeCipher( string newCipher){cipher = newCipher;}
	void changeName(string newName){name = newName;}
	void changeSex(string newSex){sex = newSex;}
	void changeAge(string newAge){age = newAge;}
	void changeAddress(string newAddress){address = newAddress;}
	void changePhone(string newPhone){phone = newPhone;}
	void changeInterest(string newInterest){interest = newInterest;}
	void changeIsAdmin(string newIsAdmin){isAdmin = newIsAdmin;}
	void output();
};
void user::set(string aID,string acipher,string aname,string asex,string aage,string aaddress,string aphone,string ainterest,string aisAdmin)
{
		ID = aID;
		cipher = acipher;
		name = aname;
		sex = asex;
		age = aage;
		address = aaddress;
		phone = aphone;
		interest = ainterest;
		isAdmin = aisAdmin;
}
void user::output()
{
	cout << "用户名：" << ID << endl
		<< "密码：" << cipher << endl
		<< "姓名：" << name << endl
		<< "性别：" << sex << endl
		<< "年龄：" << age << endl
		<< "地址：" << address << endl
		<< "电话：" << phone << endl
		<< "兴趣爱好：" << interest << endl;
}

int user::UserLength()
{
	int IDLength = ID.size();
	int cipherLength = cipher.size();
	int nameLength = name.size();
	int sexLength = sex.size();
	int ageLength = age.size();
	int addressLength = address.size();
	int phoneLength = phone.size();
	int interestLength = interest.size();
	int isAdminLength = isAdmin.size();
	int intLength = IDLength + cipherLength + nameLength + sexLength + ageLength + addressLength + phoneLength + interestLength +isAdminLength + 10;
	return intLength;
}

#endif