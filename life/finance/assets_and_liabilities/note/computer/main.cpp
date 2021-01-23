#include <stdio.h>
#include <iostream>
double total(double pri, double rate,
	     double add_pri, double add_rate,
	     int count);
int main()
{
  using std::cin;
  using std::cout;
  using std::endl;
  using std::string;

  string str = "";

  while(str != "y") {
    double principal; // 本金
    double rate; // 增长率
    double add_pri; // 每增长一次追加多少本金
    double add_rate;
    int count; // 增长次数
    cout << "本金:";
    cin >> principal;
    cout << "增长率:";
    cin >> rate;
    cout << "每增长一次追加多少本金:";
    cin >> add_pri;
    cout << "本金增长率:";
    cin >> add_rate;
    cout << "增长次数:";
    cin >> count;
    cout << "总金额:" << total(principal, rate, add_pri, add_rate,
			       count) << endl;;
    cout << "quit ?";
    cin >> str;
  }
}
// ---------------------------------------------------------------
double total(double pri, double rate,
	     double add_pri, double add_rate, int count)
{
  double total = pri;
  double add = add_pri;
  for (int i = 0; i < count; ++i) {
    if (i == 0) {
      total = total*(1.0+rate);
    } else {
      if (1 == i) {
	total = (total+add_pri)*(1.0+rate);
      } else {
	total = (total+add_pri*(1.0+add_rate))*(1.0+rate);
      }
    } // else
  } // for
  return total;
}
