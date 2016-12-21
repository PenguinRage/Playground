#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//function to check if the string is Palindrome
int isPalindrome(char *str)
{
	//the first index
	int start_index = 0;
	
	//the last index
	int last_index = strlen(str);
	
	while(start_index < last_index && str[start_index] == str[last_index])
	{
		//increment start index and decrement last index
		start_index++;
		last_index--;
	}
	
	if(start_index < last_index)
	{
		//this means that we did not reach the center
		printf("NOT A PALINDROME");
		//code obtained from http://www.studyalgorithms.com
		//feel free to copy but please acknowledge wherever possible
		return 0;
	}
	else
	{
		//we reached the center
		printf("PALINDROME");
		return 1;
	}
}

int main(void)
{
	char *s1 = "abaXaba";
	
	char *s2 = "aaabbbXbbbaaa";
	//code obtained from http://www.studyalgorithms.com
	//feel free to copy but please acknowledge wherever possible
	
	char *s3 = "abababababbabXbababbbbabba";
	
	int x;
	x = isPalindrome(s1);
	x = isPalindrome(s2);
	x = isPalindrome(s3);
	return 0;
}
