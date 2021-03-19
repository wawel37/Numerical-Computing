#include <iostream>
#include <math.h>

using namespace std;

float riemanSumSinglePrecision(const int N, const float S, bool reverse){
    float sum = 0;
    if(!reverse){
        for(int i = 1; i < N + 1; i++){
            sum += 1.0f/powf((float)i, S);
        }
    }else{
        for(int i = N; i >= 1; i--){
            sum += 1.0f/powf((float)i, S);
        }
    }
    return sum;
}

float dirichletSumSinglePrecision(int N, float S, bool reverse){
    float sum = 0;
    if(!reverse){
        for(int i = 1; i < N + 1; i++){
            sum += powf((-1.0f),(float)(i - 1))*(1.0f/powf((float)i, S));
        }
    }else{
        for(int i = N; i >= 1; i--){
            sum += powf((-1.0f),(float)(i - 1))*(1.0f/powf((float)i, S));
        }
    }
    return sum;
}

double riemanSumDoublePrecision(const int N, const double S, bool reverse){
    double sum = 0;
    if(!reverse){
        for(int i = 1; i < N + 1; i++){
            sum += 1.0/pow((double)i, S);
        }
    }else{
        for(int i = N; i >= 1; i--){
            sum += 1.0/pow((double)i, S);
        }
    }
    return sum;
}

double dirichletSumDoublePrecision(int N, double S, bool reverse){
    double sum = 0;
    if(!reverse){
        for(int i = 1; i < N + 1; i++){
            sum += pow((-1.0),(double)(i - 1))*(1.0/pow((double)i, S));
        }
    }else{
        for(int i = N; i >= 1; i--){
            sum += pow((-1.0),(double)(i - 1))*(1.0/pow((double)i, S));
        }
    }
    return sum;
}

int main(){
    int N[5] = {50, 100, 200, 500, 1000};
    float Ssingle[5] = {2.0f, 3.6667f, 5.2f, 7.2f, 10.0f};
    double Sdouble[5] = {2.0, 3.6667, 5.2, 7.2, 10.0};

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            printf("---- N = %d  S = %f ----\n\n", N[i], Ssingle[j]);
            printf("Not reversed: \n\n");

            printf("Single Precision: \n");
            printf("Dirichlet: %f\n", dirichletSumSinglePrecision(N[i], Ssingle[j], false));
            printf("Rieman: %f\n\n", riemanSumSinglePrecision(N[i], Ssingle[j], false));

            printf("Double Precision: \n");
            printf("Dirichlet: %lf\n", dirichletSumDoublePrecision(N[i], Sdouble[j], false));
            printf("Rieman: %lf\n\n", riemanSumDoublePrecision(N[i], Sdouble[j], false));

            printf("Reversed: \n\n");

            printf("Single Precision: \n");
            printf("Dirichlet: %f\n", dirichletSumSinglePrecision(N[i], Ssingle[j], true));
            printf("Rieman: %f\n\n", riemanSumSinglePrecision(N[i], Ssingle[j], true));

            printf("Double Precision: \n");
            printf("Dirichlet: %lf\n", dirichletSumDoublePrecision(N[i], Sdouble[j], true));
            printf("Rieman: %lf\n\n", riemanSumDoublePrecision(N[i], Sdouble[j], true));
        }
    }

    return 0;
}