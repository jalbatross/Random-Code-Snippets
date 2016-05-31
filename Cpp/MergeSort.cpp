/**************************

   Merge Sort from CLRS
   Made by JOEY!!!

   Running time:
   10 elements: 0.001s
   100 elements: 0.011s
   1000 elements: 0.111s
   10000 elements: 1.489s
   100000 elements: 13.937s
   1000000 elements: 188.669s

***************************/

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <time.h>
#include <stdlib.h>   

std::vector<int> merge(const std::vector<int> arr1, 
                       const std::vector<int> arr2);
std::vector<int> mergeSort(std::vector<int> &arrayToSort);
int main()
{
   const int ARR_SIZE = 1234;
   clock_t start, finish;
   start = clock();

   std::vector<int> toSort;
   int random;
   srand (time(NULL));

   for (int i = 0; i < ARR_SIZE; i++)
   {
      random = rand() % RAND_MAX - (RAND_MAX/2);
      toSort.push_back(random);
   }
   
   mergeSort(toSort);
   finish = clock(); 

   /*
   std::cout << "[ ";
   for (int i = 0; i < toSort.size(); i++)
   {
      std::cout << toSort[i] << " ";
   }
   std::cout << "] \n";   */
   std::cout << "Time for sort (seconds): " << std::setprecision(10) <<  ((double)(finish - start))/CLOCKS_PER_SEC;

   int foo;
   std::cin >> foo;

   return 0;
}

std::vector<int> merge(const std::vector<int> arr1, const std::vector<int> arr2)
{
   std::vector<int> mergedArray;
   int len = arr1.size() + arr2.size();
   int j = 0, k = 0;

   mergedArray.resize(len);
   for (int i = 0; i < len; i++)
   {
      if (arr1[j] <= arr2[k])
      {
         mergedArray[i] = arr1[j];
         j++;
      }
      else
      {
         mergedArray[i] = arr2[k];
         k++;
      }

      if (j == arr1.size() || k == arr2.size())
      {
         i++;
         if (j == arr1.size())
         {
            for (i; i < len; i++, k++)
               mergedArray[i] = arr2[k];
         }
         else
         {
            for (i; i < len; i++, j++)
               mergedArray[i] = arr1[j];
         }
      }

   }
   return mergedArray;
}

std::vector<int> mergeSort(std::vector<int> &arrayToSort)
{
   if (arrayToSort.size() <= 1)
      return arrayToSort;
   else
   {
      std::vector<int> firstHalf, secondHalf;
      firstHalf.resize(arrayToSort.size() / 2);
      secondHalf.resize(arrayToSort.size() - firstHalf.size());\
      for (int i = 0, j = 0, k = 0; i < arrayToSort.size(); i++)
      {
         if (i < firstHalf.size())
         {
            firstHalf[j] = arrayToSort[i];
            j++;
         }
         else
         {
            secondHalf[k] = arrayToSort[i];
            k++;
         }
   }

   mergeSort(firstHalf);
   mergeSort(secondHalf);
   arrayToSort = merge(firstHalf, secondHalf);
   }
   return arrayToSort;
}
