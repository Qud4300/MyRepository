#include <iostream>
#include <string>
#include <array>
#include "pch.h"
using namespace std;
class puzzle {
	typedef array<int,3> col;
	col row[3];

public :
	string toString(void){
		string res = "";
		for (int i = 0; i < 3; i++) {
			res + "[" + to_string(row[i][0]) + " " + to_string(row[0][1])
				+ " " + to_string(row[i][2]) + "]" + "\n";
		}
		return res;
	}

	puzzle() {
		row[0] = col{ 2, 8, 3 };
		row[1] = col{ 1, 6, 4 };
		row[2] = col{ 7, 0, 5 };
	}
};

int main()
{
	puzzle myPuzzle;
	myPuzzle.toString();
}

