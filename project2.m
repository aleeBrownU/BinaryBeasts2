% Iowa Gambling Task Program
% Written by: Adrian Lee, Jack Waters, Kush Patel

% Tutorial Section

disp('Hi. This is the Iowa Gambling Task')
disp('In this task, you will start out with $5000, and your goal is to earn as much money as possible.')
disp('You will be presented with four card decks. When you draw a card from a deck, you will receive a monetary reward.')
disp('The amount of money you earn may differ between decks. There is also a chance for a penalty to occur.')
disp('This monetary penalty will deduct money. The amount of money deducted may differ between decks')
disp('') %line break
disp('You will draw a total of 100 cards. Earn the most amount of money with those 100 cards.')
disp('We will start now:')

% Actual Task Section

money = 5000; %initial money
prob = 0.5; %probability of GETTING a deduction
Aplus = 100; %when you pick on the card deck, you add this much money
Bplus = 100;
Cplus = 50;
Dplus = 50;
Aminus = 250; %Penalty amount you get deducted for each deck
Bminus = 250;
Cminus = 50;
Dminus = 250;


for round = 1:10 %number of card rounds. Will bump up to 100 later
    good_input = 0;
    while good_input <1 %to ensure that the correct input is given
        user = input('Pick a deck: A(1), B(2), C(3), D(4) (enter the number)\n');
        if user == 1 || user == 2 || user == 3 || user == 4
            good_input = 1;
        else
            disp('Not a valid input. Please try again.')
        end
    end
    
    
    
    
end


% Data Section



