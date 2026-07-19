/* Power set using bit enumeration - 2^n sets for n unique set elements, including empty set */
/* P. Marais 2025. */

#include <iostream>
#include <vector>
#include <list>

using namespace std;


int main(void)
{
	vector<char> setEls{'a','b','c','d'};

	size_t nEls = setEls.size();

	list< vector<char> > Psets; // list of powersets, starts empty
	for (size_t i = 0; i < (1<<nEls); ++i) // 2^nEls sets
	{
		vector<char> setI;
		for(size_t j = 0; j < nEls; ++j) // test each element corresponding to differnet bit location
			if (i & (1<<j) ) setI.push_back(setEls[j]); // if bit is set, then set el is present
		Psets.push_back(setI); // done with this subset, save it
	}

	// dump out each subset

	for (auto ps : Psets)
	{
		cout << "{ ";
                for (auto el : ps)
                        cout << el << " ";
		cout << "}\n";
	}

	return 0;
}
