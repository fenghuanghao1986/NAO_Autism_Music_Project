/*
// Q1
#include <iostream>
#include <array>
using namespace std;

bool compareWithCase(char str1[], int len1, char str2[], int len2)
{
	int i;

	if (len1 != len2)
		return false;

	for (i = 0; i < len1; i++)
	{
		if (str1[i] != str2[i])
			return false;
		else
			continue;
	}
	return true;
	
}

bool compareIgnoreCase(char str1[], int len1, char str2[], int len2)
{
	int i;

	if (len1 != len2)
		return false;

	for (i = 0; i < len1; i++)
	{
		if (toupper(str1[i]) != toupper(str2[i]))
			return false;
		else
			continue;
	}
	return true;
}

int main()
{
	int len1, len2;
	char str1[255], str2[255];

	cout << "Please input one set of chars until you hit enter twice: " << endl;
	cin >> str1;
	len1 = sizeof(str1);
	cout << "Please input another set of chars until you hit enter twice: " << endl;
	cin >> str2;
	len2 = sizeof(str2);

	cout << str1 << endl;
	cout << str2 << endl;

	cout << compareWithCase(str1, len1, str2, len2) << endl;
	cout << compareIgnoreCase(str1, len1, str2, len2) << endl;

	system("pause");
	return 0;
}
*/


/*
// Q2
#include<iostream>
using namespace std;
int main(int argc, char* argv[]) {
	for (int i = 1; i < argc; i++)
		cout << argv[i];
}
*/


/*
Q6
Write a program that converts from 24-
hour notation to 12-hour notation. For example, it should convert 14:25 to 2:25 P.M. The input is given
as two integers. There should be at least three functions: one for input, one to do the conversion, and
one for output. Record the A.M./P.M. information as a value of type char, ¡¯A¡¯ for A.M. and ¡¯P¡¯
for P.M. Thus, the function for doing the conversions will have a call-by-reference formal parameter of
type char to record whether it is A.M. or P.M. (The function will have other parameters as well.)
Include a loop that lets the user repeat this computation for new input values again and again until the
user says he or she wants to end the program.*/
//
/*
#include <iostream>
#include <string>
using namespace std;

string input()
{
	string str;
	cin >> str;
	cout << str.size() << endl;
	return str;
}

void output(string result)
{
	cout << result << endl;
}


// define time conversion function
string convertTime(string inTime)
{
	int i, j, k;
	int h, m;
	string tempH, tempM;
	string outTime;

	for (i = 0; i < inTime.size(); i++)
	{
		if (inTime[i] == ':')
			cout << i << endl;
			break;
	}

	for (j = 0; j < i; j++)
	{
		cout << j << endl;
		tempH.append(inTime, j);
	}

	for (k = i; k < inTime.size(); k++)
	{
		cout << k << endl;
		tempM.append(inTime, k);
	}

	h = atoi(tempH.c_str());

	if (h > 12 && h <= 24)
	{ 
		h = h - 12;
		tempH = to_string(h);
		outTime = tempH + ":" + tempM + "P.M.";
		return outTime;
	}
	else if (h == 12)
	{
		outTime = tempH + ":" + tempM + "P.M.";
		return outTime;
	}
	else if (h == 0)
	{
		h = 12;
		tempH = to_string(h);
		outTime = tempH + ":" + tempM + "A.M.";
		return outTime;
	}
	else
	{ 
		outTime = tempH + ":" + tempM + "A.M.";
		return outTime;
	}
		
}

// define main function
int main()
{
	string inTime, outTime;

	cout << "Please enter current time in 24hr notation, "
		<< "follow this format 01:23: " << endl;

	inTime = input();
	outTime = convertTime(inTime);
	output(outTime);

	system("pause");

}
*/


/*
Q7
The area of an arbitrary triangle can be
computed using the formula
where a, b, and c are the lengths of the sides, and s is the semiperimeter s=(a+b+c)/2. Write a void
function that uses five parameters: three value parameters that provide the lengths of the edges, and two
reference parameters that compute the area and perimeter (not the semiperimeter). Make your function
robust. Note that not all combinations of a, b, and c produce a triangle. Your function should produce
correct results for legal data and reasonable results for illegal combinations.*/
/*
#include <iostream>
#include <math.h>
using namespace std;

void area(float a, float b, float c)
{
	float ss, ar;
	ss = a + b + c;
	if (a + b <= c || a + c <= b || b + c <= a || a <= 0|| b <= 0 || c <= 0)
	{
		cout << "Check your input! It is not a triangle!!" << endl;
		return;
	}
	else
	{
		ar = sqrt((ss / 2 - a) * (ss / 2 - b) * (ss / 2 - c) * ss / 2);
		cout << "The area of this traiangle is: " << ar << endl;
		return;
	}
	
}
 
int main()
{
	float a, b, c;
	cout << "Please input each side of the triangle: " << endl;
	cout << "Side A is: " << endl;
	cin >> a;
	cout << "Side B is: " << endl;
	cin >> b;
	cout << "Side C is: " << endl;
	cin >> c;
	area(a, b, c);
	system("pause");
}
*/


/*Write a program that tells what coins to
give out for any amount of change from 1 cent to 99 cents. For example, if the amount is 86 cents, the
output would be something like the following:
86 cents can be given as 3 quarter(s) 1 dime(s) and 1 penny(pennies)
Use coin denominations of 25 cents (quarters), 10 cents (dimes), and 1 cent (pennies). Do not use nickel
and half-dollar coins. Your program will use the following function (among others):
void computeCoin(int coinValue, int& number, int& amountLeft);
//Precondition: 0 < coinValue < 100; 0 <= amountLeft < 100.
//Postcondition: number has been set equal to the maximum number
//of coins of denomination coinValue cents that can be obtained
//from amountLeft cents. amountLeft has been decreased by the
//value of the coins, that is, decreased by number*coinValue.
For example, suppose the value of the variable amountLeft is 86. Then, after the following call, the
value of number will be 3 and the value of amountLeft will be 11 (because if you take three quarters
from 86 cents, that leaves 11 cents):
computeCoins(25, number, amountLeft);
Include a loop that lets the user repeat this computation for new input values until the user says he or
she wants to end the program. (Hint: Use integer division and the % operator to implement this
function.)*/
/*
#include <iostream>
#include <math.h>
using namespace std;

//Precondition: 0 < coinValue < 100; 0 <= amountLeft < 100.
//Postcondition: number has been set equal to the maximum number
//of coins of denomination coinValue cents that can be obtained
//from amountLeft cents. amountLeft has been decreased by the
//value of the coins, that is, decreased by number*coinValue.

void computeCoin(int coinValue, int& number, int& amountLeft)
{
	if (coinValue < 1 || coinValue >99)
	{

		cout << "input error!" << endl;
		return;
	}
	else
	{ 
		cout << coinValue << " cents can be gicen as ";
		number = coinValue / 25;
		amountLeft = coinValue % 25;
		cout << number << " quarter(s) ";
		number = amountLeft / 10;
		amountLeft = amountLeft % 10;
		cout << number << " dime(s) and "
			<< amountLeft << " penny(pennies)"
			<< endl;
		return;
	}
}

int main()
{
	int coinValue;
	int number=0;
	int amountLeft=0;
	cout << "Please input your total cents: " << endl;
	cin >> coinValue;
	computeCoin(coinValue, number, amountLeft);
	system("pause");
}
*/



/*
Q9
Write a program that reads in the average
monthly rainfall for a city for each month of the year and then reads in the actual monthly rainfall for
each of the previous 12 months. The program then prints out a nicely formatted table showing the
rainfall for each of the previous 12 months as well as how much above or below average the rainfall
was for each month. The average monthly rainfall is given for the months January, February, and so
forth, in order. To obtain the actual rainfall for the previous 12 months, the program first asks what the
current month is and then asks for the rainfall figures for the previous 12 months. The output should
correctly label the months.
There are a variety of ways to deal with the month names. One straightforward method is to code the
months as integers and then do a conversion before doing the output. A large switch statement is
acceptable in an output function. The month input can be handled in any manner you wish, as long as it
is relatively easy and pleasant for the user.
After you have completed the above program, produce an enhanced version that also outputs a graph
showing the average rainfall and the actual rainfall for each of the previous 12 months. The graph
should be similar to the one shown in Display 5.4, except that there should be two bar graphs for each
month and they should be labeled as the average rainfall and the rainfall for the most recent month.
Your program should ask the user whether she or he wants to see the table or the bar graph, and then
should display whichever format is requested. Include a loop that allows the user to see either format as
often as the user wishes until the user requests that the program end.
*/
/*
#include <iostream>
#include <string>
using namespace std;

float rainIn()
{
	float rainFall;
	cin >> rainFall;
	return rainFall;
}

string monthIn()
{
	string month;
	cin >> month;
	return month;
}

void output(string monthList[], float rainFallList[], float diff[]) 
{
	int i, j;

	for (j = 0; j < 12; j++)
	{
		cout << monthList[j] << "\t|";
	}
	cout << "\n";
	for (j = 0; j < 12; j++)
	{
		cout << "--------";
	}
	cout << "\n";
	for (j = 0; j < 12; j++)
	{
		cout << rainFallList[j] << "\t|";
	}
	cout << "\n";
	for (j = 0; j < 12; j++)
	{
		cout << "--------";
	}
	cout << "\n";
	for (j = 0; j < 12; j++)
	{
		cout << diff[j] << "\t|";
	}
	cout << "\n";
	return;
}

int main()
{
	string monthList[12], month;
	int i;
	float rainFallList[12], diff[12];
	float avgRain, rain;

	cout << "Input average rainfall : " << endl;
	cin >> avgRain;

	for (i = 0; i < 12; i++)
	{
		cout << "Please input month: " << endl;
		month = monthIn();
		monthList[i] = month;
		cout << "Pleaes input current month rainfall: " << endl;
		rain = rainIn();
		rainFallList[i] = rain;
		diff[i] = rain - avgRain;
	}
	output(monthList, rainFallList, diff);
	system("pause");
}

// miss plot bar chart or graph have to work on that. 
*/



