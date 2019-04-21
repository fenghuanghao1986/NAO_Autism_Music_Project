#ifndef PRODUCT_H
#define PRODUCT_H
#include <iostream>
#include <string>
#include<sstream>
using namespace std;

class product
{
private:
	string name;//��Ʒ��
	string sort;//��Ʒ���
	string place;//����
	string model;//�ͺ�
	string factory;//����
	string date;//��������
	string price;//����
	string number;//�������
	string score;//��Ʒ����
public:
	product(string name,string sort,string place,string model,string factory,string date,string price,string number,string score)
		:name(name),sort(sort),place(place),model(model),factory(factory),date(date),price(price),number(number),score(score){}
	string getName(){return name;}
	string getSort(){return sort;}
	string getPlace(){return place;}
	string getModel(){return model;}
	string getFactory(){return factory;}
	string getDate(){return date;}
	string getPrice(){return price;}
	string getNumber(){return number;}
	string getScore(){return score;}
	int ProductLength();//���ظ������Ե��ַ�������֮��
	void changeName(string newName){name = newName;}
	void changeSort(string newSort){sort = newSort;}
	void changePlace(string newPlace){place = newPlace;}
	void changeModel(string newModel){model = newModel;}
	void changeFactory(string newFactory){factory = newFactory;}
	void changeDate(string newDate){date = newDate;}
	void changePrice(string newPrice){price = newPrice;}
	void changeNumber(string newNumber){number = newNumber;}
	void changeScore(string newScore){score = newScore;}
};

int product::ProductLength()
{
	int NameLength = name.size();
	int SortLength = sort.size();
	int PlaceLength = place.size();
	int ModelLength = model.size();
	int FactoryLength = factory.size();
	int DateLength = date.size();
	int PriceLength = price.size();
	int NumberLength = number.size();
	int ScoreLength = score.size();
	int intLength = NameLength + SortLength + PlaceLength + ModelLength + FactoryLength + DateLength + PriceLength + NumberLength + ScoreLength +10;
	return intLength;
}
#endif