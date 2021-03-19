#include <iostream>
#include <iomanip>
#include <time.h>

using namespace std;

double absoluteError(double sum, double precise){
    return abs(precise - sum);
}

double relativeError(double sum, double precise){
    return abs(absoluteError(sum,precise)/precise);
}

float recursiveSum(float array[], int left, int right)
{
    if (left == right)
    {
        return array[left];
    }
    int mid = (left+right)/2;
    return recursiveSum(array,left,mid) + recursiveSum(array,mid+1,right);
}

float kahanSum(float array[], int N){
    float sum = 0;
    float err = 0;
    for(int i = 0; i < N; i++){
        float y = array[i] - err;
        float temp = sum + y;
        err = (temp - sum) - y;
        sum = temp;
    }
    return sum;
}

double calculateTime(clock_t timer){
    return (double)(clock() - timer) / CLOCKS_PER_SEC;
}



int main(){
    clock_t timer;
    double sumTimer, recursiveTimer, kahanTimer;

    const int N = 10000000;
    const float V = 0.53125;
    const float PRECISE = V * N;
    const int INTERVAL = 25000;
    
    double intervalArray[N/INTERVAL];
    float sum = 0;
    float *array = new float[N];

    timer = clock();
    for(int i = 0; i < N; i++){
        array[i] = V;
    }
    sumTimer = calculateTime(timer);

    for(int i = 0; i < N; i++){
        sum += array[i];
        if((i + 1) % 25000 == 0){
            intervalArray[(i+1)/25000] = relativeError(sum, (i+1)*V);
        }
    }
    
    //1.1

    cout << "Sum: " << setprecision(10) << sum << endl;
    cout << "Precise value: " << setprecision(10) << PRECISE << endl << endl;

    //1.2
    
    cout << "Sum errors" << endl;
    cout << "Relative error: " << setprecision(10) << relativeError(sum, PRECISE) << endl;
    cout << "Absolute error: " << setprecision(10) << absoluteError(sum, PRECISE) << endl << endl;

    //1.3

    cout << "Interval relative errors: " << endl << endl;

    for(int i = 0; i < N/INTERVAL; i++){
        cout << i + 1 << ". " << intervalArray[i] << endl;
    }
    
    //1.5

    timer = clock();
    float recSum = recursiveSum(array, 0, N-1);
    recursiveTimer = calculateTime(timer);

    cout << "Recursive errors: " << endl;
    cout << "Relative error: " << setprecision(10) << relativeError(recSum, PRECISE) << endl;
    cout << "Absolute error: " << setprecision(10) << absoluteError(recSum, PRECISE) << endl << endl;

    //1.6
    
    cout << "Sum Timer vs Recursive Sum Timer" << endl;
    cout << "Sum time: " << setprecision(10) << sumTimer << " s" << endl; 
    cout << "Recursive Sum Time: " << setprecision(10) << recursiveTimer << " s" << endl << endl;

    //2.1

    timer = clock();
    float kahSum = kahanSum(array, N);
    kahanTimer = calculateTime(timer);

    cout << "Kahan algorithm errors: " << endl;
    cout << "Relative error: " << setprecision(10) << relativeError(kahSum, PRECISE) << endl;
    cout << "Absolute error: " << setprecision(10) << absoluteError(kahSum, PRECISE) << endl << endl;

    //2.4

    cout << "Sum Timer vs Kahan Timer" << endl;
    cout << "Sum time: " << setprecision(10) << sumTimer << " s" << endl; 
    cout << "Kahan Sum Time: " << setprecision(10) << kahanTimer << " s" << endl << endl;


    delete(array);

}