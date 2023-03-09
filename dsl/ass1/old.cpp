#include <iostream>
using namespace std;


class Contacts{
    char name[10];
    long no;

    public:
    Contacts() {
        cout << "Please input name : ";
        cin >> name;
        cout << endl;

        cout << "Please input cont : ";
        cin >> no;
        cout << endl;
    }
};

int main(){
    return 0;
}
