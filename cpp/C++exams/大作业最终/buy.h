#ifndef BUY_H
#define BUY_H
#include<iostream>
#include<string>
#include<sstream>
using namespace std;

class user;
class buy
{
	friend class user;
private:
	string ID;//用户名
	string name;//商品名
	string price;//单价
	string number;//数量
	string date;//订购日期
	string score;//评分
public:
	buy(string ID,string name,string price,string number,string date,string score)
		:ID(ID),name(name),price(price),number(number),date(date),score(score){}
	void output();
	string getName(){return name;}
	string getID(){return ID;}
	string getPrice(){return price;}
	string getNumber(){return number;}
	string getDate(){return number;}
	string getScore(){return score;}
	int BuyLength();
	void changeNumber(string newNumber){number = newNumber;}
	void changeScore(string newScore){score = newScore;}
};

int buy::BuyLength()
{
	int IDLength = ID.size();
	int NameLength = name.size();
	int PriceLength = price.size();
	int NumberLength = number.size();
	int DateLength = date.size();
	int ScoreLength = score.size();
	int intLength = IDLength + NameLength + PriceLength + NumberLength + DateLength + ScoreLength + 8;
	return intLength;
}
void buy::output()
{
	cout<< name << "\t"
		<< price << "\t"
		<< number << "\t"
		<< date << "\t"
		<< score << "\t"
		<<endl;
}
#endif