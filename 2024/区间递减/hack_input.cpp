#include<iostream>
#include<cmath>
#include<cstring>
#include<cassert>
#include<string>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<unordered_map>
#include<map>
#include<vector>
#include<set>
#include<unordered_set>
#include<bitset>
#include<climits>
#include<numeric>
#include<functional>
#include<iomanip>
#ifdef YJL
#include<debug.h>
#else
#define debug(...)0
#endif
#define ALL(a) a.begin(),a.end()
using namespace std;
using ll = long long;
#include<random>
mt19937_64 rng(random_device{}());
ll rdi(ll l, ll r) {
    return rng() % (r-l+1) + l;
}

constexpr int V = 1000;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n = rdi(1, V);
    int q = rdi(1, V);
    cout<<n<<" "<<q<<"\n";
    for(int i=0; i<n; ++i) {
        cout<<rdi(1, V)<<" \n"[i+1==n];
    }
    for(int i=0; i<q; ++i) {
        int l = rdi(1, n);
        int r = rdi(1, n);
        if(l>r) swap(l,r);
        cout<<l<<' '<<r<<"\n";
    }
    return 0;
}
/*




*/