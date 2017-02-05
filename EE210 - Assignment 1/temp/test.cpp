#include <iostream>
using namespace std;
#include <stdlib.h>
#include <iostream>

int main() {
	float *a, *b, *c;
	int n1 = 100000, n2 = 30000;
	//cout << "Input Lengths of Audio";
	//cin >> n1 >> n2;
	int m = n1 + n2 - 1;

	a = (float*)malloc(sizeof(float) * n1);
	b = (float*)malloc(sizeof(float) * n2);
	c = (float*)malloc(sizeof(float) * m);

	for (int i = 0; i < n1; i++){
		for (int j = 0; j < n2; j++){
			c[i+j] += a[i]*b[j];
		}
	}

	cout << "Success" << endl;
}

