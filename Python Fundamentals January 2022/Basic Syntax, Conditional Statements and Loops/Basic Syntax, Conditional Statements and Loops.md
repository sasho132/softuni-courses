## 1. Largest of Three Numbers

Write a program that receives **three whole numbers** and prints the **largest one**.


## 2. Number Definer 

Write a program that reads a floating-point number and:
-	prints **"zero"** if the number is zero. 
-	prints **"positive"** or **"negative"**. 
-	adds **"small"** if the absolute value of the number is less than 1 and it is not 0, or **"large"** if it exceeds 
1 000 000.


## 3. Word Reverse

Write a program that receives a **single word**, **reverses it**, and **prints it**.


## 4. Number Between 1 and 100

Write a program that reads different floating-point numbers from the console. When it receives a number between 1 and 100 inclusive, the program should stop reading and should print **"The number {number} is between 1 and 100"**.


## 5. Patterns

Write a program that receives a **number** and **creates the following pattern**. The number represents the largest count of stars on one row.


## 6. Jenny's Secret Message

Jenny studies programming with Python and wants to create a program that **greets users** when they give their **names**. The greeting should be in the format **"Hello, {name}!"**. However, Jenny is in love with **Johnny** and would like to **greet him differently: "Hello, my love!"**. Could you help her?


## 7. Drink Something

**Kids** drink **toddy**, **teens** drink **coke**, **young adults** drink **beer**, and **adults** drink **whisky**. Create a program that receives an age and prints what they drink.

**Rules:**
* **A kid** is defined as someone **under or at the age of 14**.
* **A teen** is defined as someone **under or at the age of 18**.
* **A young adult** is defined as someone **under or at the age of 21**.
* **An adult** is defined as someone **above the age of 21**.

**Note:** All the values are **inclusive** except the **last one**!


## 8. Leonardo DiCaprio Oscars

Write a program that receives a **single integer** number and prints **different messages** depending on the number:
-	If the number **is 88 - "Leo finally won the Oscar! Leo is happy"**.
-	If the number **is 86 - "Not even for Wolf of Wall Street?!**"
-	If the number **is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?**"
-	If the number **is over 88 - "Leo got one already!**"


## 9. Double Char

You will be given a **string**. You should **print** a **string** in which **each character** (case-sensitive) is **repeated twice**.


## 10. Can't Sleep? Count Sheep

If you can't fall asleep, try counting sheep! You will be given a **positive integer**, 3, for example. You should return a string with a murmur: **"1 sheep...2 sheep...3 sheep..."**. Input will always be valid, i.e., integers greater than 0.

## 11. Orders

You work at a coffee shop, and your job is to **place orders** to the distributors. Thus, you want to know the **price of each order**. On the first line, you will receive integer **N** – the **number of orders** the shop will receive. For each order, you will receive the following information:
* Price per capsule - a **floating-point number** in the range [0.00…1000.00]
* Days – **integer** in the range [1…31]
* Capsules count - **integer** in the range [0…2000]

For **each order**, you should **print a single line** in the following format:

* **"The price for the coffee is: ${price}"**

On the final line, you need to **print the total price** in the following format:

* **"Total: ${total_price}"**

The **price must be formatted** to the second decimal place. 


## 12. Maximum Multiple

On the first line, you will be given a positive number, which will serve as a **divisor**. On the second line, you will receive a positive number that will be the **boundary**. You should find the **largest** integer **N**, that is:
* **divisible by the given divisor**
* **less than or equal to the given bound**
* **greater than 0**

**Note:** it is guaranteed that **N is found**.


## 13. Mutate Strings

You will be given **two strings**. **Transform the first** string into **the second** one, **letter** by letter. Print only the **unique** strings.

**Note:** the strings will have the same lengths.


## 14. Easter Bread

Create a program that **calculates** how many **loaves** you can make with the **budget** you **have**.
 **First**, you will **receive** your **budget**. Then, you will **receive** the **price** for **1 kg flour**. Here is the **recipe** for **one** bread:

* **Eggs - 1 pack**
* **Flour - 1 kg**
* **Milk - 0.250 l**

The **price for 1 pack of eggs** is **75%** of the **price for 1 kg flour**. The **price** for **1l milk** is **25% more** than the price for **1 kg flour**. Notice that you need **0.250l milk** for **one** bread, and the calculated price is for **1l**.
**Start** cooking the loaves and **keep making** them until you have **enough budget**. Keep in mind that:
* For **every** bread that you make, you will receive **3 colored eggs**. 
* For **every 3rd** bread you make, you will lose some of your **colored** eggs **after receiving** the usual **3 colored eggs** for your bread. The count of eggs you will lose is calculated when you **subtract 2** from your **current count** of loaves – **({current_bread_count} – 2)**

In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have **left**, **formatted** to the **2nd decimal place**, in the following format:

**"You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."**

### Input / Constraints
* On the **1st line**, you will receive the budget – a **real number** in the range [0.0…100000.0]
* On the **2nd line**, you will receive the price for **1 kg flour** – a **real number** in the range [0.0…100000.0]
* The input will always be in the correct format
* You will **always** have a **remaining budget**
* There will **not** be a case in which the **eggs** become a **negative count**

### Output 
* In the end, print the **number** of **Easter bread** you have made, the colored **eggs** you have gathered, and the **money formatted** to **the 2nd** decimal place in the format described above.


## 15. Christmas Spirit

You will receive an **allowed quantity** for **one type** of decoration and **days left** until Christmas day to decorate the house.
There are **4 types** of decorations, and each piece costs a **price**
* Ornament Set – 2$ per piece
* Tree Skirt – 5$ per piece
* Tree Garlands – 3$ per piece
* Tree Lights – 15$ per piece

Every **second day** you buy an **Ornament Set** quantity of times and **increase** your Christmas spirit by **5**.

Every **third day** you buy **Tree Skirts** and **Tree Garlands** (both quantity of times) and **increase** your spirit by **13**.

Every **fifth day** you buy **Tree Lights** and **increase** your Christmas spirit by **17**. If you have bought Tree Skirts and Tree Garlands on the **same day**, you **additionally increase** your spirit by **30**.

Every **tenth day** you **lose 20 points of the spirit** because your cat ruins all tree decorations, and you should rebuild the tree and buy **one** piece of tree **skirt**, **garlands**, and **lights**. That is why you are forced to **increase** the allowed **quantity with 2** at the **beginning** of every **eleventh day**.

Also, if the **last day** is a **tenth day**, the cat demolishes even more and ruins the Christmas turkey, and you **lose** an additional **30 points of spirit**.

In the end, you must print the **total cost** and the **gained spirit**.

### Input / Constraints
The input will consist of **exactly 2 lines**:
* quantity – **integer in the range [1…100]**
* days – **integer in the range [1…100]**

### Output
In the end, print the **total cost** and the total gained **spirit** in the following format:
* **"Total cost: {budget}"**
* **"Total spirit: {totalSpirit}"**
