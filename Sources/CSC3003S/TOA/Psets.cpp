/* recusrive powerset construction, decrease and conquer - find all subsets of original input set, 
 * less the last element, then add this last element to th recursively constructed subsets */
/* P. Marais 2025 */

#include <list>
#include <vector>
#include <iostream>

using namespace std;

list< vector<char> > Pset(list<vector<char> > in, vector<char> vals)
{
	// base case returns empty set
    if (vals.size() == 0) // empty set
    {
          in.push_back( vector<char>() );
	  return in;
    }
    else
    {
        // remove the last element from current input subset, then recursively 
        // compute subsets from remaining elements
        char v = vals.back();
        vals.pop_back();
	// recursion
        list<vector<char> > L = Pset(in, vals);
	// augment returned subsets  - a bit fiddly because of data structure used....
	list <vector<char> > S;
        for (auto x : L)
	{
           x.push_back(v);
           S.push_back(  x );
	}
     
       // concatenate subsets to existing subsets	
       for (auto x: S) L.push_back(x);

       return L;
     }
}

int main(void)
{
   list< vector<char> > sets;
   vector<char> vals{'a','b','c','d'};

   sets = Pset(sets, vals);

   for (auto x : sets)
   {
      cout << "{ ";
       for (auto y:x)
           cout << y << " " ;
      cout << "}\n";
    }

  return 0;
}
