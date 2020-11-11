#include <map>
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
int main(int argc,char** argv){
	using namespace std;
	ifstream src;
	ofstream dst;
	map<double,string,greater<double>> sort;
	src.open(argv[1]);
	dst.open(argv[2]);
	int to_sort = 0;
	if(atoi(argv[3])==1)
		to_sort = 2;
	else if(atoi(argv[3])==2)
		to_sort = 3;
	else if(atoi(argv[3])==3)
		to_sort = 4;
	else if(atoi(argv[3])==4)
		to_sort = 5;
	else if(atoi(argv[3])==5)
		to_sort = 6;
	string temp;
	cout<<"SORTING BY "<<argv[3]<<" score..."<<endl;
	cout<<"PLEASE WAIT..."<<endl;
	long count = 0;
	while(src.good()){
		getline(src,temp);
		if(!temp.size())
			break;
		int cut = 0;
		int cut_index =0;
		for(int i=0;cut<to_sort;i++){
			cut_index++;
			if(temp[i] == ':')
				cut++;
		}
		cut_index++;
		int cut_size = 1;
		for(int i=cut_index;i<temp.size();i++){
			if(temp[i] == ',')
				break;
			cut_size++;
		}
		double score = 0;
		count++;
		cout<<"cont = "<<count<<endl;
		cout<<"cut index = "<<cut_index<<"  cut_size = "<<cut_size<<endl;
		if(cut_size>temp.size()-cut_index)
			score = stod(temp.substr(cut_index));
		else
			score = stod(temp.substr(cut_index,cut_size));
		cout<<"score : "<<score<<endl;
		sort.insert(make_pair(score,temp));
	}
	cout<<sort.size()<<endl;
	for(auto iter = sort.begin();iter != sort.end();iter++)
		dst<<iter->second<<endl;
	src.close();
	dst.close();

	return 0;

}
