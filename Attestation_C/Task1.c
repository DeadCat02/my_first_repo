using System;
class Program {
  public static void Main (string[] args) {
    Console.Write("M: ");
    int m = Convert.ToInt32(Console.ReadLine());
    Console.Write("N: ");
    int n = Convert.ToInt32(Console.ReadLine());
    Program obj = new Program();
    int j = obj.Count(m, n);
    
    
  }

  public int Count(int num1, int num2){
    if (num1==num2){
      Console.Write(num1 + " ");
      return num1;
    } else {
      Console.Write(num1 + " ");
      return Count(num1 + 1, num2);
    }
  }
}