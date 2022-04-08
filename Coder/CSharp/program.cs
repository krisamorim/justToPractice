//Version 3.1
//get data -> two options to choose

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
                Console.WriteLine(yy + " você está autorizado");
                Console.ReadLine();
            }
            else if (xx > 11 && xx < 18)
            {
                Console.WriteLine(yy + " você é muito jovem");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine(yy + " você é criança ainda");
                Console.ReadLine();
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Qual seu nome?");
            var name = Console.ReadLine();

            Console.WriteLine("Olá " + name + "! O que deseja fazer? 1- Verificar permissão ou 2- Criar lista");
            var opcao = int.Parse(Console.ReadLine());

            if (opcao == 1)
            {
                Console.WriteLine("Qual sua idade:");
                int idade = int.Parse(Console.ReadLine());
                calcularIdade(idade, name);
            }else if (opcao == 2)
            {
                Console.WriteLine("Digite o primeiro produto:");
                var prod1 = Console.ReadLine();

                Console.WriteLine("Digite o segundo produto:");
                var prod2 = Console.ReadLine();

                Console.WriteLine("Digite o terceiro produto:");
                var prod3 = Console.ReadLine();

                string[] produtos = {prod1, prod2, prod3};

                Console.WriteLine("A lista é:");
                Console.WriteLine(produtos[0]);
                Console.WriteLine(produtos[1]);
                Console.WriteLine(produtos[2]);

                Console.WriteLine("Agora vamos atualizar um item da lista");
                Console.WriteLine("Qual item deseja atualizar? 1, 2 ou 3?");
                var item = int.Parse(Console.ReadLine());
                item = item - 1;
                Console.WriteLine("Deseja alterar o item "+produtos[item]+"? 1- p/ SIM e 2- p/ Não");
                var resp = int.Parse(Console.ReadLine());

                if (resp == 1)
                {
                    Console.WriteLine("Qual o novo item?");
                    produtos[item] = Console.ReadLine();
                    Console.WriteLine("A nova lista ficou assim:");
                    Console.WriteLine(produtos[0]);
                    Console.WriteLine(produtos[1]);
                    Console.WriteLine(produtos[2]);
                    Console.ReadLine();
                }
                else
                {
                    Console.WriteLine("OK bye bye");
                    Console.ReadLine();
                }
            }
        }
    }
}

