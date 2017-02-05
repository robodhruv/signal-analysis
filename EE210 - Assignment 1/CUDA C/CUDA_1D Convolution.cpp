/*
CUDA code for 1D convolution. 
GPU code, CPU code and basic benchmarking has been implemented.
Note that the GPU code is also naive.
*/
#include <cuda.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include "device_functions.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <ctime>
#include <time.h>
using namespace std;

#define THREAD_NUM 512

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

clock_t convolve(const float *a, const float *b, float *d, int n)
{
	clock_t startCPU, endCPU;
	int i, j = 0;

	startCPU = clock();

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			d[i + j] += a[i] * b[j];
		}

	endCPU = clock();

	return endCPU - startCPU;
}

__global__ static void ConvolveCUDA(const float* a, const float* b, float* c, int n)
{
	int i = 0;

	int idx = threadIdx.x + blockDim.x * blockIdx.x;

	if (idx < n)
	{
		float t1 = 0; float t2 = 0;
		for (i = 0; i <= idx; i++) {
			t1 += a[i] * b[idx - i];
		}
		for (i = idx + 1; i < n; i++) {
			t2 += a[i] * b[n + idx - i];
		}
		c[idx] = t1;
		c[n + idx] = t2;
	}
}

clock_t convolveCUDA(const float *a, const float *b, float *c, int n)
{
	float *a_d, *b_d, *c_d;
	clock_t start, end;
	int BLOCK_NUM = n / THREAD_NUM + ((n % THREAD_NUM > 0) ? 1 : 0);

	cudaMalloc((void**)&a_d, sizeof(float) * n);
	cudaMalloc((void**)&b_d, sizeof(float) * n);
	cudaMalloc((void**)&c_d, sizeof(float) * (2 * n - 1));

	start = clock();

	cudaMemcpy(a_d, a, sizeof(float) * n, cudaMemcpyHostToDevice);
	cudaMemcpy(b_d, b, sizeof(float) * n, cudaMemcpyHostToDevice);
	cudaMemcpy(c_d, c, sizeof(float) * (2 * n - 1), cudaMemcpyHostToDevice);

	ConvolveCUDA << < BLOCK_NUM, THREAD_NUM >> >(a_d, b_d, c_d, n);

	cudaMemcpy(c, c_d, sizeof(float) * (2 * n - 1), cudaMemcpyDeviceToHost);

	end = clock();

	cudaFree(a_d);
	cudaFree(b_d);
	cudaFree(c_d);

	return end - start;
}

void compare_arr(const float* a, const float* b, int len)
{
	float max_err = 0;
	float average_err = 0;
	int i = 0;

	for (i = 0; i < len; i++) {
		if (b[i] != 0) {
			float err = fabs((a[i] - b[i]) / b[i]);
			if (max_err < err) max_err = err;
			average_err += err;
		}
	}

	printf("Max error: %g\tAverage error: %g\n", max_err, average_err / (len * len));
}

int main()
{
	float *a, *b, *c, *d;
	int m, n = 0;

	printf("\nInput length n:");
	scanf("%d", &n);

	m = 2 * n - 1;

	a = (float*)malloc(sizeof(float) * n);
	b = (float*)malloc(sizeof(float) * n);
	c = (float*)malloc(sizeof(float) * m);
	d = (float*)malloc(sizeof(float) * m);

	srand((unsigned int)time(NULL) + rand());

	rand_arr(a, n);
	rand_arr(b, n);
	init_arr(c, m);
	init_arr(d, m);

	clock_t timeGPU = convolveCUDA(a, b, c, n);

	clock_t timeCPU = convolve(a, b, d, n);

	compare_arr(c, d, m);

	double secGPU = (double)timeGPU / CLOCKS_PER_SEC;
	double secCPU = (double)timeCPU / CLOCKS_PER_SEC;
	float ratio = secCPU / secGPU;
	printf("CPU vs GPU Time used: %.2f  vs  %.2f\n", secCPU, secGPU);
	printf("CPU vs GPU ratio: %.2f\n\n", ratio);

	char x;
	cin >> x;

	free(a);
	free(b);
	free(c);
	free(d);

	return 0;
}