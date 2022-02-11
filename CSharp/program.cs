//Version 1
//get data -> show access permissions

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace identificarIdade
{
    internal class Program
    {
        static void calcularIdade(int xx, string yy)
        {
            if (xx > 18)
            {
                Console.WriteLine(yy+" você está autorizado");
                Console.ReadLine();
            }
            else if (xx > 11 && xx < 18)
            {
                Console.WriteLine(yy+" vôcÊ é muito jovem");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine(yy+" você é criança ainda");
                Console.ReadLine();
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Qual seu nome?");
            var name = Console.ReadLine();

            Console.WriteLine("Qual sua idade:");
            var idade = int.Parse(Console.ReadLine());

            calcularIdade(idade, name);
            
        }
    }
}
