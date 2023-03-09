#include <iostream>
using namespace std;
class Contacts{
    private:
        string name;
        string telephone;
        int key;
    public:
        Contacts(){
            key=0;
        }
        friend class hashing;   
};
int place_inserter(string s){
    int sum=0;
    sum = s[0]-65;
    int len = s.length()-1;
    sum = sum + len;
    return sum%10;
}
class hashing{
    private:
        Contacts data[100]; 
        string n;
        string tele;
        int k, index;
        int size=100;
    public:
        hashing(){
            k=0;
        }
        void accept(string n,string tele){
            k=place_inserter(n);   
            index=k%size;   
            for (int j=index;j<size;j++){
                if(data[index].key==0){
                    data[index].key=k;
                    data[index].name=n;
                    data[index].telephone=tele;
                    break;
                }
                else
                    index=(index+1)%size;
            }
        }
        void search(string name){
            int index1,k,flag=0;
            k=place_inserter(name);
            index1=k%size;
            for(int a=0;a<size;a++){
                if(data[index1].key==k){
                    flag=1;
                    cout<<"\nRecord found\n";
                    cout<<"Name :: "<<data[index1].name<<endl;
                    cout<<"Telephone :: "<<data[index1].telephone<<endl;
                    break;
                }
                else
                    index1=(index1+1);
            }
            if(flag==0)
                cout<<"Record not found";
        };
        void delete_elem(string name){
            int index1,key,flag=0;
            key=place_inserter(name);
            index1=key%size;
            for(int a=index1;a<size;a++){
                if(data[index].key==key){
                    flag=1;
                    data[index1].key=0;
                    data[index1].name=" ";
                    data[index1].telephone=" ";
                    cout<<"\nRecord delete_elemd successfully"<<endl;
                    break;
                }
                else
                    index1=(index1+1)%size;
            }
            if(flag==0)
                cout<<"\nRecord not found";
        }
        void update(string name){
            int index1,key,flag=0;
            key=place_inserter(name);
            index1=key%size;
            for(int a=index1;a<size;a++){
                if(data[index1].key==key){
                    flag=1;
                    break;
                }
                else
                    index1=(index1+1)%size;
            }

            if(flag==1){
                cout<<"Enter the new telephone number :: ";
                cin>>tele;
                data[index1].telephone=tele;
                cout<<"\nRecord Updated successfully";
            }
        }

        
        void display(){
            cout<<"\t  Name  \t\t Telephone";
            for (int a = 0; a < size; a++) {
                if(data[a].key!=0){
                    cout<<"\n\t"<<data[a].name<<" \t\t\t "<<data[a].telephone;
                }
            }
        }
};


int main(){
    hashing s;
    string name;
    string telephone;
    int choice,x;
    bool loop=1;
    while(loop){
        cout<<"\n-------------------------"<<endl
            <<" Telephone book Database "<<endl
            <<"-------------------------"<<endl
            <<"1. Create Record"<<endl
            <<"2. Display Record"<<endl
            <<"3. Search Record"<<endl
            <<"4. Update Record"<<endl
            <<"5. Delete Record"<<endl
            <<"6. Exit"<<endl
            <<"Enter choice :: ";
        cin>>choice;
        switch (choice)
        {
        case 1:
            cout<<"\nEnter name :: ";
            cin>>name;
            cout<<"Enter Telephone number :: ";
            cin>>telephone;
            s.accept(name,telephone);
            break;
        
        case 2:
            s.display();
            break;

        case 3:
            cout<<"\nEnter the name :: ";
            cin>>name;
            s.search(name);
            break;
        case 4:
            cout<<"\nEnter the name :: ";
            cin>>name;
            s.update(name);
            break;
        case 5:
            cout<<"\nEnter name to Delete :: ";
            cin>>name;
            s.delete_elem(name);
            break;

        case 6:
            loop=0;
            break;

        default:
            cout<<"\nYou Entered something wrong!";
            break;
        }
    }   
    return 0;
}

