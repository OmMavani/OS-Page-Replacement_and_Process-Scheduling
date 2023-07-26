// 2BCE029 
// Vasu Beladiya
// A - A2
// Os _ Innovative 

#include "bits/stdc++.h"
using namespace std;

#define int long long
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)v.size()

int page_fault = 0;
vector<vector<int>> table;

void print(vector<int> res, int frames){
    int c = 0;
    table.push_back(res);
    for(int i = 0; i < res.size(); i++ ){
        if(res[i] == -1){
            c++;
        }
    }

    if(c != frames + 1){
        page_fault++;
    }
}


void printTable(int frames, int n){
    for(int row = 1; row <= frames; row++){
        for(int i = 0; i < n; i++){
            if(table[i][row] == -1) cout << "  ";
            else cout << table[i][row] << " ";
            if(i != n - 1) cout << "| ";
        }
        cout << '\n';
    }

}

void FIFO(int n,int a[],int frames)
{
    table.clear();
    page_fault = 0;
    vector<int> q;
    map<int,int> mp, pos;
    vector<int> res(frames + 1, -1);

    for(int i = 0; i < n; i++)
    {
        if(q.size() == frames)
        {
            if(mp[a[i]] == 0)
            {
                mp[q[0]] = 0;
                int next = pos[q[0]];
                res[next] = a[i];
                pos[a[i]] = next;
                q.erase(q.begin());
                q.push_back(a[i]);
                mp[a[i]] = 1;
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
        else
        {
            if(mp[a[i]] == 0)
            {
                q.push_back(a[i]);
                mp[a[i]] = 1;
                res[i+1] = a[i];
                pos[a[i]] = i+1;
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
    }
    printTable(frames, n);
}

void optimal(int n, int a[], int frames)
{
    table.clear();
    page_fault = 0;
    set<int> q;
    map<int,int> mp, pos;
    vector<int> res(frames + 1, -1);

    for(int i = 0; i < n; i++)
    {
        if(q.size() == frames)
        {
            if(mp[a[i]] == 0)
            {
                set<int> temp = q;
                for(int j = i + 1; j < n; j++)
                {
                    if(temp.size() == 1) break;
                    temp.erase(a[j]);
                }

                q.erase(*temp.begin());
                mp[*temp.begin()] = 0;
                q.insert(a[i]);
                mp[a[i]] = 1;
                int next = pos[*temp.begin()];
                res[next] = a[i];
                pos[a[i]] = next;
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
        else{
            if(mp[a[i]] == 0)
            {
                q.insert(a[i]);
                mp[a[i]] = 1;
                pos[a[i]] = i+1;
                res[i+1] = a[i];
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
    }
    printTable(frames, n);
}

void LRU(int n, int a[], int frames)
{
    table.clear();
    page_fault = 0;
    set<int> q;
    map<int,int> mp, pos;
    vector<int> res(frames + 1, -1);

    for(int i = 0; i < n; i++)
    {
        if(q.size() == frames)
        {
            if(mp[a[i]] == 0)
            {
                set<int> temp = q;
                for(int j = i - 1; j >= 0; j--)
                {
                    if(temp.size() == 1) break;
                    temp.erase(a[j]);
                }

                q.erase(*temp.begin());
                mp[*temp.begin()] = 0;
                q.insert(a[i]);
                mp[a[i]] = 1;
                int next = pos[*temp.begin()];
                res[next] = a[i];
                pos[a[i]] = next;
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
        else{
            if(mp[a[i]] == 0)
            {
                q.insert(a[i]);
                mp[a[i]] = 1;
                pos[a[i]] = i+1;
                res[i+1] = a[i];
                print(res, frames);
            }
            else{
                vector<int> temp(frames+1, -1);
                print(temp, frames);
            }
        }
    }
    printTable(frames, n);
}

void Page_String(int a[],int n)
{
    for(int i = 0; i < n; i++ )
    {
        cout << a[i] << " ";
        if(i != n - 1) cout << "| ";
    }
    cout << "\n";
}

signed main(){ 
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    cout << "---------------------------------------------------------------------------------\n" << endl;
    cout << "                        # Page Replacement Algorithms #" << endl;
    cout << "\n---------------------------------------------------------------------------------" << endl;
    cout << endl;

    int n;
    cout << "\nEnter Size of page Reference string : " << endl;
    cin >> n;

    int a[n];
    cout << "\nEnter Page Reference String : " << endl;
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    int frames;
    char c = 'y';
    while (c == 'y'){
        cout << "\nEnter No of page frames : " << endl; 
        cin >> frames;
        cout << "\n-------------------------------------------------------------------" << endl;

        cout << "\n" << endl;
        // FIFO algo.
        cout << "             || FIFO ( First In First Out ) Algorithm || ";
        cout << "\n-------------------------------------------------------------------\n" << endl;
        cout << "Page String\n" << endl;
        Page_String(a,n);
        cout << "\n";
        cout << "Page  frame table\n" << endl;
        FIFO(n,a,frames);

        cout << "\nTotal Page Faults = " << page_fault << endl;
        cout << "\n-----------------------------------------------------------------" << endl;

        // optimal algo.
        cout << "\n" << endl;
        cout << "                    || Optimal Algorithm || ";
        cout << "\n-----------------------------------------------------------------\n" << endl;
        cout << "Page String\n" << endl;;
        Page_String(a,n);
        cout << "\n";
        cout << "Page  frame table\n" << endl;
        optimal(n,a,frames);

        cout << "\nTotal Page Faults = " << page_fault << endl;
        cout << "\n---------------------------------------------------------------" << endl;

        // LRU algo.
        cout << "\n" << endl;
        cout << "           || LRU ( Least Recently Use ) Algorithm ||";
        cout << "\n---------------------------------------------------------------\n" << endl;
        cout << "Page String\n" << endl;
        Page_String(a,n);
        cout << "\n";
        cout << "Page  frame table\n" << endl;
        LRU(n,a,frames);

        cout << "\nTotal Page Faults = " << page_fault << endl;
        cout << "\n---------------------------------------------------------------" << endl;

        cout << "\n============================================================================\n" << endl;
        cout << "Do you Want to continue : (y / n)" << endl; 
        cin >> c; 
        cout << "\n============================================================================\n" << endl;
    }
    
}

// 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1