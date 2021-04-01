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

initial = 5000; %initial money
money = initial; %used later as the running money count
prob = 0.5; %probability of GETTING a deduction (range from 0 to 1)
Aplus = 100; %when you pick on the card deck, you add this much money
Bplus = 100;
Cplus = 50;
Dplus = 50;
Aminus = 250; %Penalty amount you get deducted for each deck
Bminus = 250;
Cminus = 50;
Dminus = 250;

fprintf('You currently have $%d\n',money) %displays money amount

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
    
    if rand(1)<=prob %determines if penalty should occur
        penalty = true;
    else
        penalty = false;
    end
    
    
    if user == 1 %allocates money changes and displays messages about 
        fprintf('You earned $%d\n',Aplus)
        money = money+Aplus; %adds the money
        if penalty %if a penalty is to be given
            fprintf('A penalty was given. You lost $%d\n',Aminus)
            money = money-Aminus; %subtracts the money
        end
        fprintf('You currently have $%d\n',money) %displays money amount
    elseif user == 2
        fprintf('You earned $%d\n',Bplus)
        money = money+Bplus;
        if penalty
            fprintf('A penalty was given. You lost $%d\n',Bminus)
            money = money-Bminus;
        end
        fprintf('You currently have $%d\n',money) %displays money amount
    elseif user == 3
        fprintf('You earned $%d\n',Cplus)
        money = money+Cplus;
        if penalty
            fprintf('A penalty was given. You lost $%d\n',Cminus)
            money = money-Cminus;
        end
        fprintf('You currently have $%d\n',money) %displays money amount
    elseif user == 4
        fprintf('You earned $%d\n',Dplus)
        money = money+Dplus;
        if penalty
            fprintf('A penalty was given. You lost $%d\n',Dminus)
            money = money-Dminus;
        end
        fprintf('You currently have $%d\n',money) %displays money amount
    end
    
    
end


% Data Section

fprintf('Your total at the end of this task was $%d\n',money)
net_earnings = money-initial;
fprintf('Your total earnings overall for this task was $%d\n',net_earnings)
if net_earnings < 0
    disp('Too bad. You lost more than you gambled for.')
elseif net_earnings == 0
    disp('Wow. You neither won nor lost money.')
else
    disp('Congrats. You earned money today...virtually. Non-redeemable.')
end


disp('Thanks for playing.')