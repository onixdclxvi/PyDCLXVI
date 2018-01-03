using System;
using System.IO;
using System.Threading.Tasks;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.Linq;
using System.Net;

namespace GitHack
{
    internal static class MainClass
    {
        public static void Main(string[] args)
        {
            ReadFile("/Users/artemkalinkin/Desktop/C#/test.txt");
        }


        private static void ReadFile(string filename)
        {
            var urls = new List<string>(); 

            Console.WriteLine(File.Exists(filename) ? true : false);

            var read = new StreamReader(filename);
                while (!read.EndOfStream)
            {
                var pattern = @"(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)";
                foreach (Match m in Regex.Matches(read.ReadLine(), pattern))
                {
                    urls.Add("https://" + m.Value);
                    urls.Add("http://" + m.Value);
                }
            }

            var distinctUrls = new List<string>(urls.Distinct());
            Console.WriteLine(Environment.ProcessorCount * 10);
            
            var sw = new Stopwatch();
            sw.Start();
            Parallel.ForEach(distinctUrls, new ParallelOptions { MaxDegreeOfParallelism = Environment.ProcessorCount * 5 }, CheckUrl);
            sw.Stop();
            Console.WriteLine((sw.ElapsedMilliseconds/100.0).ToString(CultureInfo.InvariantCulture));
            Console.WriteLine("Всего элементов - " + distinctUrls.Count());
        }


        private static void CheckUrl(string url)
        {
            var uri = new Uri(url + "/.git/HEAD");
            const string pattern = @"([a-z][a-z][a-z][:]\s[r][e][f][s]/)";

            try
            {
            var html = new WebClient().DownloadString(uri);
                foreach (Match m in Regex.Matches(html, pattern))
                Console.WriteLine(url + " Уязвимый");
            }
            catch (InvalidOperationException ex)
            {
                //Console.WriteLine(ex.GetType().FullName);
                //Console.WriteLine(url + " " + ex.Message);
            }
            return;
        }
    }
}

