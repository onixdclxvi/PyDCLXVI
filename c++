#include <curl/curl.h>
#include "iostream"
#include "fstream"
#include "vector"
#include "regex"




using namespace std;


class GitHack{
    vector<string> UrlVector;

public:
    auto OpenFile(string datafile) {
        ifstream fileobj;
        fileobj.open(datafile);

        if (fileobj.is_open())
        {
            cout << "Файл открыт!" << endl;

            string strline;
            while(getline(fileobj,strline)){
                RgxPush(strline);
            }
            fileobj.close();

            sort(UrlVector.begin(), UrlVector.end());
            UrlVector.resize(unique(UrlVector.begin(), UrlVector.end()) - UrlVector.begin());

            cout << (int)UrlVector.size() << endl;
        }
        else
        {
            cout << "Файл не открыт!" << endl;
        }


    }

private:
    void RgxPush(string strline){
        regex pattern("((\\w+\\.)?\\w+\\.\\w{2,4})");
        auto words_begin = sregex_iterator(strline.begin(), strline.end(), pattern);
        auto words_end = sregex_iterator();

        for (sregex_iterator i = words_begin; i != words_end; ++i) {
            smatch match = *i;
            string match_str = match.str();
            UrlVector.insert(UrlVector.end(),match_str);
        }
    }

};


/* auto CreateFile(string file) {
    ofstream ofs(file);
    ofs.close();
} */

int main()
{
    setlocale(LC_ALL, "ru");

    string file;
    //cout << "Введите имя файла: ";
    //getline(cin, file);
    //CreateFile("123.txt");

    //file = "top-1m.csv";
    file = "test1.txt";
    GitHack githack;
    githack.OpenFile(file);
    system("pause");
}







