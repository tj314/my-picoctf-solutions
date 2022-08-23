# General skills: flag_shop
There's a flag shop selling stuff, can you buy a flag? [Source](https://jupiter.challenges.picoctf.org/static/dd28f0987f28c894f35d5d48564c3402/store.c). Connect with `nc jupiter.challenges.picoctf.org 44566`.

## Solution
This was the first truly interesting challenge in the 'General skills' section. I downloaded the source code and started reading it.

The source implements a shop with flags. First, it requests user input to select activity type:
- 1 to show balance
- 2 to buy flags:
	- 1 to buy knockoff flags, then the user enters the amount to buy
	- 2 to buy the real flag
- 3 to exit

The account balance is initially 1100. To buy the real flag, the account balance must be at least 100000.

There is an integer variable to hold the account balance. The user may request to buy a positive amount of knockoff flags. Each costs 900. This is the crucial portion of the code which can be exploited (abbreviated):
```C
int total_cost = 900*number_flags;
if(total_cost <= account_balance){
	account_balance = account_balance - total_cost;
}
```

Here we can see, that should the `number_flags` be big enough, the `total_cost` variable could overflow and pass the check. Then, the account_balance would increase.

So, how many flags should we buy? Well, the maximum value the `int` data type may hold is 2147483647. If we divide that by 900, we get approx. 2386093. This amount will cause the overflow. However, if we use this amount, the amount added to the balance will be too big and the balance will overflow as well. Therefore, we must increase the number of flags to buy a bit more.

I used 2400000. This increased the balance and I was able to buy the correct flag.