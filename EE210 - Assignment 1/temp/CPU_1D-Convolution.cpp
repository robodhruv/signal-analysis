/*
CPU code for 1D convolution.
*/
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <ctime>
#include <time.h>
using namespace std;

void init_arr(float *arr, int len)
{
	int i = 0;;
	for (i = 0; i < len; i++) {
		arr[i] = 0.0f;
	}
}

void rand_arr(float *arr, int len)
{
	int i = 0;
	for (i = 0; i < len; i++) {
		arr[i] = (rand() % 1000) * 0.01;
	}
}

clock_t convolve(const float *a, const float *b, float *c, int n1, int n2)
{
	clock_t startCPU, endCPU;
	int i, j;

	startCPU = clock();

	for (i = 0; i < n1; i++)
		for (j = 0; j < n2; j++) {
			c[i + j] += a[i] * b[j];
		}

	endCPU = clock();

	return endCPU - startCPU;
}

int main()
{
	float *a, *b, *c, *d;
	int m, n1, n2 = 0;

	printf("\nInput length n1: ");
	scanf("%d", &n1);
	printf("\nInput length n2: ");
	scanf("%d", &n2);

	m = n1 + n2 - 1;

	a = (float*)malloc(sizeof(float) * n1);
	b = (float*)malloc(sizeof(float) * n2);
	c = (float*)malloc(sizeof(float) * m);

	srand((unsigned int)time(NULL) + rand());

	rand_arr(a, n1);
	rand_arr(b, n2);
	init_arr(c, m);

	clock_t timeCPU = convolve(a, b, c, n1, n2);

	double secCPU = (double)timeCPU / CLOCKS_PER_SEC;
	printf("CPU time used: %.2f", secCPU);
	cout<<endl;

	cout << "Press enter to exit. ";
	getchar();

	free(a);
	free(b);
	free(c);

	return 0;
}
