#include <math.h>
#include <stdio.h>
#include <iostream>

int main()
{
  using std::cin;
  using std::cout;
  using std::endl;
  double peak;
  double now_peak;
  double hight_point;
  double low_point;
  double valuation;
  double con_down = 0.0;
  double my_down = 0.0;
  double max_down = 0.0;
  double all_down = 0.0;
  double principal = 0.0;
  double investment_amount = 0.0;
  cout << "3年历史最高点：";
  cin >> peak;
  cout << "三年中现在所处位置：";
  cin >> now_peak;
  cout << "最近高点涨幅: ";
  cin >> hight_point;
  cout << "最近低点涨幅: ";
  cin >> low_point;
  cout << "净值估算涨幅: ";
  cin >> valuation;
  con_down = (low_point - hight_point) + valuation;
  cout << "最近一次连续下跌幅度(%): " << con_down << endl;
  con_down /= 100.0;
  cout << "持有收益率: ";
  cin >> my_down;
  my_down /= 100.0;
  //  cout << "本金: ";
  double factor;
  //  cout << "倍率: ";
  //  cin >> factor;
  principal = 4000.0;
  double x =((peak-now_peak)/peak);
  principal = principal*x;
  cout << "本金: " << principal << endl;
  factor = pow(1+x, 1+x);
  cout << "倍率: " << factor << endl;
  do{
    max_down = con_down + my_down;
    if (con_down > -0.05)
      break;
    all_down = con_down * factor;
  }while(false);
  investment_amount = principal * all_down;
  investment_amount = investment_amount < 0 ?
		      -investment_amount : investment_amount;
  all_down = all_down < 0 ? -all_down : all_down;
  cout << "预估持有收益率: " << max_down * 100.0 << "%" << endl;
  cout << "建议投入本金的: " << all_down * 100 << "%" << endl;
  cout << "建议单笔投入金额: " << investment_amount << endl;
}
