/*
#include <iostream>
using namespace std;

int main()
{
	int numberOfLanguages;
	cout << "How many programming languages have you used:";
	cin >> numberOfLanguages;
	if (numberOfLanguages < 1)
		cout << "you need to work harder to learn more\n"
		<< "and do better next time.\n";
	else
		cout << "You hired!\n";
	return 0;
}

#include <iostream>
using namespace std;
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char a = 'b';
	int c = 10, d = 10u, e = 10ul, f = 032, g = 0xC;
	cout << a << "\n"
		<< c << "\n"
		<< d << "\n"
		<< e << "\n"
		<< f << "\n";
	double h = 3.14, i = 3.14f, j = 3.14L;
	cout << h << "\n"
		<< i << "\n"
		<< j << "\n";
	system("PAUSE");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char a, d, e, g, h, m, o;
	int b, c, x, f, i, j;
	double k, l, n;
	
	cin >> oct >> i
		>> hex >> j
		>> k
		>> l >> m
		>> n >> o;

	cout << i << endl
		<< j << endl
		<< k << endl
		<< l << endl
		<< n << endl;

	system("PAUSE");
	return 0;

}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int year, month, day, hour, minute, second;
	cout << "please tell me the date and time: ";
	cin >> year >> month >> day >> hour >> minute >> second;
	cout << year << ":" << month << ":" << day << ":" << hour
		<< ":" << minute << ":" << second << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	cout << (654 * 987) << "\n"
		<< ((-55) * (-52)) << "\n"
		<< (3 / 0) << "\n"			// error C2124: divide or mod by zero
		<< (65 / 2.0) << "\n"
		<< (1e10 * 1e20) << endl;	
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	double Pi = 3.14159, r, C, S;
	cout << "please provide 'r' value: \n";
	cin >> r;
	C = Pi * (2 * r);
	S = Pi * (r * r);
	cout << "C = " << C << "\n"
		<< "S = " << S << "\n";
	system("pause");

	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double x;
	cout << "input a float number: \n";
	cin >> x;
	cout << sin(x) << "\n"
		<< cos(x) << "\n"
		<< tan(x) << "\n"
		<< abs(x) << "\n"
		<< ceil(x) << "\n"
		<< floor(x) << endl;
	system("pause");

	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double x, y;
	cout << "please input two numbers x and y, then I compute the x to the power of y: \n";
	cin >> x >> y;
	cout << pow(x, y) << "\n";
	system("pause");

	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double convertor = 35273.92, mass;
	cout << "provice you ounces: \n";
	cin >> mass;
	mass = mass / convertor;
	cout << ceil(1 / mass) << endl;
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{	
	const double convertor = 0.001;
	double dosage, weightOfMouse, weightOfHuman, amountOfSoda;

	cout << "We are going to talk about a interesting topic today: \n"
		<< "How much dosage of artificial sweets will kill a mouse? \n"
		<< "How much soda you can drink based on the killing dosage for mouse?"
		<< endl;
	cout << "Please input the dosage for mouse you think: \n";
	cin >> dosage;
	cout << "Please input the weight of that mouse: \n";
	cin >> weightOfMouse;
	cout << "Please input your weight: \n";
	cin >> weightOfHuman;
	amountOfSoda = (weightOfHuman * dosage / weightOfHuman) / convertor;
	cout << "You can only drink these amount of soda: " 
		<< amountOfSoda << ", if more than that, it may kill you as well."
		<< endl;
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	const double rateOfRise = 0.076;
	double currentSalary, increase, newSalary, monthlyPay;
	int year;
	cout << "We are going to estimate your future salary,\n"
		<< "nwo, tell me about your current year end income: ";
	cin >> currentSalary;
	cout << "Now, tell me how long you will stay in this compay: ";
	cin >> year;
	newSalary = currentSalary * (pow((1 + rateOfRise), year));
	increase = newSalary - currentSalary;
	monthlyPay = newSalary / 12;
	cout << "This is your future year income: $" << newSalary
		<< " after " << year << "years" << "\n"
		<< "Total increases is $" << increase << " each year. \n"
		<< "And your monthly income by that time is: $" << monthlyPay
		<< ". Well done! And good luck to your future! Bye! \n";
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	int maxNum = 300, actualNum, diff;
	cout << "How many people attending this meeting: " << endl;
	cin >> actualNum;
	if (actualNum <= maxNum)
	{
		diff = maxNum - actualNum;
		cout << "Number of people not vailate the rule." << endl
			<< "Based on law, you still can have " << diff
			<< " people atttend." << endl;
	}
	else {
		diff = actualNum - maxNum;
		cout << "Based to law, you should reduce " << diff
			<< " amount of people to start the meeting." << endl;
	}
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	char a;
	cin >> a;
	int b;
	b = (int)a;
	cout << b << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	char b;
	b = (char)a;
	cout << b << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main() 
{
	cout << "#include<iostream>\n"
		<< "using namespace std;\n"
		<< "int main()\n"
		<< "{\n"
		<< "int a;\n"
		<< "cout<<\"please input an intergal number\"<<endl;\n"
		<< "cin>>a;\n"
		<< "char b;\n"
		<< "b=(char)a;\n"
		<< "cout<<b<<endl;\n"
		<< "}\n";
		system("pause");
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char cha;
	cin >> cha;
	if ((cha >= '0') && (cha <= '9'))
		cout << "it is a number" << endl;
	else if ((cha >= 'a') && (cha <= 'z'))
		cout << "it is a lowercase letter" << endl;
	else if ((cha >= 'A') && (cha <= 'Z'))
		cout << "it is a capital letter" << endl;
	else
	{
		int b;
		b = (int)cha;
		cout << "it is a special character with ASCII " << b << endl;
	}
	system("pause");
	return 0;
}
*/


