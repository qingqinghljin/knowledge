#include <iostream>
#include <stdio.h>
int main()
{
  using std::cin;
  using std::cout;
  using std::endl;
  double con_down = 0.0;
  double my_down = 0.0;
  double max_down = 0.0;
  double all_down = 0.0;
  double principal = 0.0;
  double investment_amount = 0.0;
  cout << "最近一次连续下跌幅度(%): ";
  cin >> con_down;
  con_down /= 100.0;
  cout << "我的收益率: ";
  cin >> my_down;
  my_down /= 100.0;
  cout << "本金: ";
  cin >> principal;
  do{
    max_down = con_down + my_down;
    if (con_down > -0.05 and max_down > -0.05)
      break;
    if (my_down < 0.0) {
      all_down = max_down * 1.5; 
    } else {
      all_down = con_down * 2.0;
    }
  }while(false);
  investment_amount = principal * all_down;
  investment_amount = investment_amount < 0 ?
		      -investment_amount : investment_amount;
  cout << "总跌幅: " << max_down * 100.0 << "%" << endl;
  cout << "建议投入本金的: " << all_down * 100 << "%" << endl;
  cout << "建议单笔投入金额: " << investment_amount << endl;
}
